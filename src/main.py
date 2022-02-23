import logging
import multiprocessing
from ui import AGamersScriptUI
import utils

"""
Dev note:
There is something wrong with selenium where
you have you modify a variable in its source
to stop the console windows from opening for
the chromedrivers. It is located here:
python\Lib\site-packages\selenium\webdriver\common\service.py

Here:
self.process = subprocess.Popen(cmd, env=self.env,
                                close_fds=system() != 'Windows',
                                stdout=self.log_file,
                                stderr=self.log_file,
                                stdin=PIPE,
                                creationflags=0x08000000)
Update the creationflags kwarg to the value 0x08000000 as seen above.
"""


def main() -> None:
    utils.setup_logging()
    utils.create_installers_directory()
    logging.info("Starting AGamersScript")

    # start the main script workers in a separate process
    agamersscript_process = multiprocessing.Process(target=utils.start_agamersscript)
    agamersscript_process.start()

    # create tkinter ui
    a_gamers_script_ui = AGamersScriptUI()

    # check every 250 ms to see if the main worker process is finished downloading installers
    a_gamers_script_ui.after(250, utils.check_downloader, agamersscript_process, a_gamers_script_ui)

    # call the tkinter main loop
    a_gamers_script_ui.mainloop()

if __name__ == '__main__':
    multiprocessing.freeze_support()
    main()
