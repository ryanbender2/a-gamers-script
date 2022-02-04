pyinstaller ^
--noconfirm ^
--onefile ^
--console ^
--clean ^
--name="AGamersScript" ^
--add-data "./src/runners;runners/" ^
--add-data "./src/__init__.py;." ^
--add-data "./src/agamersscript.py;." ^
--add-data "./src/logger.py;." ^
--hidden-import="selenium" ^
--hidden-import="selenium.webdriver.remote.webelement" ^
--hidden-import="selenium.webdriver.support.expected_conditions" ^
--hidden-import="selenium.webdriver.support.ui" ^
--hidden-import="webdriver_manager.chrome" ^
--icon="./images/app.ico" ^
"./src/main.py"