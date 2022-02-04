import time
import threading
import logging
from abc import ABC, abstractmethod
import os
from pathlib import Path

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from webdriver_manager.chrome import ChromeDriverManager

class Runner(ABC, threading.Thread):
    """Base runner class."""
    def __init__(self, installer_name: str, headless=True) -> None:
        """Base dependency downloader runner class.

        Args:
            installer_name (str): The installer's name being downloaded.
            headless (bool, optional): headless chrome browser. Defaults to True.
        """
        super().__init__()

        self.installer_name = installer_name

        options = webdriver.ChromeOptions()
        options.headless = headless

        installers_dir_path = Path('./AGamersInstallers')
        self.installers_output_dir = str(installers_dir_path.absolute())

        prefs = {
            'download.default_directory': self.installers_output_dir,
            'download.prompt_for_download': False,
            'safebrowsing.enabled': True
        }
        options.add_experimental_option('prefs', prefs)
        options.add_argument('--safebrowsing-disable-download-protection')

        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    def run(self) -> None:
        download_button = self.get_installer_element()
        if download_button is not None:
            logging.info(f'Started downloading {self.installer_name}!')
            self.__wait_for_download__(download_button)
            logging.info(f'Finished downloading {self.installer_name}!')
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
