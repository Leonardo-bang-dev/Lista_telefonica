import csv
from search import search_contact,search_all

def create(datas):
    with open('data/lista_telefonica.csv', 'a', encoding='utf-8') as file:
        file_csv = csv.writer(file, delimiter=',', lineterminator='\n')
        file_csv.writerow(datas)
        file.close()

def read():
    with open('data/lista_telefonica.csv', 'r', encoding='utf-8') as file:
        file_csv = csv.reader(file, delimiter=',')
        for line in file_csv:
            print(line)

# passa um str e uma lista
def update(contact, new_contact):
    current_contact = search_contact(contact)
    all_contacts = search_all()
    index_contact = all_contacts.index(current_contact)
    all_contacts[index_contact] = new_contact

    with open('data/lista_telefonica.csv', 'w', encoding='utf-8') as file:
        file_csv = csv.writer(file, lineterminator='\n')
        for contact_ in all_contacts:
            file_csv.writerow(contact_)

def delete(dados):
    all_contacts = search_all()
    all_contacts.remove(dados)
    with open('data/lista_telefonica.csv', 'w', encoding='utf-8') as file:
        file_csv = csv.writer(file, lineterminator='\n')
        for contact_ in all_contacts:
            file_csv.writerow(contact_)

    