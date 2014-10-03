class Combobox:

   def __init__(self, name):
      self.name = name
      self.options = []
      
   def add_options(self, options):
      self.options = options
   
   def print_code(self):
      print '<select name="' + self.name + '">'
      
      for option in self.options:
         print '<option value="' + option[0]['id'] + '">' + option[0]['name'] + '</option>'
      
      print '</select>'