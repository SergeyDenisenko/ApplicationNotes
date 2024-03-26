class LangRU():
    __commands = {
        'read':'Читать заметку',
        'create':'Создать заметку',
        'edit':'Редактировать заметку',
        'delete':'Удалить заметку',
        'list':'Список заметок',
        'q':'Выход'}
    
    def get_commands(self):
        return self.__commands
            
    def message_enter_command(self):
        return "Введите команду: "
    
    def message_enter_heading(self):
        return "Введите заголовок: "
    
    def message_enter_body(self):
        return "Введите текст заметки: "
    
    def message_enter_index_read(self):
        return "Для чтения заметки, введите ее индекс: "
    
    def message_enter_index_edit(self):
        return "Для редактирования заметки, введите ее индекс: "
    
    def message_enter_index_delete(self):
        return "Для удаления заметки, введите ее индекс: "
    
    def message_enter_new_heading(self):
        return "Введите новый заголовок: "
    
    def message_enter_new_body(self):
        return "Введите новый текст заметки: "
    
    def message_successful_save(self):
        return "Заметка успешно сохранена"
    
    def message_successful_delete(self, name):
        return "Заметка {} успешно удалена.".format(name)
    
    def message_exit(self):
        return "Выход"
    
    def message_error_command(self):
        return "Ошибка ввода команды. Пожалуйста, повторите ввод."
    
    def message_error_index(self):
        return "Ошибка ввода индекса."
    
    def message_continue(self):
        return "Для продолжения нажмите 'enter'"
    
    def heading(self):
        return "Заголовок: "
    
    def body(self):
        return "Текст:"