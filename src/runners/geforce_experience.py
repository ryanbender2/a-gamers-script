import logging

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By

from .runner import Runner

class GeForceExperienceRunner(Runner):
    """GeForce Experience installer runner."""
    def __init__(self) -> None:
        super().__init__('GeForce Experience')
    
    def get_installer_element(self) -> WebElement:
        logging.info('Starting GeForce Experience')
        self.browser.get('https://www.nvidia.com/en-us/geforce/drivers/')
        return self.browser.find_element(By.ID, 'gfeDwnd')
