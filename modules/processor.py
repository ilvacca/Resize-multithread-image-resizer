import time, os
from PIL import Image
from multiprocessing import Pool, cpu_count
from itertools import product

class Processor:

    def __init__(self):
        self.objectName = "PROCESSOR"
        self.threadsNumber = cpu_count()

    # PROCESS ##########################################################################################################

    # Resizes an image with a given size
    def resize(self, im, outputMaxSize, outputResamplingAlgorithm):
        if im.size[0] == max(im.size):
            resized = im.resize((outputMaxSize, int(im.size[1] * (outputMaxSize / im.size[0]))), outputResamplingAlgorithm)
        else:
            resized = im.resize((int(im.size[0] * (outputMaxSize / im.size[1])), outputMaxSize), outputResamplingAlgorithm)
        return resized

    def convert(self, image, outputImageQuality, outputImageSuffix, outputResamplingAlgorithm, outputMaxSize):
        im = Image.open(image, mode="r")
        self._logger("Resizing '%s' %s" % (im.filename, im.size))
        resized = self.resize(im, outputMaxSize, outputResamplingAlgorithm)
        filename, extension = os.path.splitext(im.filename)
        outfile = "%s%s%s" % (filename,outputImageSuffix,extension)
        exif = im.info["exif"] if im.format != 'PNG' else ""
        resized.save(outfile, quality=outputImageQuality, exif=exif)
        im.close(), resized.close()
        self._logger("Resized '%s' %s" % (im.filename, im.size))

    def process(self, bucketObj, optionsObj):
        outputImageQuality = optionsObj.outputImageQuality
        outputImageSuffix = optionsObj.outputImageSuffix
        outputResamplingAlgorithm = optionsObj.outputResamplingAlgorithm
        outputSize = optionsObj.outputSize
        if bucketObj.isFilled:
            self._logger("Processing")
            pool = Pool(self.threadsNumber)
            pool.starmap(self.convert, product(bucketObj.bucket, [outputImageQuality], [outputImageSuffix], [outputResamplingAlgorithm], [outputSize]))
            self._logger("Processed")
            return(True)
        else:
            self._logger("I cannot process an emtpy bucket")
            return(False)

    # LOGGER ###########################################################################################################

    def _logger(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self.objectName, message)
        print(message)

    def _loggerReturn(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self.objectName, message)
        return(message)

if __name__ == "__main__":

    from bucket import Bucket

    myBucket = Bucket()
    myBucket.fill()

    myProc = Processor()
    myProc.setOutputCharacteristics()
    myProc.process(myBucket)