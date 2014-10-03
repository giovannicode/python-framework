class LabelCombobox:

   def __init__(self, name, label):
      self.name = name
      self.id = name
      self.label = label
      self.options = []
      
   def add_options(self, options):
      self.options = options
      
   def print_code(self):
      print '<div class="unimplemented"><label for="' + self.name + '">' + self.label + '</label><select name="' + self.name + '" id="' + self.id + '">'
      
      for option in self.options:
         print '<option value="' + option[0]['id'] + '">' + option[0]['name'] + '</option>'
         
      print '</select></div>'