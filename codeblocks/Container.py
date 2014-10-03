class Container:

   def __init__(self):
      self.width = 100	
      self.height = 100
      self.backgroundColor = 'black'
      self.children = []
      
      
   #setters 
   def set_backgroundColor(self, backgroundColor):
      self.backgroundColor = backgroundColor
      
  
   def set_dimensions(self, width, height):
      self.width = width
      self.height = height
      

   #printers
   def print_css_links(self):
      for child in self.children:
         child.print_css_links()
   
   def print_code(self):
      print '<div id="' + self.id + '" style="background-color:' + str(self.backgroundColor) + ';width:'+str(self.width) + 'px;height:' +   str(self.height) + 'px">'
      
      for child in self.children:
         child.print_code()
            
      print '</div>'