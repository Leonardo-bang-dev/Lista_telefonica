import csv

def search_contact(dado):
    ctr_search = None
    if '@' in dado:
        ctr_search = 2
    elif dado.isdigit():
        ctr_search = 1
    else: 
        ctr_search = 0
    with open('data/lista_telefonica.csv', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.split(',')
            if dado in line[ctr_search]:
                line = ','.join(line)
                line = line[0:-1]
                line = line.split(',')
                return line
                    
def search_contacts(dados):
    contacts = []
    
    with open('data/lista_telefonica.csv', 'r', encoding='utf-8') as file:
        if dados[0] != '' and dados[1] != '' and dados[2] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[0] in line[0] and dados[1] in line[1] and dados[2] in line[2]:
                    contacts.append(line)
        elif dados[0] != '' and dados[1] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[0] in line[0] and dados[1] in line[1]:
                    contacts.append(line)
        elif dados[0] != '' and dados[2] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[0] in line[0] and dados[2] in line[2]:
                    contacts.append(line)
        elif dados[1] != '' and dados[2] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[1] in line[1] and dados[2] in line[2]:
                    contacts.append(line)
        elif dados[0] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[0] in line[0]:
                    contacts.append(line)
        elif dados[1] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[1] in line[1]:
                    contacts.append(line)
        elif dados[2] != '':
            for line in file:
                line = line[0:-1]
                line = line.split(',')
                if dados[2] in line[2]:
                    contacts.append(line)
    return contacts
                    
def search_all():
    contact_list = []
    with open('data/lista_telefonica.csv', 'r', encoding='utf-8') as file:
        for line in file:
            line = line[0:-1]
            line = line.split(',')
            contact_list.append(line)
    return contact_list

