import csv
import os

from Domain.Note import Note


class DataCSV():
    def __init__(self, file='data', delimeter=','):
        self.set_path(file)
        self.__delimeter = delimeter
        
    def set_path(self, path):
        self.__path = path+'.csv'
        
    def save(self, data):
        fieldnames = ['id', 'heading', 'body', 'date']
        with open(self.__path, 'w', encoding='utf-8') as f:
            file_writer = csv.DictWriter(f, fieldnames, delimiter=self.__delimeter, lineterminator="\r")
            file_writer.writeheader()
            for note in data:
                file_writer.writerow(note.get())
            
    def read(self):
        data = []
        if os.path.exists(self.__path):
            with open(self.__path, 'r', encoding='utf-8') as f:
                file_reader = csv.DictReader(f, delimiter=self.__delimeter)
                for index, row in enumerate(file_reader, 1):
                    note = Note()
                    note.recover(row)
                    data.append(note)
        return data