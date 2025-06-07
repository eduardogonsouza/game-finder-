from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def search_steam(driver, game_name, wait):
    try:
        driver.get("https://store.steampowered.com/")
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "store_nav_search_term")))
        
        search_box.clear()
        search_box.send_keys(game_name)
        search_box.send_keys(Keys.ENTER)
        
        time.sleep(2)
        games = driver.find_elements(By.CLASS_NAME, "search_result_row")
        
        if not games:
            return None
            
        game = games[0]
        name = game.find_element(By.CLASS_NAME, "title").text
        url = game.get_attribute("href") or "https://store.steampowered.com/"
        
        try:
            discount = game.find_element(By.CLASS_NAME, "search_discount").text.strip()
            has_discount = True
        except:
            discount = "Sem desconto"
            has_discount = False
        
        try:
            price_text = game.find_element(By.CSS_SELECTOR, 
                ".search_price_discount_combined, .search_price, .col.search_price").text.strip()
        except:
            price_text = "Gratuito para Jogar"
        
        if has_discount and "R$" in price_text and price_text.count("R$") >= 2:
            prices = price_text.split("R$")
            original_price = f"R${prices[1].strip()}"
            current_price = f"R${prices[2].strip()}"
        else:
            original_price = current_price = price_text or "N/A"
        
        return {
            'platform': 'Steam',
            'name': name,
            'url': url,
            'discount': discount,
            'has_discount': has_discount,
            'original_price': original_price,
            'current_price': current_price
        }
    except Exception as e:
        return None
