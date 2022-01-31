import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .runner import Runner

class GeForceExperienceRunner(Runner):
    """GeForce Experience installer runner."""
    def __init__(self) -> None:
        super().__init__(headless=True)
    
    def get_installer_element(self) -> WebElement:
        logging.info('Downloading GeForce Experience installer')
        self.browser.get('https://www.nvidia.com/en-us/geforce/drivers/')
        return self.browser.find_element(By.ID, 'gfeDwnd')
