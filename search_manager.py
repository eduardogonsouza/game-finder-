from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from steam_search import search_steam
from nuuvem_search import search_nuuvem
from epic_search import search_epic, get_free_epic_games

class SearchManager:
    def __init__(self):
        self.driver = None
        self.wait = None
    
    def setup_driver(self, headless=False):
        options = webdriver.ChromeOptions()
        
        if headless:
            options.add_argument('--headless')
        else:
            options.add_argument('--start-minimized')
            options.add_argument('--window-position=-2000,-2000')
            
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-logging')
        options.add_argument('--log-level=3')
        options.add_argument('--silent')
        
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('useAutomationExtension', False)
        
        self.driver = webdriver.Chrome(options=options)
        
        if not headless:
            self.driver.minimize_window()
            
        self.wait = WebDriverWait(self.driver, 10)
    
    def search_all_platforms(self, platforms, game_name):
        use_headless = "epic" not in platforms
        self.setup_driver(headless=use_headless)
        results = []
        
        try:
            for platform in platforms:
                result = None
                if platform == 'steam':
                    result = search_steam(self.driver, game_name, self.wait)
                elif platform == 'nuuvem':
                    result = search_nuuvem(self.driver, game_name, self.wait)
                elif platform == 'epic':
                    result = search_epic(self.driver, game_name, self.wait)
                
                if result:
                    results.append(result)
                    
        except Exception as e:
            pass
        finally:
            if self.driver:
                self.driver.quit()
        
        return results
    
    def get_free_epic_games(self):
        self.setup_driver(headless=False)
        
        try:
            results = get_free_epic_games(self.driver, self.wait)
            return results if results else []
        except Exception as e:
            return []
        finally:
            if self.driver:
                self.driver.quit()
