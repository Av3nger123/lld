from abc import ABC, abstractmethod
from typing import Dict, List

class EventListener(ABC):
    
    @abstractmethod
    def execute(self,filename):
        raise NotImplementedError
        


class EventManager:
    def __init__(self):
        self.listeners_map: Dict[str,List[EventListener]] = {}
        
    def subscribe(self, event_type, listener):
        if event_type  not in self.listeners_map:
            self.listeners_map[event_type] = []
        self.listeners_map[event_type].append(listener)
        
    def unsubscribe(self,event_type,listener):
        if self.listeners_map[event_type]:
            self.listeners_map[event_type].remove(listener)
            
    def notify(self,event_type,data):
        for listener in self.listeners_map[event_type]:
            listener.execute(data)
        
class LoggingListener(EventListener):
    
    def __init__(self,filename,message):
        self.file = ""
        self.filename = filename
        self.message:str = message
        
    def execute(self, filename):
        print(self.message % (filename))
        
class EmailNotifierListener(EventListener):
    def __init__(self,email,message):
        self.email = email
        self.message = message
        
    def execute(self, filename):
        print(f"Sending email to {self.email} Message: {self.message % (filename)}")
        
if __name__ == "__main__":
    event_manager = EventManager()
    
    # Subscribe to "open" event so that we log
    logging_listener = LoggingListener("sample.log","Someone has opened the file: %s") 
    event_manager.subscribe("open",logging_listener)
    
    # Subscribe to "save" event so that we send email
    logging_listener = EmailNotifierListener("sample@gmail.com","Someone has changed the file: %s") 
    event_manager.subscribe("save",logging_listener)
    
    event_manager.notify("open","sample.log")
    event_manager.notify("save","sample.log")
    
    
