from abc import ABC, abstractmethod
import os
from PIL import Image

class AImageConverter(ABC):

    @abstractmethod
    def convert(source_path, destination_path):
        pass

class ImageConverterJpgToPng(AImageConverter):
    
    def convert(source_path, destination_path):
        if Checker.file_exists(source_path):
            file = os.path.basename(source_path)
            file, e = os.path.splitext(file)
            outfile = os.path.join(destination_path, file) + '.png'
            try:
                with Image.open(source_path) as im:
                    im.save(outfile)
            except OSError:
                print("Не получилось сконвертировать", file, 'в png')

class ImageConverterPngToJpg(AImageConverter):
        
    def convert(source_path, destination_path):
        if Checker.file_exists(source_path):
            file = os.path.basename(source_path)
            file, e = os.path.splitext(file)
            outfile = os.path.join(destination_path, file) + '.jpg'
            try:
                with Image.open(source_path) as im:
                    im.save(outfile)
            except OSError:
                print("Не получилось сконвертировать", file, 'в jpg')


class Checker():

    @abstractmethod
    def file_exists(path):
        return os.path.exists(path)