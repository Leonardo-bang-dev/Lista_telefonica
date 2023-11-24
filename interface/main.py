from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud import create, read, update, delete
from search import search_all, search_contact, search_contacts

root = Tk()


class Funcs():
    def limpar_tela(self): 
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.email_entry.delete(0, END)
    
    def add_contact(self):
        yes_cancel = messagebox.askyesno('Aviso', 'Deseja adicionar este contato ?')
        if yes_cancel == True:
                if self.nome_entry.get() != "" and self.telefone_entry.get() != ""  and self.email_entry.get() != "":
                    if "@gmail.com" in self.email_entry.get() or "@hotmail.com" in self.email_entry.get():
                        self.nome = self.nome_entry.get()
                        self.telefone = self.telefone_entry.get()
                        self.email = self.email_entry.get()
                        create([self.nome, self.telefone, self.email])
                        self.limpar_tela()
                        self.select_table()
                        messagebox.showinfo('Aviso', "Adicionado com sucesso!")
                    else:
                        messagebox.showwarning('Aviso', "Digite um email valido!")
                else:
                    messagebox.showwarning('Aviso', "Preencha todos os campos!")

    def delete_contact(self):
        yes_cancel = messagebox.askyesno('Aviso', 'Deseja deletar este contato ?')
        if yes_cancel == True:
            if self.table_contacts.selection() != ():
                for n in self.table_contacts.selection():
                    nome, telefone, email = self.table_contacts.item(n, 'values')
                    if search_contact(telefone) in search_all():
                        self.limpar_tela()
                        delete([nome, telefone, email])
                        self.select_table()
                        messagebox.showinfo('Aviso', "Contato deletado!")
                    else:
                        messagebox.showwarning('Aviso', "Contato não existente!")
            else:
                messagebox.showwarning('Aviso', "Selecione um contato para ser apagado!")
            
    def update_contact(self):
        yes_cancel = messagebox.askyesno('Aviso', 'Deseja modificar este contato ?')
        if yes_cancel == True:
                nome, telefone, email = self.nome_entry.get(), self.telefone_entry.get(), self.email_entry.get()
                if nome != '' and telefone != '' and email != '':
                    if "@gmail.com" in self.email_entry.get() or "@hotmail.com" in self.email_entry.get():
                        for n in self.table_contacts.selection():
                            nome_, telefone_, email_ = self.table_contacts.item(n, 'values')
                        self.limpar_tela()
                        update(telefone_, [nome,telefone,email])
                        self.select_table()
                        messagebox.showinfo('Aviso', "Modificação feita com Sucesso!")
                    else:
                        messagebox.showwarning('Aviso', "Digite um email valido!")
                else:
                    messagebox.showwarning('Aviso', "Selecione um contato para ser modificado!")    

    def select_table(self):
        self.table_contacts.delete(*self.table_contacts.get_children())
        lista = search_all()
        for datas in lista:  
            self.table_contacts.insert("", END, values = datas)

    def search_table(self):
        nome, telefone, email = self.nome_entry.get(), self.telefone_entry.get(), self.email_entry.get()
        
        self.table_contacts.delete(*self.table_contacts.get_children())
        lista = search_contacts([nome, telefone, email])
        print([nome, telefone, email])
        if lista != []:
            for datas in lista:  
                self.table_contacts.insert("", END, values = datas)
        else:
            self.select_table()

    def on_DoubleClick_table(self, event):
        self.limpar_tela()
        self.table_contacts.selection()

        for n in self.table_contacts.selection():
            nome, telefone, email = self.table_contacts.item(n, 'values')
            self.nome_entry.insert(END, nome)
            self.telefone_entry.insert(END, telefone)
            self.email_entry.insert(END, email)
        

class Application(Funcs):
    def __init__(self): 
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.criando_botoes()
        self.table_table()
        self.select_table()
        root.mainloop()

    def tela(self):
        self.root.title('Lista Telefonica')
        self.root.configure(background='#252525')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width= 1000, height= 800)
        self.root.minsize(width= 400, height= 300)

    def frame_da_tela(self):
        self.form = Frame(self.root, border= 4, bg= '#D5D5D5')
        self.form.place(relx= 0.02, rely= 0.02, relwidth= 0.96, relheight= 0.47,)

        self.table = Frame(self.root, border= 4, bg= '#D5D5D5')
        self.table.place(relx= 0.02, rely= 0.51, relwidth= 0.96, relheight= 0.47,)

    def criando_botoes(self):
        # Criando botao limpar
        self.bt_limpar = Button(self.form, text= 'Limpar', bd=2, bg='#B2B093', command= self.limpar_tela)
        self.bt_limpar.place(relx= 0.01, rely= 0.82, relwidth= 0.1, relheight= 0.15)

        # Criando botao buscar
        self.bt_buscar = Button(self.form, text= 'Buscar', bd=2, bg='#B2B093', command=self.search_table)
        self.bt_buscar.place(relx= 0.12, rely= 0.82, relwidth= 0.1, relheight= 0.15)

        # Criando botao novo
        self.bt_novo = Button(self.form, text= 'Novo', bd=2, bg='#B2B093', command= self.add_contact)
        self.bt_novo.place(relx= 0.35, rely= 0.82, relwidth= 0.1, relheight= 0.15)

        # Criando botao alterar
        self.bt_alterar = Button(self.form, text= 'Alterar', bd=2, bg='#B2B093', command=self.update_contact)
        self.bt_alterar.place(relx= 0.46, rely= 0.82, relwidth= 0.1, relheight= 0.15)

        # Criando botao apagar
        self.bt_apagar = Button(self.form, text= 'Apagar', bd=2, bg='#B2B093',command=self.delete_contact)
        self.bt_apagar.place(relx= 0.57, rely= 0.82, relwidth= 0.1, relheight= 0.15)

        # Criação da label e entrada do nome
        self.lb_nome = Label(self.form, text= 'Nome', background= '#D5D5D5')
        self.lb_nome.place(relx= 0.01, rely= 0.03)
        self.nome_entry = Entry(self.form)
        self.nome_entry.place(relx= 0.01, rely= 0.15, relwidth= 0.65)

        # Criação da label e entrada do telefone
        self.lb_telefone = Label(self.form, text= 'Telefone', background= '#D5D5D5')
        self.lb_telefone.place(relx= 0.68, rely= 0.03)
        self.telefone_entry = Entry(self.form)
        self.telefone_entry.place(relx= 0.68, rely= 0.15, relwidth= 0.30)

        # Criação da label e entrada do email
        self.lb_email = Label(self.form, text= 'Email', background= '#D5D5D5')
        self.lb_email.place(relx= 0.01, rely= 0.30)
        self.email_entry = Entry(self.form)
        self.email_entry.place(relx= 0.01, rely= 0.40, relwidth= 0.70)
        
    def table_table(self):
        self.table_contacts = ttk.Treeview(self.table, height= 3, columns= ('coll', 'col2', 'col3'))
        self.table_contacts.heading('#0', text='')
        self.table_contacts.heading('#1', text='Nome')
        self.table_contacts.heading('#2', text='Telefone')
        self.table_contacts.heading('#3', text='Email')

        self.table_contacts.column('#0', width=1)
        self.table_contacts.column('#1', width=180)
        self.table_contacts.column('#2', width=170)
        self.table_contacts.column('#3', width=150)

        self.table_contacts.place(relx= 0.01, rely= 0.01, relwidth=0.94, relheight= 0.90)
        
        self.scroollist = Scrollbar(self.table, orient= 'vertical')
        self.table_contacts.configure(yscrollcommand = self.scroollist.set)
        self.scroollist.place(relx= 0.95, rely= 0.01, relwidth= 0.04, relheight=0.90)
        self.table_contacts.bind("<Double-1>", self.on_DoubleClick_table)

Application()