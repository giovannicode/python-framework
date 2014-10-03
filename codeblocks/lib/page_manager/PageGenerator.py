import sys
sys.path.append('../../')

from ParentBlock import *
from CodeBlock import *

class PageGenerator:

   def __init__(self, page_ID, dbconn):
      self.page_ID = page_ID
      self.parentBlock = ParentBlock()
      self.add_codeBlocks(dbconn)
      
   def add_codeBlocks(self,dbconn):
      dbconn.query("SELECT codeblock_ID FROM Page_Components WHERE page_ID=" + self.page_ID)
      result = dbconn.store_result()
      answers = result.fetch_row(0,1)
      
      for answer in answers:   
         self.parentBlock.add_child(CodeBlock(answer['codeblock_ID'], dbconn))

         
   def print_code(self):
      self.parentBlock.print_code()
      
   
   
     
   