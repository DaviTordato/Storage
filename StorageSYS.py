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
def add():
    global ID
    adiction1 = ID
    adiction2 = int(input("Quantia do produto"))
    adiction3 = input("Localização do produto").lower().strip()
    lista.append([adiction1,adiction2,adiction3])
    ID += 1

def Search():
    for items in lista:
        print(f"ID: {items[0]} Amout: {items[1]} Name: {items[2]}")
#-----------------------

#use this as the main loop
while True:
    chose = input("Hello, What you wanna do??\n1-add\n2-Search").strip().lower()
    if chose == "1":
        add()
    elif chose == "2":
        Search()
