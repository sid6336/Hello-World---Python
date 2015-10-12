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
  next_thing = pool.pop(0) #-1 would add the last item from the pool list
  stuff.append(next_thing)
  print "%s has been added, there are %d items in the list." % (next_thing, len(stuff))

print ' '.join(stuff)
print '$'.join(stuff[2:5]) #$ signs betwee 2-4

# 4. Class
class Song(object):
  def __init__ (self,lyrics):
    self.lyrics=lyrics
  def sing_me_a_song (self):
    for line in self.lyrics:
      print line 

Happy_Bday = Song (["Hello My friend",
                    "This is your B'day",
                    "I wish you all the best."])
Happy_Bday.sing_me_a_song()

#5. Class, Object, is-a, has-a

class Animal(object):
  pass

class Dog(Animal):
  def __init(self,name):
    self.name=name
class Cat(Animal):
  def __init(self,name):
    self.name=name

class Person(object):
  def __init(self,name):
    self.name=name
    self.pet=none

rex = Dog("Rex")
owen = Cat("Owen")
john = Person("John")
john.pet=owen

print john.pet.name

#6. Class inheritence, override, super class

class Parent(object):
  def implicit(self):
    print "Parent implicit"

class Child(Parent):
  def implicit(self):
    print "Child override before"
    super(Child,self).implicit()
    print "Child override after"

father = Parent()
son = Child()
son.implicit()

#7. List
import random
list_new = random.shuffle(list_old)

sorted (list1, key=lambda s:s[-1]) #sorted by last character of each element in list
sorted (list1, key=len)
sorted (list1, key=str.lower, reverse = True)

list_low = [x.lower() for x in list_orig] #comprehension

#8. Dict
dict1={}
dict1['Name'] = 'John'
dict1['Age'] = 18

print dict1.keys(), dict1.values(), dict1.items() #items=(key,value)

search_value='John' #search value='John' and print its key
if search_value in dict1.values():
  for first,second in dict1.items():
    if second==search_value:
      print first,second

for key in sorted(dict1): #sorted keys and their values
  print key,dict1[key]
  
print "%(Name)s came yesterday. He is %(Age)d years old." % dict1


  
