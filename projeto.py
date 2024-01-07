from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()
window.title("Gestor de Fotografias")

#Criar ficheiros

f = open("basedados.txt","a")
f.close()


f = open("comentarios.txt","a")
f.close()


f = open("pontuações.txt","a")
f.close()

###############################FUNÇÃO JANELA INICIAL############################### 
def oginWindow():

    #CENTRAR A JANELA

    w = 500
    h = 200
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="#F0F0F0")

    #INSERIR A LABEL E A ENTRY DO UTILIZADOR

    lbl_utilizador.place(x = 120,y = 20)
    txt_utilizador.place(x = 230,y = 53)

    #INSERIR A LABEL E A PALAVRA-PASSE DO UTILIZADOR

    label_password.place()
    text_password.place()

    #INSERIR BOTÕES DE LOGIN E CRIAR CONTA

    button_login.place(x = 190,y = 100)
    button_criarconta.place(x = 190,y = 140)

    #REMOVE ENTRIES E LABELS NÃO NECESSÁRIAS 
    label_email.place_forget() 
    text_email.place_forget()
    label_confirmpasse.place_forget() 
    text_confirmpasse.place_forget()
    button_criar.place_forget()
    button_voltar.place_forget()

    #REMOVE ####
    





###############################FUNÇÃO DA JANELA DE CRIAR CONTA############################### 

def JanelaCriar():

    #AUMENTAR A JANELA PARA COLOCAR NOVOS CAMPOS DE ESCRITA
    
    w = 450
    h = 230
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #CRIAR ESPAÇO PARA A ENTRY DE UTILIZADOR
    
    label_utilizador.place(x = 30,y = 20)
    text_utilizador.place(x = 230,y = 22)

    #PLACE DA ENTRY EMAIL
    
    label_email.place(x = 30,y = 50)
    text_email.place(x = 230,y = 53)

    #PLACE DA ENTRE PASSWORD
    
    label_passe.place(x = 30,y = 80)
    text_passe.place(x = 230,y = 83)

    #PLACE DA ENTRY PARA CONFIRMAR PASSOWRD
    
    label_confirmarpasse.place(x = 30,y = 110)
    text_confirmarpasse.place(x = 230,y = 113)

    #PLACE DO BOTÃO CRIAR 
    
    button_criar.place(x = 240,y = 160)
    button_retornar.place(x = 70, y = 160)

    #APAGAR OS BOTÕES DE LOGIN E DE CRIAR CONTA
    
    button_login.place_forget()
    button_criarconta.place_forget()


    

    #-----------------------------FUNÇÃO LOGIN--------------------------------#
def Login():

    #BUSCA O USUÁRIO E A PASSWORD INSERIDOS
    user = text_utilizador.get()
    password = text_passe.get()

    #GUARDA OS DADOS DE LOGIN NUMA STRING
    guardar = user + ";" + password + ";" + "user"
    guardar_admin = user + ";" + password + ";" + "admin"

    #ABRE O FICHEIRO basedados.txt E PARA LEITURA
    f = open("basedados.txt","r")
    lista = f.readlines()

    #CASO OS CAMPOS ESTEJAM VAZIOS, RETORNA UM ERRO
    if user == "" or password == "":
        messagebox.showerror("Erro","Por favor forneça os seus dados de acesso.")
    
    #CASO OS DADOS DE ACESSO ESTEJAM CORRETOS, EFETUA LOGIN
    else:
        if str(guardar_admin) in str(lista):
           messagebox.showinfo("Bem vindo ADMINISTRADOR")
           txt_passe.delete(0,"end")
           Janela_AppAdmin()

        elif str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso!")
            txt_passe.delete(0,"end")
            Janela_App()
        
        #SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Utilizador ou palavra-passe incorreta. Por favor tente novamente.")
            txt_passe.delete(0,"end")              

#--------------------------FUNÇÃO CRIAR CONTA-----------------------------#
def Criar_Conta():

    #BUSCA OS DADOS DE ACESSO (UTILIZADOR, PASSWORD E EMAIL)
    utilizador = text_utilizador.get()
    password = text_passe.get()
    email = text_email.get()
    passwordC = text_passeC.get()

    #GUARDA OS DADOS DE ACESSO INSERIDOS PARA UMA STRING
    guardar = utilizador + ";" + password + ";" + email

    #ABRE O FICHEIRO basedados.txt PARA LEITURA
    f = open("basedados.txt","r")

    #CASO ALGUM DOS CAMPOS ESTEJA VAZIO, RETORNA UM ERRO
    if utilizador == "" or email == "" or password == "" or cpassword == "":
        messagebox.showerror("Erro","Por favor forneça todos os dados corretamente.")

    #SE OS CAMPOS UTILIZADOR E PALAVRA-PASSE ESTIVEREM PREENCHIDOS, ADICIONA OS DADOS DO FICHEIRO basedados.txt PARA UMA STRING
    if utilizador != "" and password != "":
        lista = f.readlines()

        #VERIFICA SE OS DADOS JÁ SE ENCONTRAM NO FICHEIRO
        if str(guardar) in str(lista):
            messagebox.showerror("Já existe uma conta com esses dados.")

        #VERIFICA SE O NOME DE UTILIZADOR JÁ ESTÁ EM USO 
        elif str(utilizador) in str(lista):
            messagebox.showerror("Esse utilizador já existe.")

        #SE A PALAVRA-PASSE FOR CONFIRMADA CORRETAMENTE CRIA A CONTA  
        else:
            if password == passwordC:
                f = open("basedados.txt","a")
                f.write(utilizador + ";" + password + ";" + "user" + ";" + email + "\n")
                messagebox.showinfo("Sucesso","A sua conta foi criada com sucesso!")
                loginWindow()
            else:
                messagebox.showerror("As passwords não coincidem.")

#-----------------FUNÇÃO JANELA DE CRIAR CONTA ADMIN----------------------#
def JanelaCAdmin():
    JanCAdmin = Toplevel(window)
    JanCAdmin.title("Adicionar Utilizadores")

    w = 450
    h = 230
    ws = JanCAdmin.winfo_screenwidth()
    hs = JanCAdmin.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanCAdmin.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #UTILIZADOR
    label_utilizador=Label(JanCAdmin,text="Utilizador:",fg="black",font=("Helvetica",15))
    text_utilizador=Entry(JanCAdmin,width=30)
    label_utilizador.place(x=30,y=20)
    text_utilizador.place(x=230,y=22)

    #EMAIL
    label_email=Label(JanCAdmin,text="Email:",fg="black",font=("Helvetica",15))
    text_email=Entry(JanCAdmin, width=30)
    label_email.place(x=30,y=50)
    text_email.place(x=230,y=53)

    #PASSWORD
    label_passe=Label(JanCAdmin,text="Palavra-Passe:",fg="black",font=("Helvetica",14))
    text_passe=Entry(JanCAdmin,width=30,show="*")
    label_passe.place(x=30,y=80)
    text_passe.place(x=230,y=83)

    #CONFIRMAR PASSOWRD
    label_cpasse=Label(JanCAdmin,text="Confirmar Palavra-Passe:",fg="black",font=("Helvetica",15))
    text_passeC=Entry(JanCAdmin, width=30,show="*")
    label_passeC.place(x=30,y=110)
    text_passeC.place(x=230,y=113)

    #CHECKBUTTON USER OU ADMIN
    checkb1 = IntVar()
    checkb1.set(1)
    cb2 = IntVar()

    checkb1_utilizador = Checkbutton(JanCAdmin, text="Utilizador", variable = cb1)
    checkb2_utilizador = Checkbutton(JanCAdmin,text="Administrador",variable=cb2)
        
    checkb1_utilizador.place(x=70, y=150)
    checkb2_utilizador.place(x=70, y=180)
