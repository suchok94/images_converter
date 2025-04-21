from abc import ABC, abstractmethod
import os, sys
from PIL import Image

class ImageConverter(ABC):

    @abstractmethod
    def convert(source_path, destination_path):
        pass

class ImageConverterJpgToPng(ImageConverter):
    
    def convert(source_path, destination_path):
        file = os.path.splitext(source_path)
        outfile = destination_path + file + '.png'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("cannot convert", file)

class ImageConverterPngToJpg(ImageConverter):
        
    def convert(source_path, destination_path):
        file = os.path.splitext(source_path)
        outfile = destination_path + file + '.jpg'
        try:
            with Image.open(source_path) as im:
                  im.save(outfile)
        except OSError:
            print("cannot convert", file)