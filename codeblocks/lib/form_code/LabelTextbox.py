class LabelTextbox:

   def __init__(self, name, label):
      self._class = 'unimplemented'
      self.name = name
      self.label = label
   
   def print_code(self):
      print '<div class="unimplemented"><label for="' + self.name + '">' + self.label + '</label><input type="text" name="' + self.name + '"/></div>'