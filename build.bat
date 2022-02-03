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
--hidden-import="webdriver_manager.chrome" ^
--icon="./app.ico" ^
"./src/main.py"