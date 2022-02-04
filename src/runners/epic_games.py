import logging

from selenium.webdriver.remote.webelement import WebElement

from .runner import Runner

class EpicGamesRunner(Runner):
    """Epic Games installer runner."""
    def __init__(self) -> None:
        super().__init__('Epic Games')
    
    def get_installer_element(self) -> WebElement:
        logging.info('Starting Epic Games')
        self.browser.get('https://www.epicgames.com/store/en-US/download')
        epic_games_as = self.browser.find_elements_by_tag_name('a')
        download_buttons = list(filter(lambda ele: str(ele.get_attribute('href')).endswith('EpicGamesLauncherInstaller.msi'), epic_games_as))
        
        if not download_buttons:
            return None

        return download_buttons[0]