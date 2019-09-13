from modules.bucket import Bucket
from modules.processor import Processor
from modules.options import Options

import time

class Controller:

    def __init__(self):
        self._objectName = "CONTROLLER"
        self._bucket = Bucket()
        self._processor = Processor()
        self._options = Options()

    # USE CASES ########################################################################################################

    def resizeImages(self):
        counter = 0
        self._logger("Start resizing process")
        while (not self._bucket.isFilled) and (counter < 3):
            self._bucket.fill()
            counter += 1
        if self._bucket.isFilled:
            self._options.setOutputOptions()
            self._processor.process(self._bucket, self._options)
        self._logger("Ended resizing process")

    # LOGGER ###########################################################################################################

    def _logger(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self._objectName, message)
        print(message)

if __name__ == "__main__":

    con = Controller()
    con.resizeImages()
