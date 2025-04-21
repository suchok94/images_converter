from abc import ABC, abstractmethod
from modules.converter import ImageConverterJpgToPng, ImageConverterPngToJpg

class AConverterCreator(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def create_converter():
        pass


class ConverterCreatorJpgToPng(AConverterCreator):

    def __init__(self):
        pass

    def create_converter(self, source_path, destination_path):
        return ImageConverterJpgToPng.convert(source_path, destination_path)

class ConverterCreatorPngToJpg(AConverterCreator):
    
    def __init__(self):
        pass

    def create_converter(self, source_path, destination_path):
        return ImageConverterPngToJpg.convert(source_path, destination_path)

