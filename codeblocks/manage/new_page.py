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

new_theme_form = Form('new_theme_form', '/codeblocks/lib/page_manager/new_page_script.py', 'post')

dbconn.query("SELECT id, name FROM CodeBlocks")
result = dbconn.store_result()
list = []
result_tuple = result.fetch_row(1,1)

while str(result_tuple) != '()':
   list.append(result_tuple)
   result_tuple = result.fetch_row(1,1)

txt1 = LabelTextbox('page_name', 'Enter the name of the page:')
txt2 = LabelTextbox('page_path', 'Enter the locaation of the file')
cb1 = LabelCombobox('block_selector', 'Choose a Code Block to add')

cb1.add_options(list)

new_theme_form.add_input(txt1)
new_theme_form.add_input(txt2)
new_theme_form.add_input(cb1)


new_theme_form.print_code()