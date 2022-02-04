import logging
import time

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .runner import Runner

class BattleNetRunner(Runner):
    """Battle.net installer runner."""
    def __init__(self) -> None:
        super().__init__('Battle.net')
    
    def get_installer_element(self) -> WebElement:
        logging.info('Starting Battle.net')
        self.browser.get('https://www.blizzard.com/en-us/download?product=bnetdesk')
        
        battle_net_desktop_button = self.browser.find_element(By.ID, 'bnetdesk')
        battle_net_desktop_button.click()

        time.sleep(1)

        modal = self.browser.find_element(By.ID, 'modal_bnetdesk')
        download_button = modal.find_element(By.TAG_NAME, 'a')

        download_button.click()

        time.sleep(8)

        return self.browser.find_element(By.CLASS_NAME, 'textArea')
