import logging

from selenium.webdriver.remote.webelement import WebElement

from .runner import Runner

class SteamRunner(Runner):
    def __init__(self) -> None:
        """Steam installer runner."""
        super().__init__(headless=True)
    
    def get_installer_element(self) -> WebElement:
        logging.info('Downloading Steam installer')
        self.browser.get('https://store.steampowered.com/about/')
        
        website_as = self.browser.find_elements_by_tag_name('a')
        installer_buttons = list(filter(lambda x: str(x.get_attribute('href')).endswith('client/installer/SteamSetup.exe'), website_as))
        
        if not installer_buttons:
            return None

        return installer_buttons[0]