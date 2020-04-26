import os
import sys


class NewDirectory():
    """docstring for ."""

    def __init__(self):
        self.name=''
        self.permision=''
    def add_new_dir_plus_permision(self):
        while True:
            self.name=raw_input('Add new directory name:')
            print('New name for direcotry is '+self.name)
            self.permision=raw_input('Add new permisions for directory '+self.name+':')
            os.system('mkdir'+' '+self.name+';'+' '+'chmod'+' '+self.permision+' '+self.name+';'+' '+'ls -l'+' '+self.name)
            break


new_dir=NewDirectory()
new_dir.add_new_dir_plus_permision()
