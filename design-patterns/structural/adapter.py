import math

class RoundPeg:
    def __init__(self,radius):
        self.radius = radius
        
    def get_radius(self):
        return self.radius

class RoundHole:
    def __init__(self,radius):
        self.radius = radius
        
    def fits(self,peg:RoundPeg):
        return self.radius >= peg.get_radius()
    
class SquarePeg:
    def __init__(self,side):
        self.side = side
        
    def get_side(self):
        return self.side

# This class acts as a adapter between SquarePeg and RoundPeg so that it can be used in RoundHole
class SquarePegAdapter(RoundPeg):
    def __init__(self, peg:SquarePeg):
        self.peg = peg
    
    def get_radius(self):
        return (self.peg.side * math.sqrt(2)) / 2
    
if __name__ == "__main__":
    hole = RoundHole(5)
    round_peg = RoundPeg(4)
    print(hole.fits(round_peg))
    
    square_peg = SquarePeg(10)
    # print(hole.fits(square_peg)) # Gives error AttributeError: 'SquarePeg' object has no attribute 'get_radius'
    
    square_peg_adapter = SquarePegAdapter(square_peg)
    print(hole.fits(square_peg_adapter))
        