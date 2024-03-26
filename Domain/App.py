from Domain.Console import Console
from Domain.DataCSV import DataCSV
from Domain.LangRU import LangRU
from Domain.Note import Note


class App():
    
    def __init__(self):
        self.__console = Console(LangRU())
        self.__storage = DataCSV()
        self.__list_notes = self.__storage.read()
        
    def start(self):
        while True:
            self.__console.print_menu()
            status = self.__switch(self.__console.input_command())
            if status == 1: break
            
    def is_index(self, index):
        return (len(self.__list_notes) > 0) and (len(self.__list_notes) > index) and (index >= 0)
    
    def __read(self):
        self.__console.print_list(self.__list_notes)
        index = self.__console.input_index_read()
        if self.is_index(index):
            self.__console.print_note(self.__list_notes[index])
        else:
            self.__console.print_message_error_index()
            
    def __create(self):
        heading, body = self.__console.input_note()
        self.__list_notes.append(Note(heading, body))
        self.__storage.save(self.__list_notes)
        self.__console.print_successful_save()
        
    def __edit(self):
        self.__console.print_list(self.__list_notes)
        index = self.__console.input_index_edit()
        if self.is_index(index):
            self.__console.input_note_edit(self.__list_notes[index])
            self.__storage.save(self.__list_notes)
            self.__console.print_successful_save()
        else:
            self.__console.print_message_error_index()
            
    def __delete(self):
        self.__console.print_list(self.__list_notes)
        index = self.__console.input_index_delete()
        if self.is_index(index):        
            note = self.__list_notes.pop(index)
            self.__storage.save(self.__list_notes)
            self.__console.print_successful_delete(note.get_heading())
        else:
            self.__console.print_message_error_index()
            
    def __switch(self, command):
        if command == 'read':
            self.__read()
        elif command == 'create':
            self.__create()
        elif command == 'edit':
            self.__edit()
        elif command == 'delete':
            self.__delete()
        elif command == 'list':
            self.__console.print_list_sort(self.__list_notes)
        elif command == 'q':
            self.__console.print_message_exit()
            return 1
        else:
            self.__console.print_message_error_command()
        return 0