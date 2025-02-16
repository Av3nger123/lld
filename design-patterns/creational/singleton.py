# Important implement to learn 

class Singleton:
    _instance = None
    def __new__(cls,*args,**kwargs):
        if not cls._instance:
            cls._instance = super(Singleton,cls).__new__(cls)
        return cls._instance
            
            
if __name__ == "__main__":
    obj1 = Singleton()
    obj2 = Singleton()
    
    print(obj1 is obj2)
    