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
def loginWindow():

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

    label_utilizador.place(x = 120,y = 20)
    text_utilizador.place(x = 230,y = 53)

    #INSERIR A LABEL E A PALAVRA-PASSE DO UTILIZADOR

    label_passe.place()
    text_passe.place()

    #INSERIR BOTÕES DE LOGIN E CRIAR CONTA

    button_login.place(x = 190,y = 100)
    button_criarconta.place(x = 190,y = 140)

    #REMOVE ENTRIES E LABELS NÃO NECESSÁRIAS 
    label_email.place_forget() 
    text_email.place_forget()
    label_confirmarpasse.place_forget() 
    text_confirmarpasse.place_forget()
    button_criar.place_forget()
    button_retornar.place_forget()

    #REMOVE NÃO NECESSÁRIOS LOGOUT-----------alterar
    btn_guias.place_forget()
    btn_montanhas.place_forget()
    btn_cidades.place_forget()
    btn_praia.place_forget()
    btn_sair.place_forget()
    lbl_menu.place_forget()
    





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
           text_passe.delete(0,"end")
           Janela_AppAdmin()

        elif str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso!")
            text_passe.delete(0,"end")
            Janela_App()
        
        #SE OS DADOS ESTIVEREM ERRADOS, RETORNA UM ERRO
        else:
            messagebox.showerror("Utilizador ou palavra-passe incorreta. Por favor tente novamente.")
            text_passe.delete(0,"end")              

#--------------------------FUNÇÃO CRIAR CONTA-----------------------------#
def Criar_Conta():

    #BUSCA OS DADOS DE ACESSO (UTILIZADOR, PASSWORD E EMAIL)
    utilizador = text_utilizador.get()
    password = text_passe.get()
    email = text_email.get()
    confirmarpasse = text_confirmarpasse.get()

    #GUARDA OS DADOS DE ACESSO INSERIDOS PARA UMA STRING
    guardar = utilizador + ";" + password + ";" + email

    #ABRE O FICHEIRO basedados.txt PARA LEITURA
    f = open("basedados.txt","r")

    #CASO ALGUM DOS CAMPOS ESTEJA VAZIO, RETORNA UM ERRO
    if utilizador == "" or email == "" or password == "" or confirmarpasse == "":
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
            if password == confirmarpasse:
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
    label_confirmarpasse=Label(JanCAdmin,text="Confirmar Palavra-Passe:",fg="black",font=("Helvetica",15))
    text_confirmarpasse=Entry(JanCAdmin, width=30,show="*")
    label_confirmarpasse.place(x=30,y=110)
    text_confirmarpasse.place(x=230,y=113)

    #CHECKBUTTON USER OU ADMIN
    checkb1 = IntVar()
    checkb1.set(1)
    checkb2 = IntVar()

    checkb1_utilizador = Checkbutton(JanCAdmin, text="Utilizador", variable = checkb1)
    checkb2_utilizador = Checkbutton(JanCAdmin,text="Administrador",variable= checkb2)
        
    checkb1_utilizador.place(x=70, y=150)
    checkb2_utilizador.place(x=70, y=180)

    def CriarContaAdmin():
        #BUSCA OS DADOS DE ACESSO (UTILIZADOR, PASSWORD E EMAIL)
        utilizador = text_utilizador.get()
        password = text_passe.get()
        confirmarpassword = text_confirmarpasse.get()
        email = text_email.get()

        #GUARDA OS DADOS DE ACESSO INSERIDOS PARA UMA STRING
        guardar = utilizador + ";" + password + ";" + email

        #ABRE O FICHEIRO basedados.txt PARA LEITURA
        f = open("basedados.txt","r")

        #SE UM CAMPO ESTIVER VAZIO, RETORNA UM ERRO
        if utilizador == "" or email == "" or password == "" or confirmarpassword == "":
            messagebox.showerror("Erro","Por favor forneça todos os dados corretamente.")
            JanCAdmin.attributes("-topmost", True)

        #SE UTILIZADOR E PASSE FOREM PREENCHIDOS, ADICIONA OS DADOS DO FICHEIRO basedados.txt PARA UMA STRING
        if utilizador != "" and password != "":
            lista = f.readlines()

            #VÊ SE OS DADOS JÁ SE ENCONTRAM NO FICHEIRO
            if str(guardar) in str(lista):
                messagebox.showerror("Já existe uma conta com esses dados, por favor efetue login.")
                JanCAdmin.attributes("-topmost"; True)
            
            #VÊ SE O NOME DE UTILIZADOR JÁ ESTÁ EM USO 
            elif str(utilizador) in str(lista):
                messagebox.showerror("Este utilizador já existe.")
                JanCAdmin.attributes("-topmost", True)

            #SE A PALAVRA-PASSE ESTIVER CORRETA, CRIA A CONTA
            else:
                if password == confirmarpassword:
                    if checkb1.get() == 1 and checkb2.get() == 0:
                        f = open("basedados.txt","a")
                        f.write(utilizador + ";" + password + ";" + "user" + ";" + email + "\n")
                        messagebox.showinfo("A sua conta de UTILIZADOR foi criada com sucesso!")
                        WindowAppAdmin()
                        JanelaCAdmin.quit()
                    elif checkb2.get() == 1 and checkb1.get() == 0:
                        f = open("basedados.txt", "a")
                        f.write(utilizador + ";" + password + ";" + "admin" + ";" + email + "\n")
                        messagebox.showinfo("A sua conta de ADMINISTRADOR foi criada com sucesso!")
                        WindowAppAdmin()
                        JanelaCAdmin.quit()
                    elif checkb1.get() == 1 and checkb2.get() == 1:
                        messagebox.showerror("Selecione apenas uma das opções: UTILIZADOR ou ADMINISTRADOR.")
                    else:
                        messagebox.showerror("As duas passwords não coincidem, tente novamente")
                        JanelaCAdmin.attributes("-topmost",True)

    #BOTÃO CRIAR
    button_criar = Button(JanelaCAdmin,text="Criar Conta", fg="white",bg="lightgreen", font = ("Calibri 12 bold"), width=15,height=1, command=CriarContaAdmin)
    button_criar.place(x=240,y=160)



#------------------FUNÇÃO PARA REMOVER CONTA (POR ACABAR!!!!!!!!!!!!)----------------------#
def RemoveUtilizador():
    JanelaRemover = Toplevel(window)
    JanelaRemover.title("Remover Utilizadores")

    w = 450
    h = 230
    ws = JanelaRemover.winfo_screenwidth()
    hs = JanelaRemover.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanelaRemover.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #UTILIZADOR
    label_utilizador=Label(JanelaRemover,text="Utilizador:",fg="black",font=("Times New Roman",14))
    text_utilizador=Entry(JanelaRemover,width=30)
    label_utilizador.place(x=30,y=20)
    text_utilizador.place(x=230,y=22)

    #EMAIL
    label_email=Label(JanelaRemover,text="Email:",fg="black",font=("Times New Roman",14))
    text_email=Entry(JanelaRemover, width=30)
    label_email.place(x=30,y=50)
    text_email.place(x=230,y=53)

    def RemoveUser():

        f = open("basedados.txt","r")
        lista = f.readlines()
        f.close()
        #PROCURA OS DADOS DE ACESSO
        utilizador = text_utilizador.get()
        email = text_email.get()

        if utilizador !="" and email != "":
            
            nf = open("basedados.txt","w")
            for linha in lista:
                if linha != utilizador:
                    print(linha)
                    nf.write(linha)
            nf.close()
        else:
            messagebox.showerror("Por favor introduza os dados corretamente.")

    #BOTÃO REMOVER
    button_RemoveUser = Button(JanelaRemover,text="Remover User", fg="white",bg="red", font = ("Calibri 12 bold"), width=15,height=1, command=RemoveUser)
    button_RemoveUser.place(x=240,y=160)


#BOTÃO PARA LOGIN E CRIAR CONTA
button_login = Button(window, text = "Login", fg = "white", bg="limegreen", font = ("Calibri 12 bold"),width=15,height=1, command = Login)
button_criarconta = Button(window, text = "Criar Conta", fg = "white",bg="royalblue1", font = ("Calibri 12 bold"),width=15,height=1, command = JanelaCriar)
button_criar = Button(window,text="Criar Conta", fg="white",bg="lightgreen", font = ("Calibri 12 bold"), width=15,height=1, command=Criar_Conta)

#UTILIZADOR
label_utilizador=Label(window,text="Utilizador:",fg="black",font=("Times New Roman",14))
text_utilizador=Entry(window,width=30)

#E-MAIL
label_email=Label(window,text="Email:",fg="black",font=("Times New Roman",14))
text_email=Entry(window, width=30)

#PALAVRA-PASSE
label_passe=Label(window,text="Palavra-Passe:",fg="black",font=("Times New Roman",14))
text_passe=Entry(window,width=30,show="")

#CONFIRMAR PALAVRA-PASSE
label_confirmarpasse=Label(window,text="Confirmar Palavra-Passe:",fg="black",font=("Times New Roman",14))
text_confirmarpasse=Entry(window, width=30,show="")

#BOTÃO RETORNAR
button_retornar = Button(window,text="<-- Retornar", fg="white",bg="red", font = ("Calibri 12 bold"), width=15,height=1, command = loginWindow)



#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#REGIÃO JANELA DA APP
def WindowApp():

    #REDIMENSIONAR A JANELA
    w = 980
    h = 550
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.configure(bg ="white")

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS DE INICIO DE SESSÃO
    button_login.place_forget()
    button_criarconta.place_forget()
    button_retornar_menu.place_forget()


    #alterar estes botões---------------------------------------------------------

    #REMOVE OS BOTÕES DAS PRAIAS
    btn_kaanapali.place_forget()
    btn_anse.place_forget()
    btn_navagio.place_forget()
    btn_zlatni.place_forget()

    #REMOVE BOTÕES DAS MONTANHAS
    btn_kilimanjaro.place_forget()
    btn_kirkjufell.place_forget()
    btn_matterhorn.place_forget()
    btn_estrela.place_forget()

    #REMOVE AS LABELS E ENTRIES NÃO NECESSÁRIAS
    label_passe.place_forget()
    label_utilizador.place_forget()
    label_praias.place_forget()
    text_utilizador.place_forget()
    text_passe.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = text_utilizador.get()
    label_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri", 10),width=20,height=1,bg = "white")
    label_user.place(x=10,y=20)

    #INSERE O TITULO DA PÁGINA
    label_menu.place(x=490, y=60,anchor=CENTER)

    #BOTÃO PARA FECHAR TUDO
    button_sair.place(x=856, y=10)

    #INSERE OS BOTÕES DE GUIAS, MONTANHAS, CIDADES E PRAIAS
    btn_guias.place(x=30,y=100)
    btn_montanhas.place(x=260,y=100)
    btn_cidades.place(x=490,y=100)
    btn_praia.place(x=720,y=100)
