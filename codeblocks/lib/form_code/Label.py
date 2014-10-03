class Label:

   def __init__(self, text, _for):
      self.text = text
      self._for = _for
   
   def print_code(self):
      print '<label for="' + self._for + '">' + self.text + '</label>'