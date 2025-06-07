from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def search_nuuvem(driver, game_name, wait):
    try:
        search_url = f"https://www.nuuvem.com/br-pt/catalog/page/1/search/{game_name.replace(' ', '%20')}"
        driver.get(search_url)
        time.sleep(3)
        
        games = []
        game_selectors = [
            "article.game-card",
            ".product-card",
            ".game-item",
            "[data-testid='game-card']",
            "div[class*='card'][class*='game']"
        ]
        
        for selector in game_selectors:
            try:
                games = driver.find_elements(By.CSS_SELECTOR, selector)
                if games:
                    break
            except:
                continue
        
        if not games:
            return None
        
        def name_matches(title, search_term):
            title_lower = title.lower().strip()
            search_lower = search_term.lower().strip()
            
            common_words = ['the', 'a', 'an', 'of', 'in', 'on', 'at', 'to', 'for', 'with', 'by']
            
            title_words = [word for word in title_lower.split() if word not in common_words]
            search_words = [word for word in search_lower.split() if word not in common_words]
            
            if search_lower == title_lower:
                return True, 100
            
            if search_lower in title_lower:
                if len(search_lower) >= 4:
                    return True, 90
            
            if len(search_words) == 0:
                return False, 0
                
            matching_words = 0
            for search_word in search_words:
                for title_word in title_words:
                    if search_word == title_word:
                        matching_words += 1
                        break
                    elif len(search_word) >= 5 and len(title_word) >= 5:
                        if search_word in title_word or title_word in search_word:
                            matching_words += 0.7
                            break
            
            match_percentage = matching_words / len(search_words)
            
            if match_percentage >= 0.8 and matching_words >= 1:
                return True, match_percentage * 80
            
            return False, match_percentage * 40
        
        base_game = None
        best_match = None
        best_score = 0
        
        for g in games[:10]:
            try:
                title_selectors = [
                    ".game-card__product-name",
                    ".product-name",
                    "h3",
                    "[data-testid='product-name']",
                    ".title"
                ]
                
                title = ""
                for selector in title_selectors:
                    try:
                        title_elem = g.find_element(By.CSS_SELECTOR, selector)
                        title = title_elem.text.strip()
                        if title:
                            break
                    except:
                        continue
                
                if title:
                    if any(keyword in title.lower() for keyword in ["dlc", "bundle", "pack", "expansion", "season pass"]):
                        continue
                    
                    matches, score = name_matches(title, game_name)
                    
                    if matches and score > best_score:
                        best_score = score
                        best_match = g
                        
                        if score >= 90:
                            base_game = g
                            break
            except:
                continue
        
        if not base_game and best_match and best_score >= 60:
            base_game = best_match
        
        if not base_game:
            return None
        
        game = base_game
        
        name = "Jogo encontrado"
        name_selectors = [
            ".game-card__product-name",
            ".product-name",
            "h3",
            "[data-testid='product-name']",
            ".title"
        ]
        
        for selector in name_selectors:
            try:
                name_elem = game.find_element(By.CSS_SELECTOR, selector)
                if name_elem and name_elem.text.strip():
                    name = name_elem.text.strip()
                    break
            except:
                continue
        
        url = "https://www.nuuvem.com/"
        try:
            url_elem = game.find_element(By.CSS_SELECTOR, "a")
            url = url_elem.get_attribute("href")
            if url and not url.startswith("http"):
                url = f"https://www.nuuvem.com{url}"
        except:
            pass
        
        discount = "Sem desconto"
        has_discount = False
        
        discount_selectors = [
            ".discount-percentage",
            ".badge-discount",
            "[data-testid='discount']",
            ".discount"
        ]
        
        for selector in discount_selectors:
            try:
                discount_elem = game.find_element(By.CSS_SELECTOR, selector)
                if discount_elem and discount_elem.text.strip():
                    discount = discount_elem.text.strip()
                    has_discount = True
                    break
            except:
                continue
        
        current_price = "Verificar na loja"
        price_selectors = [
            ".product-price--val",
            ".add-to-cart__btn__text",
            ".price",
            "[data-testid='price']",
            ".current-price"
        ]
        
        for selector in price_selectors:
            try:
                price_elem = game.find_element(By.CSS_SELECTOR, selector)
                price_text = price_elem.text.strip()
                if price_text and ("R$" in price_text or "gratuito" in price_text.lower() or "free" in price_text.lower()):
                    current_price = price_text
                    break
            except:
                continue
        
        return {
            'platform': 'Nuuvem',
            'name': name,
            'url': url,
            'discount': discount,
            'has_discount': has_discount,
            'original_price': current_price,
            'current_price': current_price
        }
        
    except Exception as e:
        return None
