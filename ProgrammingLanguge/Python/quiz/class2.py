class Calc():
    def __init__(self):
        self.num1 = '-'
        self.num2 = '-'
        
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        
    def plus(self):
        
        return self.num1 + self.num2
        
    def minus(self):
        
        return self.num1 - self.num2
        
    def multiple(self):
                
        return self.num1 * self.num2
    
    def divide(self):
    
        return self.num1 // self.num2
    
calc = Calc()
calc.set_number(20, 10)
print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())