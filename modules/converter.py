from abc import ABC, abstractmethod
import os, sys
from PIL import Image

class AImageConverter(ABC):

    @abstractmethod
    def convert(source_path, destination_path):
        pass

class ImageConverterJpgToPng(AImageConverter):
    
    def convert(source_path, destination_path):
        file = os.path.splitext(source_path)
        outfile = str(destination_path) + str(file) + '.png'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("cannot convert", file)

class ImageConverterPngToJpg(AImageConverter):
        
    def convert(source_path, destination_path):
        file = os.path.splitext(source_path)
        outfile = str(destination_path) + str(file) + '.jpg'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("cannot convert", file)