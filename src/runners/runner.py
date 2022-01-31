import time
import threading
from abc import ABC, abstractmethod
import os

from settings import get_settings

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

class Runner(ABC, threading.Thread):
    """Base runner class."""
    def __init__(self, headless=True) -> None:
        """Base dependency downloader runner class.

        Args:
            headless (bool, optional): headless chrome browser. Defaults to True.
        """
        super().__init__()

        options = webdriver.ChromeOptions()
        options.headless = headless

        settings = get_settings()
        self.installers_output_dir = settings.installers_output_directory

        prefs = {
            'download.default_directory': settings.installers_output_directory,
            'download.prompt_for_download': False,
            'safebrowsing.enabled': True
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--safebrowsing-disable-download-protection')

        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    def run(self) -> None:
        download_button = self.get_installer_element()
        if download_button is not None:
            self.__wait_for_download__(download_button)
        self.browser.close()
    
    def __wait_for_download__(self, download_button: WebElement) -> None:
        download_button.click()
        time.sleep(2)
        dl_wait = True
        while dl_wait:
            time.sleep(1)
            dl_wait = False
            files = os.listdir(self.installers_output_dir)
            for fname in files:
                if fname.endswith('.crdownload'):
                    dl_wait = True

    @abstractmethod
    def get_installer_element(self) -> WebElement:
        """
            This method is meant to be overridden by subclasses to perform
            the operations needed to get the download installer element.
        
            This method should return the WebElement in the installer website
            that is used to download the installer.
        """
        ...
