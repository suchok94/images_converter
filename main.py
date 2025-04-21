from modules.converters_creator import ConverterCreatorJpgToPng, ConverterCreatorPngToJpg
from modules.converter import ImageConverterJpgToPng, ImageConverterPngToJpg
from abc import ABC, abstractmethod

class App():

    def __init__(self, converter_creator):
        self.__converter_creator = converter_creator


    def convert(self, source_path, destination_path):
        self.__converter_creator.create_converter(source_path, destination_path)

    # @classmethod
    # def run(cls):
    #     source_path = input('Введите путь до исходного файла: ')
    #     destination_path = input('Введите путь до конечного файла: ')

    #     image_type = source_path[-4:]

    #     if image_type == '.png':
    #         converterCreator = AConverterCreator(ImageConverterPngToJpg)
        
    #     elif image_type == '.jpg' or image_type == 'jpeg':
    #         converterCreator = AConverterCreator()
    #     converter = converterCreator.create_converter()
    #     converter.convert(source_path, destination_path)
    #     print('Всё получилось')

def main():
    app = App(ConverterCreatorJpgToPng())
    app.convert('123.jpg', '321.png')


if __name__ == '__main__':
    main()