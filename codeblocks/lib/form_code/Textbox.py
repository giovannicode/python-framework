class Textbox:

   def __init__(self,id):
      self.id = id
      self.name = id
      
   def print_code(self):
      print '<input type="text" id="' + self.id + '" name="' + self.name + '"/>'
