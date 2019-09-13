from PIL import Image
import time, os

class Options:

    def __init__(self):
        self.objectName = "OPTIONS"
        self.setDefault()

    # SETTER ###########################################################################################################

    def setDefault(self):
        self.outputImageQuality = 95
        self.outputImageSuffix = ""
        self.outputResamplingAlgorithm = Image.BILINEAR
        self.outputSize = 1000
        self.outputDirectory = ""

    def setOutputImageQuality(self, outputImageQuality):
        self.outputImageQuality = outputImageQuality
        self._logger("Output image quality is now '%s'" % self.outputImageQuality)

    def setOutputImageSuffix(self, outputImageSuffix):
        self.outputImageSuffix = outputImageSuffix
        self._logger("Output image suffix is now '%s'" % self.outputImageSuffix)

    def setOutputResamplingAlgorithm(self, outputResamplingAlgorithm):
        self.outputResamplingAlgorithm = outputResamplingAlgorithm
        self._logger("Output resampling algorithm is now '%s'" % self.outputResamplingAlgorithm)

    def setOutputSize(self, outputSize):
        self.outputSize = outputSize
        self._logger("Output max image size is now '%s'" % self.outputSize)

    # PROMPT INTERFACE #################################################################################################

    def setOutputOptions(self):
        keyboardInput = input(self._loggerReturn("Insert desired output image quality [0-100] (default: 95): "))
        keyboardInput = 95 if keyboardInput == "" else int(keyboardInput.strip())
        self.setOutputImageQuality(keyboardInput)
        keyboardInput = input(self._loggerReturn("Insert desired suffix for conversion [ex. MYIMAGE_SUFFIX.jpg] (default: None): "))
        keyboardInput = "" if keyboardInput == "" else ("_"+keyboardInput.strip())
        self.setOutputImageSuffix(keyboardInput)
        keyboardInput = input(self._loggerReturn("Insert desired resampling algorithm [NN, BIL] (default: Bilinear): "))
        keyboardInput = Image.BILINEAR if ((keyboardInput == "") or (keyboardInput.upper() == "BIL") ) else (Image.NEAREST)
        self.setOutputResamplingAlgorithm(keyboardInput)
        keyboardInput = input(self._loggerReturn("Insert desired max output size (default: 1000): "))
        keyboardInput = 1000 if keyboardInput == "" else int(keyboardInput.strip())
        self.setOutputSize(keyboardInput)

    # LOGGER ###########################################################################################################

    def _logger(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self.objectName, message)
        print(message)

    def _loggerReturn(self, message):
        now = time.strftime("%H:%M:%S", time.localtime())
        message = "%s [%s]: %s" % (now, self.objectName, message)
        return(message)