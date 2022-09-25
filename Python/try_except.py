class Calc():    
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
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print('0으로 나눌 수 없습니다.')
            
try:
    calc = Calc()
    calc.set_number()
except ValueError:
    print('숫자만 입력 가능합니다.')

print(calc.plus())
print(calc.minus())
print(calc.multiple())
print(calc.divide())