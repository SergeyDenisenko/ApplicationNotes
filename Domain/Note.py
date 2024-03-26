import datetime


class Note():
    
    def __init__(self, heading = '', body = ''):
        self.__set_current_time()
        today = datetime.datetime.today()
        self.__id = today.strftime("%Y%m%d%H%M%S")
        self.__heading = heading
        self.__body = body
        
    def __set_current_time(self):
        today = datetime.datetime.today()
        self.__date = today.strftime("%d/%m/%Y %H:%M:%S")
        
    def set_heading(self, text):
        self.__heading = text
        self.__set_current_time()
        
    def set_body(self, text):
        self.__body = text
        self.__set_current_time()
        
    def get_id(self):
        return self.__id
    
    def get_heading(self):
        return self.__heading
    
    def get_body(self):
        return self.__body
    
    def get_date(self):
        return self.__date
        
    def get(self):
        return {'id':self.__id, 'date':self.__date, 'heading':self.__heading, 'body':self.__body}
    
    def recover(self, data):
        self.set_heading(data['heading'])
        self.set_body(data['body'])
        self.__id = data['id']
        self.__date = data['date']