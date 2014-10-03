import sys
sys.path.append('../../form_code')

from Form import *

class NewCodeBlockForm(Form):

   def __init__(self, name, action, method):
      Form.__init__(self, name, action, method)
      self.add_input(LabelTextbox('codeblock_name', 'Codeblock Name: '))
      self.add_input(LabelFilebox('codeblock_html', 'HTML file: '))
      self.add_input(LabelFilebox('codeblock_css_str', 'CSS Structure File:'))
      self.add_input(LabelFilebox('codeblock_css_des', 'CSS Design File:'))
   
   