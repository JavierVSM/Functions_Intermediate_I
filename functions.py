
print ( "======= Task 1 =======")
# 1. Update Values in Dictionaries and Lists

x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# A-Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
def changeNum (num):
  y=x[1]
  y[0] = 15
  print (x)

changeNum (x)

# B-Change the last_name of the first student from 'Jordan' to 'Bryant'

def changeLastName (num):
  dic1= students[0]
  dic2= students[1]
  dic1 ["last_name"]="Bryant"
  print (dic1)

changeLastName (students)

# C-In the sports_directory, change 'Messi' to 'Andres'
def changeSoccer (num):
  sports_directory ["soccer"][0]= "Andres"
  print (sports_directory)

changeSoccer (sports_directory)

# D-Change the value 20 in z to 30
def changeZ (num):
  dicZ= z[0]
  dicZ ["y"]=30
  print (z)

changeZ (z)


print ( "======= Task 2 =======")
# 2. Iterate Through a List of Dictionaries

#Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary (some_list):
  i=0
  while i < len(some_list):
    for key,val in some_list[i].items():
      print(key + " - "+ val+",")
    i += 1

iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

print ( "======= Task 3 =======")
# 3.Get Values From a List of Dictionaries
#Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

def iterateDictionary2(key_name, some_list):
  i=0
  while i < len(some_list):
    print (some_list[i] [key_name])
    i += 1

iterateDictionary2('first_name', students)

print ( "======= Task 4 =======")
# 4- Iterate Through a Dictionary with List Values
# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
  for key, val in some_dict.items():
    print(len(key), key)
    i=0
    while i<len(val):
       print (val[i])
       i += 1  
    
printInfo(dojo)