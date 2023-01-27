from random import choices
import string
import numpy as np
import string
from copy import copy

class Password:

    input_universe = {'numbers': list(range(10)),
                      'letters': list(string.ascii_letters),
                      'punctuation': list(string.punctuation)}

    default_lenght = {'low':8,
                      'mid':12,
                      'high':16}

    def __init__(self,strength: str = 'mid', lenght:int = None) -> str:
        self.strength = strength
        self.lenght = lenght
        self._password_gen()

    @classmethod
    def show_input_universe(cls):
        """Return the complete universe from which characters are sampled

        :return: The universe of characters from which random sampling is done"""
        return cls.input_universe


    def _password_gen(self):

        population = copy(self.input_universe['letters'])
        length = self.lenght or self.default_lenght.get(self.strength)

        if self.strength == 'high':
            population += self.input_universe['numbers'] + self.input_universe['punctuation']
        else:
            population += self.input_universe['letters']


        self.password = "".join(list(map(str, choices(population, k =length)    )))

if __name__ == '__main__' :

    low_pass = Password(strength='low')
    print('low password is ', low_pass.password)
    password = Password()
    print('default password is ', password.password)

    strong_pass = Password(strength='high')
    print('strong password is ', strong_pass.password)

    password = Password()
    print('default2 password is ', password.password)

