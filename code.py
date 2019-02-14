import math
import os
import datetime
import random

def hello(a_name):
  print("Hello! " + a_name)


def hello2(name_a,name_b):
  print("Hello! " + name_a +" and " + name_b)


def sum_two(x,y):
  Z = x + y 
  return z 

def circle_area(radius):
   a = math.pi * radius ** 2
   return a

def today():
    now = datetime.datetime.now()
    return now.day 


def my_sum(a_list):
  total = 0
  for n in a_list:
    total = total + n
  return total 


def my_prod(a_list):
  total = 1 
  for n in a_list:
    total = total * n 
  return total 


def my_count(a_list):
  total = 0
  for n in a_list:
    total = 1 + total 
  return total

def my_count_less_5(a_list):
  count = 0
  for n in a_list:
    if n < 5:
      count = count + 1
  return count 

def count_ones(a_list):
  count = 0
  for n in a_list:
    if n == 1:
      count = count + 1
  return count 

def is_list_empty(a_list):
  if my_count(a_list) == 0:
    return True
  else:
    return False 

def my_max(a_list):
  if is_list_empty(a_list):
    return None
  else:
    count = a_list[0]
    for n in a_list:
      if n > count: 
        count = n
    return count 

# get_filenames("C:\\Users\\Desktop")
# --> list of filen names 
# ['"C:\\Users\\Desktop\\code.py', '"C:\\Users\\Desktop\\imageprocessor.py', 'loops.py', 'start.py']


def get_filenames(a_dirname):
  list_of_files = os.listdir(a_dirname)
  print("list of file name")
  print(list_of_files)
  print("-----------")
  all_files = []
  for filename in list_of_files:
    full_path = os.path.join(a_dirname,filename)
    if not os.path.isdir(full_path):
      all_files.append(full_path)
  return all_files



# [12,34, [56,67],78] -> [12,34,56,67]

def flatten(a_list_with_lists):
  new_list = []
  for n in a_list_with_lists:
    if isinstance(n,list):
      for i in n:
        new_list.append(i)
    else:
      new_list.append(n)
  return new_list

#  [12,34, [56,67],78] -> # hint: use print(..,end='')
#  12
#  34
#  5667
#  78

a_list_with_lists = [12,34, [56,67], 78]

def print_right(a_list_with_lists):
  for i in a_list_with_lists:
    string = ""
    if isinstance(i,list):
      for n in i:
        string = string + str(n)
      if n == i[-1]:
        print(string)
    else:
      print(i)

print_right(a_list_with_lists)


#  single_row_stars(4) -> ****
#  single_row_stars(6) -> ********

def single_row_stars(number):
  for i in range(number):
    print('*',end='')

single_row_stars(4)
print('')
single_row_stars(6)
  

def single_row_stars(number):
  for i in range(number):
    print('***',end='-')

single_row_stars(4)
print('')
single_row_stars(6)


#  single_row_of(4,"*") -> ****
#  single_row_of(3,"-+") -> -+-+-+

def single_row_of(number,string):
  for i in range(number):
    print(string,end="")
  print("")

print('')
single_row_of(4,"*")
print('')
single_row_of(3,"-+")


# square_of_stars(4)
# ->
# ****
# ****
# ****
# ****

def square_of_stars(number):
  for i in range(number):
    for j in range(number):
      print('*',end='')
    print('*')
  

#  list_by_2([1,2,3]) -> [2,4,6]

def list_by_2(list_with_n_list):
  n_list = []
  for n in list_with_n_list:
    n_list.append(n * 2)
  return n_list

list_with_n_list = ([1,2,3])
print(list_by_2(list_with_n_list)) 

# create_grid(4)
# --> list of list mit 4 Teilen  

def create_grid(size):
  new_grid = []
  for row in range(size):
    new_sublist = []
    for colum in range(size):
      new_sublist.append('-')   # - wegen Aufgabenstellung
    new_grid.append(new_sublist)
  return new_grid


def rand_alive():
  number = random.randint(1,3)
  if number == 1:
    return True
  else:
    return False 




print(circle_area)

print(circle_area)


      







