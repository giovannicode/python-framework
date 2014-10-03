class ParentBlock:
  
   def __init__(self):
      self.children = []
      
   
   def add_child(self, codeBlock):
      self.children.append(codeBlock)    
      
               
   def print_code(self):
      print '<!DOCTYPE HTML>'
      print '<html>'     
      
      print '<head>'
      print '<meta charset="utf-8" />'
      print '<title>CoderWarehouse</title>'
      print '<link rel="stylesheet" type="text/css" href="/codeblocks/code_files/css/main.css"/>' 
      for child in self.children: 
         child.print_css_links() 
      print '<script type="text/javascript" src="/codeblocks/code_files/js/jquery-2.1.1.js"></script>' 
      print '<script type="text/javascript" src="/codeblocks/code_files/js/test.js"></script>'    
      print '</head>'
      
      print '<body>'      
      for child in self.children:
         child.print_code() 
      self.test_method()   
      print '</body>'      
     
      print '</html>'
      
   def test_method(self):
      print '<script>'
      print "if (typeof jQuery != 'undefined')"
      print '{alert("jQuery library is loaded!");}else{'
      print 'alert("jQuery library is not found!");'
      print '}'
      print '</script>'
      
      


         
