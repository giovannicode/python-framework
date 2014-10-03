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

form = cgi.FieldStorage()
codeblock = form['block_selector']
page_name = form['page_name']
page_path = form['page_path']

dbconn.query("INSERT INTO Pages (name, path) VALUES('" + page_name.value + "', '" + page_path.value + "')")

new_page = open(website_root + 'pages/' + page_name.value + '.py', 'a')
os.chmod(new_page.name, 0755)
minimum_python = open(setup_page, 'r')

#new line character is so that (page_id = codeblock.value) starts on a new line
new_page.write(minimum_python.read() + '\n\n')

dbconn.query("SELECT ID FROM Pages WHERE path='" + page_path.value + "'")
result = dbconn.store_result()
answer = result.fetch_row(1,1)
new_page.write("page_ID = '" + str(answer[0]['ID']) + "'")

dbconn.query("INSERT INTO Page_Components (page_ID, codeblock_ID) VALUES(" + answer[0]['ID'] + "," + codeblock.value + ")")

new_page.write('\npageGenerator = PageGenerator(page_ID, dbconn)')
new_page.write('\npageGenerator.print_code()')