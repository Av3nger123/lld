# Important implement to learn 

class Car:
    
    _brand:str = ""
    _model:str = ""
    _variant:str = ""
    _fuel_type:str = ""
    _number:str = ""
    
    def __init__(self):
        pass

    def brand(self,brand:str):
        self._brand = brand
        return self
        
    def model(self,model:str):
        self._model = model
        return self
        
    def variant(self,variant:str):
        self._variant = variant
        return self
        
    def fuel_type(self,fuel_type:str):
        self._fuel_type = fuel_type
        return self
        
    def number(self,number:str):
        self._number = number
        return self
        
    def __str__(self):
        return f"Car[{self._number}](brand={self._brand},model={self._model},variant={self._variant},fuel_type={self._fuel_type})"
    
if __name__ == "__main__":
    
    # Dynamically assign values for the object as needed
    car = Car()
    car.brand("Mercedes Benz").model("GLE").variant("220d")
    
    car = Car()
    car.brand("Maruti Suzuki").model("Breza").variant("xli").fuel_type("petrol").number("MH12MH1212")
    print(car)