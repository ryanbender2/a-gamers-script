import threading
from abc import ABC, abstractmethod

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class Runner(ABC, threading.Thread):
    """Base runner class."""
    def __init__(self, headless=True) -> None:
        """Base dependency downloader runner class.

        Args:
            headless (bool, optional): headless browser. Defaults to True.
        """
        super().__init__()
        options = webdriver.ChromeOptions()
        options.headless = headless
        self.browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    
    def run(self) -> None:
        self.download_dependency()
        self.browser.close()

    @abstractmethod
    def download_dependency(self) -> None:
        """
            This method is meant to be overridden by subclasses to perform
            the operations needed to download dependencies.
        
            This class contains the self.browser, which is the browser for
            this runner. Use it to go to the dependency's website and download
            the dependency. In this method, do not close the browser, that will
            be handled automatically.
        """
        ...
