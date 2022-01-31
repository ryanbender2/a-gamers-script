from locale import strcoll
import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .runner import Runner

class MSIAfterburnerRunner(Runner):
    """MSI Afterburner installer runner."""
    def __init__(self) -> None:
        super().__init__(headless=True)
    
    def get_installer_element(self) -> WebElement:
        logging.info('Downloading MSI Afterburner installer')
        self.browser.get('https://www.msi.com/Landing/afterburner/graphics-cards')

        website_as = self.browser.find_elements(By.TAG_NAME, 'a')
        website_as = list(filter(lambda x: 'MSIAfterburnerSetup' in str(x.get_attribute('href')), website_as))

        if not website_as:
            return None
        return website_as[0]
