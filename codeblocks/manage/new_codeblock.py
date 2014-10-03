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

form = NewCodeBlockForm('frmNewCodeBlock', '/codeblocks/lib/codeblock_manager/new_codeblock_script.py', 'POST')
form.print_code()