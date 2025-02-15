from abc import abstractmethod


class DataSource:
    
    @abstractmethod
    def write(self,input):
        raise NotImplementedError
    
    @abstractmethod
    def read(self):
        raise NotImplementedError

class FileDataSource(DataSource):
    def __init__(self,filename):
        self.filename = filename
        self.file = ""
    
    def write(self,input):
        self.file += input

    def read(self):
        return self.file
    
class EncryptionDecorator(DataSource):
    
    def __init__(self,data_source: DataSource):
        self.data_source = data_source
        self.delimiter = "#"
    
    def write(self,input):
        self.data_source.write(self.encrypt(input))

    def read(self):
        return self.data_source.read()
    
    def encrypt(self,input):
        return f"{self.delimiter}{input}"
    
class CompressionDecorator(DataSource):
    
    def __init__(self,data_source: DataSource):
        self.data_source = data_source
        self.delimiter = "|"
    
    def write(self,input):
        self.data_source.write(self.compress(input))

    def read(self):
        return self.data_source.read()
    
    def compress(self,input):
        return f"{self.delimiter}{input}"
    
    
if __name__ == "__main__":
    
    file_data_source = FileDataSource("sample.txt")
    file_data_source.write("Sample\n")
    file_data_source.write("Sample\n")
    file_data_source.write("Sample")
    print(file_data_source.read())
    
    file_data_source = FileDataSource("sample.txt")
    encrypt_decorator = EncryptionDecorator(file_data_source)
    encrypt_decorator.write("Sample\n")
    encrypt_decorator.write("Sample\n")
    encrypt_decorator.write("Sample")
    print(encrypt_decorator.read())
    
    file_data_source = FileDataSource("sample.txt")
    compression_decorator = CompressionDecorator(file_data_source)
    compression_decorator.write("Sample\n")
    compression_decorator.write("Sample\n")
    compression_decorator.write("Sample")
    print(compression_decorator.read())
    
    