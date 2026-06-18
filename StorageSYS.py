import os
import os

# Funções default
def c():
    os.system('cls')
def k():
    input("Press any thing to continue...")
def s():
    print("----------")
#add a product
#list all products
#Search for id
#Modify the stock
#exit the program
#Commit all in parts
#Main list
ID = 0
lista = []

#Put the functions here:

def listing():
    c()
    for items in lista:
        s()
        print(f"ID: {items[0]}\n Amout: {items[1]}\n location: {items[2]}")
        s()
    k()

def add():
    global ID
    adiction1 = ID
    adiction2 = int(input("Quantia do produto: "))
    adiction3 = input("Localização do produto: ").lower().strip()
    lista.append([adiction1,adiction2,adiction3])
    ID += 1

def search():
    c()
    for items in lista:
        print("----------")
        print(f"ID: {items[0]}\n Amout: {items[1]}\n location: {items[2]}")
        print("----------")
    sid = int(input("ID of the item: "))
    for s in lista:
        if s[0] == sid:
            c()
            print(f"ID: {s[0]}\n Amout: {s[1]}\n location: {s[2]}")
            chose = input("What you wanna do?\n1-Delete")
            if chose == "1":
                
                lista.pop(sid)
        else:
            c()
            print("No items in search.")
            k()

#-----------------------

#use this as the main loop
while True:
    c()
    chose = input("Hello, What you wanna do??\n1-add\n2-list every thing\n3-Search for ID ").strip().lower()
    if chose == "1":
        add()
    elif chose == "2":
        listing()
    elif chose == "3":
        search()
    else:
        input("ERROR")
