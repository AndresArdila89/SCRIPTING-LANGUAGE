class Circle:
    import math
    pi = math.pi
    idSequence = 1000

    def __init__(self,radius,color):
        
        self.circleId = 'CIR_' + str(Circle.idSequence)
        self.radius = radius
        self.color = color
        self.perimeter = 2*Circle.pi*radius
        self.area = Circle.pi*(radius**2)
        Circle.idSequence += 1
    
    @property
    def getCircleId(self):
        return self.circleId
    
    @property
    def getRadius(self):
        return self.radius

    @property
    def getColor(self):
        return self.color

    @getRadius.setter
    def setRadius(self, newRadius):
        if newRadius < 0:
            self.radius = 1
        else:
            self.radius = newRadius

    
    def __str__(self):
        return f"Circle Id: {self.circleId}, Color: {self.color}, Perimeter: {self.perimeter}, Area: {self.area}"
