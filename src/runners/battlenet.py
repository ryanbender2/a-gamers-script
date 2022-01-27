import logging

from selenium.webdriver.remote.webelement import WebElement

from .runner import Runner

class BattleNetRunner(Runner):
    def __init__(self) -> None:
        """Battle.net installer runner."""
        super().__init__(headless=False)
    
    def get_installer_element(self) -> WebElement:
        logging.info('Downloading Battle.net installer')
        self.browser.get('https://www.blizzard.com/en-us/download?product=bnetdesk')
        
        

        return None
