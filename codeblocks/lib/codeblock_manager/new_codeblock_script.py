#!/usr/bin/python

import cgitb
import os
import sys

cgitb.enable()

path_string = os.path.abspath(__file__).split('/')
document_root =  '/' + path_string[1] + '/' + path_string[2] + '/'

sys.path.append(document_root)

from Globals_Setup import *
#####################################################################

form = cgi.FieldStorage()
codeblock_name = form['codeblock_name']
file_html = form['codeblock_html']
file_css_str = form['codeblock_css_str']
file_css_des = form['codeblock_css_des']

if file_html.filename:
   fn1 = os.path.basename(file_html.filename)
   open(codeblocks_html_root + fn1, 'wb').write(file_html.file.read())
   
   fn2 = os.path.basename(file_css_str.filename)
   open(codeblocks_css_root + fn2, 'wb').write(file_css_str.file.read())
   
   fn3 = os.path.basename(file_css_des.filename)
   open(codeblocks_css_root + fn3, 'wb').write(file_css_des.file.read())
   
   dbconn.query("INSERT INTO CodeBlocks VALUES(NULL,'" + codeblock_name.value + "','" + codeblocks_html_root + fn1 + "','" + codeblocks_css_path + fn2 + "','" + codeblocks_css_path + fn3  + "')")
   
else:
   print 'No files were uploaded'