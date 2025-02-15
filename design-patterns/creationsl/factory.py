# Important implement to learn 

class BaseObject:
    
    def some_operation(self):
        return "BaseObject"

# Base creator class
class BaseCreatorClass:
    
    def create_object(self) -> BaseObject:
        return BaseObject()
    
    def some_operation(self):
        obj = self.create_object()
        return obj.some_operation()

class ChildObject1(BaseObject):
    
    def some_operation(self):
        return "ChildObject1"
    
class ChildObject2(BaseObject):
    
    def some_operation(self):
        return "ChildObject2"
        
    
class ChildCreatorClass1(BaseCreatorClass):
    
    def create_object(self):
        return ChildObject1()
    
class ChildCreatorClass2(BaseCreatorClass):
    
    def create_object(self):
        return ChildObject2()
    
if __name__ == "__main__":
    
    obj1 = ChildCreatorClass1().some_operation()
    obj2 = ChildCreatorClass2().some_operation()
    print(obj1,obj2) # ChildObject1 ChildObject2