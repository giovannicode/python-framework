class CodeBlock:
   
   #default variables
   backgroundColor = 'white'

   def __init__(self, id, dbconn):
      self.id = id
      self.children = []
      self.html = ''     
      self.has_css_structure = False
      self.has_css_design = False
      self.css_strucure_link = ''
      self.css_design_link = ''
      
      self.set_db_variables(dbconn)
      self.setup()
      

   def add_child(self, codeBlock):
      self.children.append(codeBlock)
      
      
   #getters  
   def get_css_structure_link(self):   
      self.has_css_structure = True
      return '<link rel="stylesheet" type="text/css" href="' + self.db_variables[0]['str_css_path'] + '"/>'
      
      
   def get_css_design_link(self):
      self.has_css_design = True
      return '<link rel="stylesheet" type="text/css" href="' + self.db_variables[0]['des_css_path'] + '"/>'
      
      
   def get_html(self):
      try:
         html_path = self.db_variables[0]['html_path']
         fileHandle = open ( html_path, 'r' )
	 self.html = fileHandle.read()
	 fileHandle.close()
      except:
         pass
      finally:
         return self.html
   
   
   #setters
   def set_db_variables(self, dbconn):
      dbconn.query("SELECT * FROM CodeBlocks WHERE id = " + self.id)
      result = dbconn.store_result()
      self.db_variables = result.fetch_row(1,1)     
         
                    
   def setup(self):
      self.html = self.get_html()
      self.css_structure_link = self.get_css_structure_link()
      self.css_design_link = self.get_css_design_link()
      
   
   #printers 
   def print_css_links(self):
      if self.has_css_structure:
         print self.css_structure_link
      if self.has_css_design:
         print self.css_design_link

             
   def print_code(self):
      print self.html   