import reprlib
print(reprlib.repr(set('supercalifragilisticexpialidocious')))

# Output formatting

import pprint
t = [[[['black', 'cyan'], 'white', ['green', 'red']], [['magenta', 'yellow'], 'blue']]]
pprint.pprint(t, width=30)

import textwrap
doc = """The wrap() method is just like fill() except that it returns
         a list of strings instead of one big string with newlines to separate
         the wrapped lines."""

print(textwrap.fill(doc, width=40))

import locale
locale.setlocale(locale.LC_ALL, 'English_United States.1252')
conv = locale.localeconv()          # get a mapping of conventions
x = 1234567.8
print(locale.format("%d", x, grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                    conv['frac_digits'], x), grouping=True))

# Templating 
					
from string import Template
t = Template('${village}folk send $$10 to $cause.')
print(t.substitute(village='Nottingham', cause='the ditch fund'))

t = Template('Return the $item to $owner.')
d = dict(item='unladen swallow')
# t.substitute(d)           # causes KeyError
print(t.safe_substitute(d)) # safe_substitute may be more appropriate

import time, os.path
photofiles = ['img_1074.jpg', 'img_1076.jpg', 'img_1077.jpg']

class BatchRename(Template):
    delimiter = '%'

fmt = 'timonisula_%n%f' # input('Enter rename style (%d-date %n-seqnum %f-format):  ')
t = BatchRename(fmt)
date = time.strftime('%d%b%y')
for i, filename in enumerate(photofiles):
    base, ext = os.path.splitext(filename)
    newname = t.substitute(d=date, n=i, f=ext)
    print('{0} --> {1}'.format(filename, newname))


# Working with binary data record layouts
# Pack codes "H" and "I" represent two and four byte unsigned numbers respectively. 
# The "<" indicates that they are standard size and in little-endian byte order:
import os, struct

with open('my_zip.zip', 'rb') as f:
    data = f.read()

start = 0
for i in range(2): # show the first 2 file headers
    start += 14
    fields = struct.unpack('<IIIHH', data[start:start+16])
    crc32, comp_size, uncomp_size, filenamesize, extra_size = fields

    start += 16
    filename = data[start:start+filenamesize]
    start += filenamesize
    extra = data[start:start+extra_size]
    print(filename, hex(crc32), comp_size, uncomp_size)

    start += extra_size + comp_size  # skip to the next header	

