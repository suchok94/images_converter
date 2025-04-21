class App():

    def __init__(self, converter_creator):
        self.__converter_creator = converter_creator


    def convert(self, source_path, destination_path):
        self.__converter_creator.create_converter(source_path, destination_path)