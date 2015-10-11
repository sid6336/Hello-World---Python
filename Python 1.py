# Copying text from one file to another
# $python script.py from_file.txt to_file.txt

from sys import argv
from os.path import exist

script, from_file, to_file = argv
print "copying from %r to %r" % (from_file, to_file)

in_file = open (from_file)
in_data = in_file.read ()

print "data is %d bytes long" % len(in_data)
print "Does the Out_file exist? %r" % exist(to_file)
print "Last check before Write."
raw_input()

out_file = open (to_file, 'w')
out_file.write(in_data)

print "All done."

in_file.close()
out_file.close()
