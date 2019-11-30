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


# The high level threading module can run tasks in background 
# while the main program continues to run	
import threading, zipfile

class AsyncZip(threading.Thread):
    def __init__(self, infiles, outfile, extension):
        threading.Thread.__init__(self)
        self.infiles = infiles
        self.outfile = outfile
        self.extension = extension

    def run(self):
        zf = zipfile.ZipFile("%s" % (self.outfile), "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(self.infiles)
        print("abs_src : " + abs_src)
        for dirname, subdirs, files in os.walk(self.infiles):
            for filename in files:
                if filename.endswith(self.extension):
                    absname = os.path.abspath(os.path.join(dirname, filename))
                    arcname = absname[len(abs_src) + 1:]
                    print('zipping %s as %s' % (os.path.join(dirname, filename), arcname))
                    # zf.write(absname, arcname)
                    zf.write(os.path.join(dirname, filename), arcname=filename)
        zf.close()        

		
background = AsyncZip("c:\\pythonoulu\\today", "archive.zip", ".py")
background.start()
print('The main program continues to run in foreground.')

background.join()    # Wait for the background task to finish
print('Main program waited until background was done.')


# Logging
import logging
logging.debug('Debugging information')
logging.info('Informational message')
logging.warning('Warning:config file %s not found', 'server.conf')
logging.error('Error occurred')
logging.critical('Critical error -- shutting down')


# Decimal Floating Point Arithmetic
from decimal import *
x = Decimal('0.70') * Decimal('1.05')
print(x)
print(x.quantize(Decimal('0.01')))  # round to nearest cent
print(round(.70 * 1.05, 2))         # same calculation with floats
print(Decimal('1.00') % Decimal('.10'))
print(1.00 % 0.10)
print(sum([Decimal('0.1')]*10) == Decimal('1.0'))
print(sum([0.1]*10) == 1.0)
getcontext().prec = 15
print(Decimal(1) / Decimal(7))