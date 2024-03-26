class Console():
    def __init__(self, view, delimeter='-', length=40):
        self.__view = view
        self.__delimeter = delimeter
        self.__length = length
        
    def print_menu(self):
        commands = self.__view.get_commands()
        print(self.__delimeter*self.__length)
        for command, text in commands.items():
            print("{:<30}".format(text), "\t: ", command)
        print()
              
    def print_note(self, note):
        print(self.__delimeter*self.__length)
        print(self.__view.heading(), note.get_heading())
        print()
        print(self.__view.body())
        print(note.get_body())
        print(self.__delimeter*self.__length)
        input(self.__view.message_continue())
        
    def print_successful_save(self):
        print(self.__delimeter*self.__length)
        print(self.__view.message_successful_save())
        
    def print_successful_delete(self, name):
        print(self.__delimeter*self.__length)
        print(self.__view.message_successful_delete(name))
        
    def print_message_exit(self):
        print(self.__delimeter*self.__length)
        print(self.__view.message_exit())
        
    def print_message_error_command(self):
        print(self.__delimeter*self.__length)
        print(self.__view.message_error_command())
        
    def print_message_error_index(self):
        print(self.__delimeter*self.__length)
        print(self.__view.message_error_index())
        
    def print_list(self, notes):
        print(self.__delimeter*self.__length)
        for index, note in enumerate(notes):
            print(index, note.get_heading(), note.get_date())
            
    def print_list_sort(self, notes):
        print(self.__delimeter*self.__length)
        tmp = dict()
        for note in notes:
            tmp[note.get_date()] = note
        tmp = dict(sorted(tmp.items()))
        self.print_list(tmp.values())
        print(self.__delimeter*self.__length)
        input(self.__view.message_continue())
        
    def input_command(self):
        return input(self.__view.message_enter_command())
    
    def input_note(self):
        heading = input(self.__view.message_enter_heading())
        body = input(self.__view.message_enter_body())
        return heading, body
    
    def input_index_read(self):
        try:
            return int(input(self.__view.message_enter_index_read()))
        except:
            return -1
    
    def input_index_edit(self):
        try:
            return int(input(self.__view.message_enter_index_edit()))
        except:
            return -1
    
    def input_index_delete(self):
        try:
            return int(input(self.__view.message_enter_index_delete()))
        except:
            return -1
    
    def input_note_edit(self, note):
        print(note.get_heading())
        heading = input(self.__view.message_enter_new_heading())
        if len(heading) > 0:
            note.set_heading(heading)
        print(note.get_body())
        body = input(self.__view.message_enter_new_body())
        if len(body) > 0:
            note.set_body(body)