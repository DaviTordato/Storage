import os

def c():
    os.system('cls')

def k():
    input('Press any thing to continue... ')

def s():
    print('----------')

ID = 0
lista = []

def listing():
    c()
    for items in lista:
        s()
        print(f"ID: {items[0]}\n Amout: {items[1]}\n location: {items[2]}\n Name: {items[3]}")
    s()
    k()

def add():
    global ID
    adiction1 = ID
    adiction2 = int(input("Quantia do produto: "))
    adiction3 = input("Localização do produto: ").lower().strip()
    adiction4 = input("Nome: ")
    lista.append([adiction1, adiction2, adiction3,adiction4])
    ID += 1

# pesquisar por id

def search():
    c()
    for items in lista:
        print('----------')
        print(f"ID: {items[0]}\n Amout: {items[1]}\n location: {items[2]}\n Name: {items[3]}")
        print('----------')
    sid = int(input("ID of the item: "))
    
    item_found = False
    for item in lista:
        if item[0] == sid:
            item_found = True
            c()
            print(f"ID: {item[0]}\n Amout: {item[1]}\n location: {item[2]}\n Name: {items[3]}\n")
            chose = input("What you wanna do?\n1-Quantity\n")
            if chose == '1':
                newvalue = int(input("New value: "))
                item[1] = newvalue
                # lista.remove(item)
                # id2 = 0
                # for list_item in lista:
                #     list_item[0] = id2
                #     id2 += 1
                # else:
                #     break
            else:
                break
    
    if not item_found:
        c()
        print('No items in search.')
    k()

while True:
    c()
    chose = input("Hello, What you wanna do??\n1-add\n2-list every thing\n3-Search for ID\n").strip().lower()
    if chose == '1':
        add()
    elif chose == '2':
        listing()
    elif chose == '3':
        search()
    else:
        input('ERROR')
