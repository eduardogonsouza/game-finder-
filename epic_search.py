from selenium.webdriver.common.by import By
import time

def search_epic(driver, game_name, wait):
    try:
        search_url = f"https://store.epicgames.com/en-US/browse?q={game_name.replace(' ', '%20')}"
        driver.get(search_url)
        time.sleep(5)
        
        try:
            no_results_span = driver.find_elements(By.XPATH, "//span[text()='No results found']")
            if no_results_span:
                return None
        except:
            pass
        
        games = []
        try:
            games_list = driver.find_element(By.CSS_SELECTOR, "ul.css-cnqlhg")
            games = games_list.find_elements(By.CSS_SELECTOR, "li.css-lrwy1y")
        except:
            try:
                games = driver.find_elements(By.CSS_SELECTOR, "div[data-component='BrowseOfferCard']")
            except:
                pass
        
        if not games:
            return None
        
        base_game = None
        for game in games[:3]:
            try:
                category_elem = game.find_element(By.CSS_SELECTOR, "span.eds_1ypbntd0.eds_1ypbntdd.eds_1ypbntdk.css-1247nep span")
                if category_elem and "base game" in category_elem.text.lower():
                    base_game = game
                    break
            except:
                continue
        
        if not base_game:
            base_game = games[0]
        
        game = base_game
        
        name = "Jogo encontrado"
        try:
            name_elem = game.find_element(By.CSS_SELECTOR, "div.css-rgqwpc")
            if name_elem and name_elem.text.strip():
                name = name_elem.text.strip()
        except:
            try:
                img_elem = game.find_element(By.CSS_SELECTOR, "img")
                alt_text = img_elem.get_attribute("alt")
                if alt_text and alt_text.strip():
                    name = alt_text.strip()
            except:
                pass
        
        url = "https://store.epicgames.com/"
        try:
            link_elem = game.find_element(By.CSS_SELECTOR, "a.css-g3jcms")
            url = link_elem.get_attribute("href")
            if url and not url.startswith("http"):
                url = f"https://store.epicgames.com{url}"
        except:
            pass
        
        discount = "Sem desconto"
        has_discount = False
        try:
            discount_elem = game.find_element(By.CSS_SELECTOR, "span.eds_1xxntt819")
            if discount_elem and discount_elem.text.strip():
                discount = discount_elem.text.strip()
                has_discount = True
        except:
            pass
        
        current_price = "Verificar na loja"
        original_price = "Verificar na loja"
        
        try:
            current_price_elem = game.find_element(By.CSS_SELECTOR, "span.eds_1ypbntd0.eds_1ypbntdc.eds_1ypbntdk.css-12s1vua")
            if current_price_elem and current_price_elem.text.strip():
                current_price = current_price_elem.text.strip()
        except:
            pass
        
        if has_discount:
            try:
                original_price_elem = game.find_element(By.CSS_SELECTOR, "span.css-4jky3p")
                if original_price_elem and original_price_elem.text.strip():
                    original_price = original_price_elem.text.strip()
            except:
                original_price = current_price
        else:
            original_price = current_price
        
        result = {
            'platform': 'Epic Games',
            'name': name,
            'url': url,
            'discount': discount,
            'has_discount': has_discount,
            'original_price': original_price,
            'current_price': current_price
        }
        
        return result
        
    except Exception as e:
        return None

def get_free_epic_games(driver, wait):
    try:
        driver.get("https://store.epicgames.com/en-US/free-games")
        time.sleep(5)
        
        free_games = []
        
        main_container = driver.find_element(By.CSS_SELECTOR, ".css-1myhtyb")
        
        game_cards = main_container.find_elements(By.CSS_SELECTOR, ".css-17st2kc")
        
        for card in game_cards:
            try:
                is_free_now = False
                is_coming_soon = False
                
                card_text = card.text.lower()
                
                if "free now" in card_text:
                    is_free_now = True
                
                if "coming soon" in card_text:
                    is_coming_soon = True
                
                try:
                    spans = card.find_elements(By.TAG_NAME, "span")
                    for span in spans:
                        span_text = span.text.lower().strip()
                        if "free now" in span_text:
                            is_free_now = True
                        if "coming soon" in span_text:
                            is_coming_soon = True
                except:
                    pass
                
                try:
                    status_divs = card.find_elements(By.CSS_SELECTOR, "div")
                    for div in status_divs:
                        div_text = div.text.lower().strip()
                        if "free now" in div_text:
                            is_free_now = True
                        if "coming soon" in div_text:
                            is_coming_soon = True
                except:
                    pass
                
                if not (is_free_now or is_coming_soon):
                    continue
                
                name = "Jogo Gratuito"
                try:
                    name_elem = card.find_element(By.CSS_SELECTOR, "h6")
                    if name_elem and name_elem.text.strip():
                        name = name_elem.text.strip()
                except:
                    try:
                        img_elem = card.find_element(By.CSS_SELECTOR, "img")
                        alt_text = img_elem.get_attribute("alt")
                        if alt_text and alt_text.strip():
                            name = alt_text.strip()
                    except:
                        pass
                
                if name == "Jogo Gratuito":
                    continue
                
                url = "https://store.epicgames.com/"
                try:
                    link_elem = card.find_element(By.CSS_SELECTOR, "a")
                    url = link_elem.get_attribute("href")
                    if url and not url.startswith("http"):
                        url = f"https://store.epicgames.com{url}"
                except:
                    pass
                
                availability = "Disponível"
                try:
                    p_elements = card.find_elements(By.TAG_NAME, "p")
                    for p in p_elements:
                        p_text = p.text.strip()
                        if p_text and ("free" in p_text.lower() or "jun" in p_text.lower() or ":" in p_text):
                            availability = p_text
                            break
                except:
                    pass
                
                if is_free_now:
                    status = "🆓 GRATUITO AGORA"
                elif is_coming_soon:
                    status = "🔜 EM BREVE"
                else:
                    status = "🆓 GRATUITO"
                
                free_games.append({
                    'platform': 'Epic Games',
                    'name': name,
                    'url': url,
                    'discount': status,
                    'has_discount': False,
                    'original_price': availability,
                    'current_price': status
                })
                
            except Exception as e:
                continue
        
        return free_games
        
    except Exception as e:
        return []
