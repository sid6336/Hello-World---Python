# 1. Copying text from one file to another
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

# 2. lists
mix_list = [1,'hello',2,'sid', True]

for item in mix_list:
  print "This is your item from Mix_List %r" % item  #%r for mixed lists, %d number, %s string

elements = []
for i in range (0,6):
  elements.append(i) # adding i into list
print elements

# 3. Adding to list
input1 = "Sugar Beer Meat"
pool = ['Salad','Steak','Icer-cream','Eggs']
stuff = input1.split()
while len(stuff) < 5:
  next_thing = pool.pop(0)
  stuff.append(next_thing)
  print "%s has been added, there are %d items in the list." % (next_thing, len(stuff))

print ' '.join(stuff)
print '#'.join(stuff[2:5])
