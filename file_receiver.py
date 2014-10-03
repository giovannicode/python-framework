#!/usr/bin/env python
import cgi, os
import cgitb; cgitb.enable()

try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()

# A nested FieldStorage instance holds the file
file_html = form['html_file']
file_css_str = form['css_str_file']
file_css_sty = form['css_sty_file']

# Test if the file was uploaded
if file_html.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(file_html.filename)
   open('Code_Files/html/' + fn, 'wb').write(file_html.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No html file was uploaded'
   
if file_css_str.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(file_css_str.filename)
   open('Code_Files/css/' + fn, 'wb').write(file_css_str.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No css structure file was uploaded'
   
if file_css_sty.filename:
   
   # strip leading path from file name to avoid directory traversal attacks
   fn = os.path.basename(file_css_sty.filename)
   open('Code_Files/css/' + fn, 'wb').write(file_css_sty.file.read())
   message = 'The file "' + fn + '" was uploaded successfully'
   
else:
   message = 'No css style file was uploaded'
   
print """\
Content-Type: text/html\n
<html><body>
<p>%s</p>
</body></html>
""" % (message,)