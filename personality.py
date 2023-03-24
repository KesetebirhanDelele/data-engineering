from datetime import datetime as dt, date
from dateutil.relativedelta import relativedelta

class Person:
    def __init__(self, date_of_birth, my_name):
        # __init__ function to fill properties and use self
        # your birth date input yyyy-mm-dd
        self.__date_of_birth = dt.strptime(date_of_birth, '%Y-%m-%d')
        self.__my_name = my_name
        self.__my_details_years = relativedelta(
            date.today(), self.__date_of_birth).years
        self.__names=self.__my_name.split(' ')
    # create print function: last name
    def last_name(self):
        return f"Last name: {self.__names[0]}."
    
    # create print function: first name
    def first_name(self):
       return f"First name: {self.__names[1]}."
    
    def age(self):
        return f"{self.__my_name}, you are so young, only {self.__my_details_years} years old!"
