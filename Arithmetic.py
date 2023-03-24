# Note that module file name should be small case and class name should be named Capitalized
# Or else module file name can be capital but written in small case when imported
class Arithmetic:
    def __init__(self,num1,num2):
        self.__num1 = num1
        self.__num2 = num2
        
    def addition(self):
        return self.__num1+self.__num2
    
    def subtraction(self):
        return self.__num1-self.__num2
    
    def division(self):
        return self.__num1/self.__num2
    
    def product(self):
        return self.__num1*self.__num2