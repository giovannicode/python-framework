#!/usr/bin/python

import cgitb
import os
import sys

cgitb.enable()

path_string = os.path.abspath(__file__).split('/')
document_root =  '/' + path_string[1] + '/' + path_string[2] + '/'

sys.path.append(document_root)

from Globals_Setup import *
##################################################################

parentBlock = ParentBlock()
headerBlock = CodeBlock('header')
bodyBlock = CodeBlock('body')
horinavBlock = CodeBlock('horinav')
footerBlock = CodeBlock('footer')

parentBlock.set_dimensions(975, 1000)
bodyBlock.set_dimensions(975, 600)

parentBlock.set_is_container(True)
bodyBlock.set_is_container(True)

headerBlock.setup()
horinavBlock.setup()
footerBlock.setup()

bodyBlock.add_child(horinavBlock)
parentBlock.add_child(headerBlock)
parentBlock.add_child(bodyBlock)
parentBlock.add_child(footerBlock)

print "<!DOCTYPE HTML>"
print "<html>"
print "<head>"
print "<title>CoderWarehouse</title>"
print '<link rel="stylesheet" type="text/css" href="./CodeBlocks/Code_Files/css/main.css"/>'

parentBlock.get_css_links()

print "</head>"
print "<body>"

parentBlock.print_code()

form = Form('Form_codeblock_adder', 'file_receiver.py', 'post')
label_textbox = LabelTextbox('Name', 'name')
lfb_html = LabelFilebox('Label_FileBox', 'HTML File', 'html_file')
lfb_css_str = LabelFilebox('Label_FileBox', 'CSS Structure File', 'css_str_file')
lfb_css_sty = LabelFilebox('Label_FileBox', 'CSS Sty File', 'css_sty_file')
cb = Combobox('cb')
form.add_input(lfb_html)
form.add_input(lfb_css_str)
form.add_input(lfb_css_sty)
form.add_input(cb)
form.print_code()

print "</body>"
print "</html>"