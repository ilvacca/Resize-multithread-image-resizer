import time
from tkinter import Tk, filedialog

class Bucket:

    def __init__(self):
        self.objectName = "BUCKET"
        self.empty()
        self.isFilled = False

    # FILL / EMPTY #####################################################################################################

    def fill(self):
        Tk().withdraw()
        self.bucket = filedialog.askopenfilenames(title="Select images to convert",filetypes=(
            ("JPG files","*.jpg *.jpeg"),("PNG files","*.png"),("TIFF files","*.tiff *.tif"),("ALL files","*.*")
        ))
        self.bucketSize = len(self.bucket)
        if self.bucketSize != 0:
            self._logger("Filled bucket with %s photos" % self.bucketSize)
            self.isFilled = True
        else:
            self._logger("Bucket still empty")
            self.isFilled = False

    def empty(self):
        self.bucket = []
        self.bucketSize = 0
        self.isFilled = False
        self._logger("The bucket is now empty")

    # LOGGER ###########################################################################################################

    def _logger(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self.objectName, message)
        print(message)


if __name__ == "__main__":

    myBucket = Bucket()
    myBucket.fill()
    print(myBucket)