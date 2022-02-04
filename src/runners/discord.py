import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .runner import Runner

class DiscordRunner(Runner):
    """Discord installer runner."""
    def __init__(self) -> None:
        super().__init__('Discord')
    
    def get_installer_element(self) -> WebElement:
        logging.info('Starting Discord')
        self.browser.get('https://discord.com/download')

        website_as = self.browser.find_elements(By.TAG_NAME, 'a')
        download_as = list(filter(lambda x: 'app/installers/latest' in x.get_attribute('href'), website_as))

        if not download_as:
            return None
        return download_as[0]
