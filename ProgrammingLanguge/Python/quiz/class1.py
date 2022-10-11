class Area():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def square(self):
        
        return self.width * self.height
        
    def triangle(self):
        
        return self.width * self.height // 2
        
    def circle(self):
                
        return self.width // 2 * 3.14

area = Area(10, 20)
print(area.square())
print(area.triangle())
print(area.circle())