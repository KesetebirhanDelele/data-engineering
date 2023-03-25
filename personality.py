{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "from datetime import datetime as dt, date\n",
    "from dateutil.relativedelta import relativedelta\n",
    "\n",
    "class Person:\n",
    "    def __init__(self, date_of_birth, my_name):\n",
    "        # __init__ function to fill properties and use self\n",
    "        # your birth date input yyyy-mm-dd\n",
    "        self.__date_of_birth = dt.strptime(date_of_birth, '%Y-%m-%d')\n",
    "        self.__my_name = my_name\n",
    "        self.__my_details_years = relativedelta(\n",
    "            date.today(), self.__date_of_birth).years\n",
    "        self.__names=self.__my_name.split(' ')\n",
    "    # create print function: last name\n",
    "    def last_name(self):\n",
    "        return f\"Last name: {self.__names[0]}.\"\n",
    "    \n",
    "    # create print function: first name\n",
    "    def first_name(self):\n",
    "       return f\"First name: {self.__names[1]}.\"\n",
    "    \n",
    "    def age(self):\n",
    "        return f\"{self.__my_name}, you are so young, only {self.__my_details_years} years old!\""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  },
  "orig_nbformat": 4
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
