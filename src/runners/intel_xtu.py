import logging
import re

from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .runner import Runner

class IntelXTURunner(Runner):
    """Intel Extreme Tuning Utility installer runner."""
    def __init__(self) -> None:
        super().__init__('Intel Extreme Tuning Utility')
    
    def get_installer_element(self) -> WebElement:
        logging.info('Starting Intel Extreme Tuning Utility')
        self.browser.get('https://www.intel.com/content/www/us/en/download-center/home.html')

        products = self.browser.find_elements(By.CLASS_NAME, 'simple-card-item')

        processors_button = list(filter(lambda x: str(x.find_element(By.TAG_NAME, 'a').get_attribute('href')).find('Processors') > 0, products))[0]
        processors_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'coveo-result-list-container'))
        )

        search_results = self.browser.find_elements(By.CLASS_NAME, 'CoveoResultLink')

        intel_xtu_button = list(filter(lambda item: re.match('Intel.*Extreme Tuning Utility.*', str(item.get_attribute('title'))), search_results))[0]
        intel_xtu_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'dc-page-short-description__title'))
        )

        page_buttons = self.browser.find_elements(By.TAG_NAME, 'button')
        
        download_button = list(filter(lambda btn: str(btn.get_attribute('data-href')).find('XTUSetup') > 0, page_buttons))[0]
        download_button.click()

        WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'license-modal-content-license__btn'))
        )
        
        return self.browser.find_element(By.CLASS_NAME, 'license-modal-content-license__btn')
