import os
import csv
import string
import sys
import imp
import fileinput
lines=[""]
itemsRecodlist=[""]

def ItemRead():
   script_dir = os.path.dirname(__file__)
   rel_path = "DataBase\Tuples.txt"
   abs_file_path = os.path.join(script_dir, rel_path)   
   itemsRecodlist = open(abs_file_path).readlines() 
   itemsRecodlist  = map(lambda s: s.strip(), itemsRecodlist)
   itemsRecodlist  = list(set(itemsRecodlist))
   itemsRecodlist = filter(None, itemsRecodlist) 
   for item in itemsRecodlist:     
     print(item)

   
def ItemAdd():
   ID = 1
   script_dir = os.path.dirname(__file__)
   rel_path = "DataBase\Tuples.txt"
   abs_file_path = os.path.join(script_dir, rel_path)
   itemsRecodlist = open(abs_file_path).readlines() 
   itemsRecodlist  = map(lambda s: s.strip(), itemsRecodlist)
   itemsRecodlist  = list(set(itemsRecodlist))
   itemsRecodlist = filter(None, itemsRecodlist) 
   for item in itemsRecodlist:
      ID = ID + 1
      
   file1 = open(abs_file_path , "a")   
   name = raw_input("Enter Item Name : ")
   Price = raw_input("Enter Price : ")
   Qty = raw_input("Enter Quantity : ")
   file1.write("\n{0}  | {1}  | {2}  #{3}".format(name ,Price , Qty , ID+1 ))
  
def ItemSale():
   ID = 1
   script_dir = os.path.dirname(__file__)
   rel_path = "DataBase\Tuples.txt"
   abs_file_path = os.path.join(script_dir, rel_path)
   itemsRecodlist = open(abs_file_path).readlines()
   ID = raw_input("Enter Item ID : ")
   itemsRecodlist  = map(lambda s: s.strip(), itemsRecodlist)
   itemsRecodlist  = list(set(itemsRecodlist))
   itemsRecodlist = filter(None, itemsRecodlist) 
   for item in itemsRecodlist:
       unique =   item.split("#")        
       if(ID  == unique[1]):
              Qty = raw_input("Enter Item Quantity : ")
              line1 = unique[0]
              feild = line1.split("|")
              qtys = int(feild[2])
              sold = qtys- int(Qty)
              newstr = "\n"+str(feild[0]) + "|" + str(feild[1]) + "|" +str(sold) + " # " +str(ID)
              replaceAll(abs_file_path , item , newstr) 
              print("sold....")
        
  
    
def replaceAll(file,searchExp,replaceExp):
    for line in fileinput.input(file, inplace=1):
        if searchExp in line:
            line = line.replace(searchExp,replaceExp)
        sys.stdout.write(line)

def Main():
  
  ans=True
  while ans:
    print ("""
    1.View Items
    2.Add Items
    3.Sales
    4.Exit/Quit
    """)
    ans=raw_input("Select option from menu? ") 
    if ans=="1":       
       ItemRead()       
    elif ans=="2":
       ItemAdd()
    elif ans=="3":
       ItemSale()   
    elif ans=="4":
      exit()
    elif ans !="":
      print("\n Not Valid Choice Try again") 


Main()	

 
