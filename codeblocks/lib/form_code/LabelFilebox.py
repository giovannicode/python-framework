class LabelFilebox:

   def __init__(self, name, label):
      self.name = name
      self.label = label
      
   def print_code(self):
      print '<div><label for="' + self.name + '">' + self.label + '</label><input type="file" name="' + self.name + '"/></div>'