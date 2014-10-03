from Combobox import *
from LabelCombobox import *
from LabelFilebox import *
from LabelTextbox import *

class Form:
   
   def __init__(self, name, action, method):
      self.name = name
      self.action = action
      self.method = method
      self.input_list = []
      
   def add_input(self, input):
      self.input_list.append(input)
     
   def print_code(self):
      print '<form name="' + self.name + '" enctype="multipart/form-data" action="' + self.action + '" method="' + self.method + '">'
      
      for input in self.input_list:
         input.print_code()
         
      print '<input type="submit" value="send"/>'
      print '</form>'
      
   
