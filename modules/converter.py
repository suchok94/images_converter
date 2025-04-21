from abc import ABC, abstractmethod
import os
from PIL import Image

class AImageConverter(ABC):

    @abstractmethod
    def convert(source_path, destination_path):
        pass

class ImageConverterJpgToPng(AImageConverter):
    
    def convert(source_path, destination_path):
        file, e = os.path.splitext(source_path)
        outfile = os.path.join(destination_path, file) + '.png'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("Не получилось сконвертировать", file, 'в png')

class ImageConverterPngToJpg(AImageConverter):
        
    def convert(source_path, destination_path):
        file, e = os.path.splitext(source_path)
        outfile = os.path.join(destination_path, file) + '.jpg'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("Не получилось сконвертировать", file, 'в jpg')