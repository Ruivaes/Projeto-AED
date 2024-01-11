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

def dev():
    messagebox.showinfo("ACESSO RESTRITO", "Esta pagina ainda está em desenvolvimento")
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
    text_utilizador.place(x = 230,y = 22)

    #INSERIR A LABEL E A PALAVRA-PASSE DO UTILIZADOR

    label_passe.place(x=90,y=50)
    text_passe.place(x=230,y=53)

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
    button_carlos.place_forget()     
    button_dora.place_forget()  
    button_cristina.place_forget()    
    button_manuel.place_forget()    
    button_sair.place_forget()
    label_menu.place_forget()
    





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
            WindowAppAdmin()

        elif str(guardar) in str(lista):
            messagebox.showinfo("Bem vindo",f"Olá {user}, o seu login foi efetuado com sucesso!")
            text_passe.delete(0,"end")
            WindowApp()
        
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
                JanCAdmin.attributes("-topmost", True)
            
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

    #REMOVE OS BOTÕES DAS MANUEL
    button_manueldesporto.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelarte.place_forget()
    button_manuelcarros.place_forget()

    #REMOVE BOTÕES DAS DORA
    button_doradesporto.place_forget()
    button_doranatureza.place_forget()
    button_doraarte.place_forget()
    button_doracarros.place_forget()

    #REMOVE AS LABELS E ENTRIES NÃO NECESSÁRIAS
    label_passe.place_forget()
    label_utilizador.place_forget()
    label_manuel.place_forget()       
    text_passe.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = text_utilizador.get()
    label_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri", 10),width=20,height=1,bg = "white")
    label_user.place(x=10,y=20)

    #INSERE O TITULO DA PÁGINA
    label_menu.place(x=490, y=60,anchor=CENTER)

    #BOTAO PARA FECHAR TUDO
    button_sair.place(x=856 ,y=10)

    #INSERE OS BOTÕES DE CARLOS, DORA, CRISTINA E MANUEL
    
    button_carlos.place(x=30,y=100)
    button_dora.place(x=260,y=100)
    button_cristina.place(x=490,y=100)
    button_manuel.place(x=720,y=100)

    text_utilizador.place_forget()

#LABEL MENU PRINCIPAL
label_menu = Label(window, text="MENU PRINCIPAL",fg = "black", bg="white", font=("Calibri 25 bold"), width = 30, height = 1)

#BOTÃO SAIR
button_sair = Button(window, text = "SAIR", fg = "red", font = ("Calibri", 12),width=10,height=1, command = window.quit)

#BOTÃO RETORNAR MENU
button_retornar_menu = Button(window, text="Menu", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=WindowApp)


#JANELA DA APP DE ADMIN
def WindowAppAdmin():
    
    #REDIMENSIONAR A JANELA
    w = 980
    h = 550
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    window.title("Gestor de Roteiro de Viagens (Modo Administrador) ")

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS DE INICIO DE SESSÃO
    button_login.place_forget()
    button_criarconta.place_forget()
    button_retornar_menu.place_forget()

    #REMOVE OS BOTÕES DAS MANUEL
    button_manueldesporto.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelarte.place_forget()
    button_manuelcarros.place_forget()

    #REMOVE BOTÕES DAS DORA
    button_doradesporto.place_forget()
    button_doranatureza.place_forget()
    button_doraarte.place_forget()
    button_doracarros.place_forget()

    #REMOVE AS LABELS E ENTRIES NÃO NECESSÁRIAS
    label_passe.place_forget()
    label_utilizador.place_forget()
    label_manuel.place_forget()
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

    #INSERE OS BOTÕES DAS CATEGORIAS

    if chk_g.get() == 1:
        button_carlos.place(x=30,y=100)
    else:
        button_carlos.place_forget()

    if chk_m.get() == 1:
        button_dora.place(x=260,y=100)
    else:
        button_dora.place_forget()

    if chk_c.get() == 1:
        button_cristina.place(x=490,y=100)
    else:
        button_cristina.place_forget()

    if chk_p.get() == 1:
        button_manuel.place(x=720,y=100)
    else:
        button_manuel.place_forget()

    if chk_r.get() == 1 and chk_g.get() == 0:
        button_rui.place(x=30,y=100)
        button_carlos.place_forget()
    elif chk_r.get() == 1 and chk_m.get() == 0:
        button_rui.place(x=260,y=100)
        button_dora.place_forget()
    elif chk_r.get() == 1 and chk_c.get() == 0:
        button_rui.place(x=490,y=100)
        button_cristina.place_forget()
    elif chk_r.get() == 1 and chk_p.get() == 0:
        button_rui.place(x=720,y=100)
        button_manuel.place_forget()
    else:
        button_rui.place_forget()

    if chk_t.get() == 1 and chk_g.get() == 0:
        button_angela.place(x=30,y=100)
        button_carlos.place_forget()
    elif chk_t.get() == 1 and chk_m.get() == 0:
        button_angela.place(x=260,y=100)
        button_dora.place_forget()
    elif chk_t.get() == 1 and chk_c.get() == 0:
        button_angela.place(x=490,y=100)
        button_cristina.place_forget()
    elif chk_t.get() == 1 and chk_p.get() == 0:
        button_angela.place(x=720,y=100)
        button_manuel.place_forget()
    else:
        button_angela.place_forget()

    if chk_r.get() == 1 and chk_t.get() == 1:
        if chk_g.get() == 0 and chk_m.get() == 0:
            button_rui.place(x=30,y=100)
            button_carlos.place_forget()
            button_angela.place(x=260,y=100)
            button_dora.place_forget()
        elif chk_g.get() == 0 and chk_c.get() == 0:
            button_rui.place(x=30,y=100)
            button_carlos.place_forget()
            button_angela.place(x=490,y=100)
            button_cristina.place_forget()
        elif chk_g.get() == 0 and chk_p.get() == 0:
            button_rui.place(x=30,y=100)
            button_carlos.place_forget()
            button_angela.place(x=720,y=100)
            button_manuel.place_forget()
        elif chk_m.get() == 0 and chk_c.get() == 0:
            button_rui.place(x=260,y=100)
            button_dora.place_forget()
            button_angela.place(x=490,y=100)
            button_cristina.place_forget()
        elif chk_m.get() == 0 and chk_p.get() == 0:
            button_rui.place(x=260,y=100)
            button_dora.place_forget()
            button_angela.place(x=720,y=100)
            button_manuel.place_forget()
        elif chk_c.get() == 0 and chk_p.get() == 0:
            button_rui.place(x=490,y=100)
            button_cristina.place_forget()
            button_angela.place(x=720,y=100)
            button_manuel.place_forget()    
     #BARRA MENU ADMIN
    barra_admin = Menu(window)

    utilizadores_Menu = Menu(barra_admin)
    utilizadores_Menu.add_command(label="Adicionar Utilizadores", command=JanelaCAdmin)
    # utilizadores_Menu.add_command(label="Remover Utilizadores", command=removerUtilizador)
    barra_admin.add_cascade(label="Utilizadores", menu=utilizadores_Menu)

    categorias_menu = Menu(barra_admin)
    categorias_menu.add_command(label = "Alterar Categorias",command=escolha_categorias)
    barra_admin.add_cascade(label = "Categorias", menu=categorias_menu)

    ordenar_menu = Menu(barra_admin)
    ordenar_menu.add_command(label="Mais Popular", command = ordenar_gostos)
    # ordenar_menu.add_command(label="Mais Comentada", command = dev)
    barra_admin.add_cascade(label="Ordenar", menu=ordenar_menu)

    window.configure(bg ="white", menu=barra_admin)

#LABEL MENU PRINCIPAL
label_menu = Label(window, text="MENU PRINCIPAL",fg = "black", bg="white", font=("Calibri 25 bold"), width = 30, height = 1)

#BOTÃO SAIR
button_sair = Button(window, text = "SAIR", fg = "red", font = ("Calibri", 12),width=10,height=1, command = window.quit)

#BOTÃO RETORNAR MENU
button_retornar_menu = Button(window, text="Menu", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=WindowApp)



#region carlos E ROTEIROS
def carlos_roteiros():

    #REDIMENSIONAR A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    button_carlos.place_forget()
    button_dora.place_forget()
    button_cristina.place_forget()
    button_manuel.place_forget()
    button_retornar.place_forget()
    button_sair.place_forget()

    #REMOVE A LABEL DO MENU
    label_menu.place_forget()

    #REMOVE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    button_retornar_menu.place(x=380,y=10)

#BOTÃO carlos E ROTEIROS
foto_carlos = ImageTk.PhotoImage(Image.open("carlos.png"))
button_carlos = Button(window, text = "", fg="black", width = 220, height = 395,image = foto_carlos, command = dev)

#endregion

#region dora
def dora():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.configure(bg ="#aba8e2")
    
    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    button_carlos.place_forget()
    button_dora.place_forget()
    button_cristina.place_forget()
    button_manuel.place_forget()
    button_sair.place_forget()
    button_rui.place_forget()
    button_angela.place_forget()

    #REMOVE A LABEL DO MENU PRINCIPAL
    label_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU
    button_retornar_dora.place_forget()
    button_retornar_menu.place(x=740,y=17)

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = text_utilizador.get()
    label_user = Label(window, text= f"Utilizador: {user}",fg="black",font = ("Calibri bold", 10),width=20,height=1,bg = "#aba8e2")
    label_user.place(x=10,y=20)
    
    #BOTÃO doradesporto
    button_doradesporto.place(x=55,y=90)
    
    #REMOVE A IMAGEM E A DESCRIÇÃO DA doradesporto
    desc_doradesporto.place_forget()
    label_doradesporto.place_forget()

    #BOTÃO doranatureza
    button_doranatureza.place(x=55, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA doranatureza
    desc_doranatureza.place_forget()
    label_doranatureza.place_forget()

    #BOTÃO doraarte
    button_doraarte.place(x=450,y=90)

    #BOTÃO SERRA DA doracarros
    button_doracarros.place(x=450, y=310)

def doradesporto():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))


    #REMOVE OS BOTÕES DAS dora
    button_doradesporto.place_forget()
    button_doraarte.place_forget()
    button_doranatureza.place_forget()
    button_doracarros.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_dora.place(x=740,y=17)

    #INSERE A IMAGEM
    label_doradesporto.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA MONTANHA
    desc_doradesporto.place(x=445,y=400, anchor=CENTER)

def doranatureza():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS dora
    button_doradesporto.place_forget()
    button_doraarte.place_forget()
    button_doranatureza.place_forget()
    button_doracarros.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_dora.place(x=740,y=17)

    #INSERE A IMAGEM
    label_doranatureza.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA MONTANHA
    desc_doranatureza.place(x=445,y=400, anchor=CENTER)

#BOTÃO dora
foto_dora=ImageTk.PhotoImage(Image.open("dora.png"))
button_dora=Button(window,text="",width = 220, height = 395,image = foto_dora, command = dora)

#BOTÃO RETORNAR dora
button_retornar_dora = Button(window, text="Retornar", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=dora)

#doradesporto
foto_doradesporto = ImageTk.PhotoImage(Image.open("doradesporto.png"))
button_doradesporto=Button(window,text="",width = 375, height = 200,image = foto_doradesporto,command=doradesporto)
label_doradesporto = Label(window,text="",width = 375, height = 200,image = foto_doradesporto)
desc_doradesporto = Label(window,text="O Parque Nacional do doradesporto já é famoso pelo enorme nome que carrega da famosa montanha da luz,\ntambém conhecida como Kilimanharo.O parque nacional é um dos parques nacionais que se encontram em\num dos países da África Oriental, a Tanzânia. O parque possui a montanha mais alta com neve na África,\nchamada de parque nacional doradesporto. O parque nacional doradesporto está localizado na parte norte da\nTanzânia, logo acima das colinas suaves e do planalto do parque nacional Amboeseli.", font=("Calibri 14"),bg="#aba8e2", width = 85, height = 5)

#doranatureza
foto_doranatureza = ImageTk.PhotoImage(Image.open("doranatureza.png"))
button_doranatureza=Button(window,text="",width = 375, height = 200,image = foto_doranatureza,command=doranatureza)
label_doranatureza = Label(window,text="",width = 375, height = 200,image = foto_doranatureza)
desc_doranatureza = Label(window,text="doranatureza, ou 'Montanha da Igreja', é um pico de formato distinto encontrado na costa norte da Península\nde Snæfellsnes, na Islândia, a apenas uma curta distância da cidade de Grundarfjörður. É frequentemente\nchamada de 'a montanha mais fotografada da Islândia',devido à sua formação dramática\ne localização costeira perfeita.", font=("Calibri 14"),bg="#aba8e2", width = 85, height = 5)

#doraarte
foto_doraarte = ImageTk.PhotoImage(Image.open("doraarte.png"))
button_doraarte=Button(window,text="",width = 375, height = 200,image = foto_doraarte,command=dev)

#SERRA DA doracarros
foto_doracarros = ImageTk.PhotoImage(Image.open("doracarros.png"))
button_doracarros=Button(window,text="",width = 375, height = 200,image = foto_doracarros,command=dev)

#endregion

#region cristina
def cristina():

    #REDIMENSIONA A JANELA
    w = 500
    h = 500
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))
    
    #ESQUECE OS BOTÕES NÃO NECESSÁRIOS
    button_carlos.place_forget()
    button_dora.place_forget()
    button_cristina.place_forget()
    button_manuel.place_forget()
    button_sair.place_forget()

    #ESQUECE A LABEL DO MENU PRINCIPAL
    label_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU PRINCIPAL
    button_retornar_menu.place(x=380,y=10)

#BOTÃO cristina
foto_cristina=ImageTk.PhotoImage(Image.open("cristina.png"))
button_cristina=Button(window,text="",width = 220, height = 395,image = foto_cristina,command = dev)

#endregion

#region manuel
def manuel():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    window.configure(bg ="#025083")

    #REMOVE OS BOTÕES NÃO NECESSÁRIOS
    button_carlos.place_forget()
    button_dora.place_forget()
    button_cristina.place_forget()
    button_manuel.place_forget()
    button_sair.place_forget()
    button_rui.place_forget()
    button_angela.place_forget()

    #REMOVE A LABEL DO MENU PRINCIPAL
    label_menu.place_forget()

    #INSERE O BOTÃO PARA RETORNAR AO MENU 
    button_retornar_manuel.place_forget()
    button_retornar_menu.place(x=740,y=17)

    #REMOVE OS BOTÕES DE COMENTÁRIO
    button_comentar_manuelnatureza.place_forget()
    button_comentar_manuelcarros.place_forget()
    button_comentar_manuelarte.place_forget()
    button_comentar_manueldesporto.place_forget()

    text_comentario.place_forget()

    button_submeter_manuelnatureza.place_forget()
    button_submeter_manuelcarros.place_forget()
    button_submeter_manuelarte.place_forget()
    button_submeter_manueldesporto.place_forget()

    button_ver_manuelnatureza.place_forget()
    button_ver_manuelcarros.place_forget()
    button_ver_manueldesporto.place_forget()
    button_ver_manuelarte.place_forget()

    #REMOVE OS BOTÕES DE GOSTO
    button_gosto_manuelnatureza.place_forget()
    button_gosto_manuelcarros.place_forget()
    button_gosto_manuelarte.place_forget()
    button_gosto_manueldesporto.place_forget()

    #INSERE O NOME DE UTILIZADOR QUE ESTÁ AUTENTICADO
    user = text_utilizador.get()
    label_user = Label(window, text= f"Utilizador: {user}",fg="white",font = ("Calibri bold", 10),width=20,height=1,bg = "#025083")
    label_user.place(x=10,y=20)

    #TITULO DA JANELA
    label_manuel.place(x=442.5,y=60, anchor=CENTER)
    
    #BOTÃO DA manuel manuelnatureza
    button_manuelnatureza.place(x=55,y=90)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA manuelnatureza
    label_manuelnatureza.place_forget()
    desc_manuelnatureza.place_forget()

    #BOTÃO manuel manuelarte
    button_manuelarte.place(x=55, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA manuelarte
    label_manuelarte.place_forget()
    desc_manuelarte.place_forget()

    #BOTÃO manuel manuelcarros
    button_manuelcarros.place(x=450,y=90)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA manuelcarros
    label_manuelcarros.place_forget()
    desc_manuelcarros.place_forget()

    #BOTÃO manuel manueldesporto
    button_manueldesporto.place(x=450, y=310)

    #REMOVE A IMAGEM E A DESCRIÇÃO DA manueldesporto
    label_manueldesporto.place_forget()
    desc_manueldesporto.place_forget()

def manuelarte():

    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS manuel
    button_manuelarte.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelcarros.place_forget()
    button_manueldesporto.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_manuel.place(x=740,y=17)

    #INSERE A IMAGEM
    label_manuelarte.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA manuel
    desc_manuelarte.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    button_comentar_manuelarte.place(x=414,y=520,anchor=CENTER)
    button_ver_manuelarte.place(x=572, y=520, anchor = CENTER)

    #GOSTO
    button_gosto_manuelarte.place(x=292,y=520,anchor=CENTER)

def manuelnatureza():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS manuel
    button_manuelarte.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelcarros.place_forget()
    button_manueldesporto.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_manuel.place(x=740,y=17)

    #INSERE A IMAGEM
    label_manuelnatureza.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA manuel
    desc_manuelnatureza.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    button_comentar_manuelnatureza.place(x=414,y=520,anchor=CENTER)
    button_ver_manuelnatureza.place(x=572, y=520, anchor = CENTER)

    #GOSTO
    button_gosto_manuelnatureza.place(x=292,y=520,anchor=CENTER)

def manuelcarros():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS manuel
    button_manuelarte.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelcarros.place_forget()
    button_manueldesporto.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_manuel.place(x=740,y=17)

    #INSERE A IMAGEM
    label_manuelcarros.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA manuel
    desc_manuelcarros.place(x=445,y=400, anchor=CENTER)

    #COMENTÁRIO
    button_comentar_manuelcarros.place(x=414,y=520,anchor=CENTER)
    button_ver_manuelcarros.place(x=572, y=520, anchor = CENTER)

    #GOSTO
    button_gosto_manuelcarros.place(x=292,y=520,anchor=CENTER)

def manueldesporto():
    #REDIMENSIONAR A JANELA
    w = 885
    h = 560
    ws = window.winfo_screenwidth()
    hs = window.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #REMOVE OS BOTÕES DAS manuel
    button_manuelarte.place_forget()
    button_manuelnatureza.place_forget()
    button_manuelcarros.place_forget()
    button_manueldesporto.place_forget()

    #TROCA O BOTÃO MENU POR BOTÃO RETORNAR
    button_retornar_menu.place_forget()
    button_retornar_manuel.place(x=740,y=17)

    #INSERE A IMAGEM
    label_manueldesporto.place(x=445, y=200, anchor = CENTER)

    #DESCRIÇÃO DA manuel
    desc_manueldesporto.place(x=445,y=400, anchor=CENTER)

      #COMENTÁRIO
    button_comentar_manueldesporto.place(x=414,y=520,anchor=CENTER)
    button_ver_manueldesporto.place(x=572, y=520, anchor = CENTER)

    #GOSTO
    button_gosto_manueldesporto.place(x=292,y=520,anchor=CENTER)

#BOTÃO PRINCIPAL
foto_manuel=ImageTk.PhotoImage(Image.open("manuel.png"))
button_manuel=Button(window,text="",width = 220, height = 395,image = foto_manuel, command = manuel)

#BOTÃO RETORNAR manuel
button_retornar_manuel = Button(window, text="Retornar", fg="black",font = ("Calibri 12 bold"), width=10,height=1, command=manuel)

#manuelarte
foto_manuelarte = ImageTk.PhotoImage(Image.open("manuelarte.png"))
button_manuelarte = Button(window,text="",width = 375, height = 200,image = foto_manuelarte,command=manuelarte)
label_manuelarte = Label(window,text="",width = 375, height = 200,image = foto_manuelarte)
desc_manuelarte = Label(window,text="manuelarte está localizado no noroeste de Zakynthos (Ilha grega). As colinas de alturas variáveis que\nprotegem a baía e a manuel dos ventos fortes contribuem para a sua singularidade. A manuel é coberta por\nareia macia e limpa de cor creme e uma água bastante clara.", font=("Calibri 14"),bg="#025083", fg="white", width = 80, height = 4)

#manuelnatureza
foto_manuelnatureza = ImageTk.PhotoImage(Image.open("manuelnatureza.png"))
button_manuelnatureza = Button(window,text="",width = 375, height = 200,image = foto_manuelnatureza,command=manuelnatureza)
label_manuelnatureza = Label(window,text="",width = 375, height= 200, image=foto_manuelnatureza)
desc_manuelnatureza = Label(window,text="Localizada no extremo oeste de La Digue, manuelnatureza Source d'Argent é um autêntico paraíso na terra, uma\nbela manuel de areia branca e calmas águas turquesas rodeada por coqueiros e curiosos blocos de granito\nmoldados com o passar do tempo.",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#manuelcarros
foto_manuelcarros = ImageTk.PhotoImage(Image.open("manuelcarros.png"))
button_manuelcarros = Button(window,text="",width = 375, height = 200,image = foto_manuelcarros,command=manuelcarros)
label_manuelcarros = Label(window,text="",width = 375, height= 200, image=foto_manuelcarros)
desc_manuelcarros = Label(window,text="manuelcarros Rat é uma manuel na cidade de Bol, que fica na Ilha de Brač. Um fenômeno natural da região\nformou uma ponta de areia, que parece um chifre, cercado de um mar turquesa maravilhoso.\nPor conta desse visual, a manuel ganhou esse nome: manuelcarros Rat, que significa\nChifre Dourado, na língua local. ",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#manueldesporto
foto_manueldesporto = ImageTk.PhotoImage(Image.open("manueldesporto.png"))
button_manueldesporto = Button(window,text="",width = 375, height = 200,image = foto_manueldesporto,command=manueldesporto)
label_manueldesporto = Label(window,text="",width = 375, height= 200, image=foto_manueldesporto)
desc_manueldesporto = Label(window,text="manueldesporto Beach em Maui se estende por 3 milhas entre o Hyatt Regency Maui para o sul e Sheraton\nMaui para o norte. Muito tempo atrás, costumava ser um playground para os membros da realeza de\nMaui e hoje esta manuel incrível é um dos pontos mais visitados da ilha.",font=("Calibri 14"), bg="#025083", fg="white", width = 80, height = 4)

#TITULO: manuel
label_manuel = Label(window, text= "manuel",fg = "white", bg="#025083", font=("Calibri 25 bold"), width = 30, height = 1)

#endregion

#region rui

#BOTÃO rui
foto_rui=ImageTk.PhotoImage(Image.open("rui.png"))
button_rui=Button(window, text = "", width = 220, height = 395,image = foto_rui, command=dev)

#endregion

#region angela E OUTDOORS

#BOTÃO angela E OUTDOORS
foto_angela=ImageTk.PhotoImage(Image.open("angela.png"))
button_angela=Button(window, text = "",width = 220, height = 395,image = foto_angela,command=dev)

#endregion

#region GESTÃO DE COMENTÁRIOS

#COMENTARIOS manuelnatureza
def comentar_manuelnatureza():
    text_comentario.place(x=402,y=490, anchor=CENTER)
    button_comentar_manuelnatureza.place_forget()
    button_gosto_manuelnatureza.place_forget()
    button_ver_manuelnatureza.place_forget()
    button_submeter_manuelnatureza.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_manuelnatureza():

    comentario = text_comentario.get("1.0",END)
    user = text_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("manuelnatureza: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")
    text_comentario.delete("1.0",END)

    text_comentario.place_forget()
    button_submeter_manuelnatureza.place_forget()
    manuelnatureza()

def ver_cmt_manuelnatureza():
    f = open("comentarios.txt","r")
    linhas = f.readlines()
    manuelnatureza = ""
    for i in linhas:
        if str("manuelnatureza") in i:
            edit = i.replace("manuelnatureza:","-")
            manuelnatureza+= edit + "\n"
    if manuelnatureza == "":
        messagebox.showerror("ERRO", "Não existem comentários.")
    else:
        JanComentarios = Toplevel(window)
        JanComentarios.title("Comentários manuelnatureza")
        label_manuelnatureza_cmt = Label(JanComentarios,text="Comentários da manuel manuelnatureza", font=("Calibri 16 bold"), width=30, height = 3)
        label_manuelnatureza_cmt.place(x=250,y=30,anchor=CENTER)
        w = 500
        h = 200
        ws = JanComentarios.winfo_screenwidth()
        hs = JanComentarios.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        JanComentarios.geometry('%dx%d+%d+%d' % (w, h, x, y))
        print(manuelnatureza)
        label_cmt_manuelnatureza= Text(JanComentarios,width=60, height=5)
        label_cmt_manuelnatureza.place(x=250,y=120,anchor=CENTER)
        label_cmt_manuelnatureza.insert("end", manuelnatureza)
        
button_comentar_manuelnatureza=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_manuelnatureza)
text_comentario = Text(window,width=80,height=5)
button_submeter_manuelnatureza = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_manuelnatureza)
button_ver_manuelnatureza=Button(window, text="Ver comentários",fg="black", font = ("Calibri bold", 12),width=15,height=1, command = ver_cmt_manuelnatureza)

#COMENTARIOS manuelcarros
def comentar_manuelcarros():
    text_comentario.place(x=402,y=490, anchor=CENTER)
    button_comentar_manuelcarros.place_forget()
    button_gosto_manuelcarros.place_forget()
    button_ver_manuelcarros.place_forget()
    button_submeter_manuelcarros.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_manuelcarros():

    comentario = text_comentario.get("1.0",END)
    user = text_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("manuelcarros: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    text_comentario.place_forget()
    button_submeter_manuelcarros.place_forget()
    manuelcarros()

def ver_cmt_manuelcarros():
    f = open("comentarios.txt","r")
    linhas = f.readlines()
    manuelcarros = ""
    for i in linhas:
        if str("manuelcarros") in i:
            edit = i.replace("manuelcarros:","-")
            manuelcarros+= edit + "\n"
    if manuelcarros == "":
        messagebox.showerror("ERRO", "Não existem comentários.")
    else:
        JanComentarios = Toplevel(window)
        JanComentarios.title("Comentários manuelcarros")
        label_manuelcarros_cmt = Label(JanComentarios,text="Comentários da manuel manuelcarros", font=("Calibri 16 bold"), width=30, height = 3)
        label_manuelcarros_cmt.place(x=250,y=30,anchor=CENTER)
        w = 500
        h = 200
        ws = JanComentarios.winfo_screenwidth()
        hs = JanComentarios.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        JanComentarios.geometry('%dx%d+%d+%d' % (w, h, x, y))
        print(manuelcarros)
        label_cmt_manuelcarros= Text(JanComentarios,width=60, height=5)
        label_cmt_manuelcarros.place(x=250,y=120,anchor=CENTER)
        label_cmt_manuelcarros.insert("end", manuelcarros)

button_comentar_manuelcarros=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_manuelcarros)
text_comentario = Text(window,width=80,height=5)
button_submeter_manuelcarros = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_manuelcarros)
button_ver_manuelcarros=Button(window, text="Ver comentários",fg="black", font = ("Calibri bold", 12),width=15,height=1, command = ver_cmt_manuelcarros)

#COMENTAR manuelarte
def comentar_manuelarte():
    text_comentario.place(x=402,y=490, anchor=CENTER)
    button_comentar_manuelarte.place_forget()
    button_gosto_manuelarte.place_forget()
    button_ver_manuelarte.place_forget()
    button_submeter_manuelarte.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_manuelarte():

    comentario = text_comentario.get("1.0",END)
    user = text_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("manuelarte: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    text_comentario.place_forget()
    button_submeter_manuelarte.place_forget()
    manuelarte()

def ver_cmt_manuelarte():
    f = open("comentarios.txt","r")
    linhas = f.readlines()
    manuelarte = ""
    for i in linhas:
        if str("manuelarte") in i:
            edit = i.replace("manuelarte:","-")
            manuelarte+= edit + "\n"
    if manuelarte == "":
        messagebox.showerror("ERRO", "Não existem comentários.")
    else:
        JanComentarios = Toplevel(window)
        JanComentarios.title("Comentários manuelarte")
        label_manuelarte_cmt = Label(JanComentarios,text="Comentários da manuel manuelarte", font=("Calibri 16 bold"), width=30, height = 3)
        label_manuelarte_cmt.place(x=250,y=30,anchor=CENTER)
        w = 500
        h = 200
        ws = JanComentarios.winfo_screenwidth()
        hs = JanComentarios.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        JanComentarios.geometry('%dx%d+%d+%d' % (w, h, x, y))
        print(manuelarte)
        label_cmt_manuelarte= Text(JanComentarios,width=60, height=5)
        label_cmt_manuelarte.place(x=250,y=120,anchor=CENTER)
        label_cmt_manuelarte.insert("end", manuelarte)

button_comentar_manuelarte=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_manuelarte)
text_comentario = Text(window,width=80,height=5)
button_submeter_manuelarte = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_manuelarte)
button_ver_manuelarte=Button(window, text="Ver comentários",fg="black", font = ("Calibri bold", 12),width=15,height=1, command = ver_cmt_manuelarte)

#COMENTAR manueldesporto
def comentar_manueldesporto():
    text_comentario.place(x=402,y=490, anchor=CENTER)
    button_comentar_manueldesporto.place_forget()
    button_gosto_manueldesporto.place_forget()
    button_ver_manueldesporto.place_forget()
    button_submeter_manueldesporto.place(x=795,y=490,anchor=CENTER)

def submeter_comentario_manueldesporto():

    comentario = text_comentario.get("1.0",END)
    user = text_utilizador.get()

    f = open("comentarios.txt","a")
    f.write("manueldesporto: " + user + ":" + comentario)
    messagebox.showinfo("Sucesso","O seu comentário foi adicionado com sucesso!")

    text_comentario.place_forget()
    button_submeter_manueldesporto.place_forget()
    manueldesporto()

def ver_cmt_manueldesporto():
    f = open("comentarios.txt","r")
    linhas = f.readlines()
    manueldesporto = ""
    for i in linhas:
        if str("manueldesporto") in i:
            edit = i.replace("manueldesporto:","-")
            manueldesporto+= edit + "\n"
    if manueldesporto == "":
        messagebox.showerror("ERRO", "Não existem comentários.")
    else:
        JanComentarios = Toplevel(window)
        JanComentarios.title("Comentários manueldesporto")
        label_manueldesporto_cmt = Label(JanComentarios,text="Comentários da manuel manueldesporto", font=("Calibri 16 bold"), width=30, height = 3)
        label_manueldesporto_cmt.place(x=250,y=30,anchor=CENTER)
        w = 500
        h = 200
        ws = JanComentarios.winfo_screenwidth()
        hs = JanComentarios.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        JanComentarios.geometry('%dx%d+%d+%d' % (w, h, x, y))
        print(manueldesporto)
        label_cmt_manueldesporto= Text(JanComentarios,width=60, height=5)
        label_cmt_manueldesporto.place(x=250,y=120,anchor=CENTER)
        label_cmt_manueldesporto.insert("end", manueldesporto)

button_comentar_manueldesporto=Button(window, text="Adicionar comentário",fg="black", font = ("Calibri bold", 12),width=20,height=1, command = comentar_manueldesporto)
text_comentario = Text(window,width=80,height=5)
button_submeter_manueldesporto = Button(window, text="Submeter",fg="black", font = ("Calibri bold", 12),width=10,height=1, command = submeter_comentario_manueldesporto)
button_ver_manueldesporto=Button(window, text="Ver comentários",fg="black", font = ("Calibri bold", 12),width=15,height=1, command = ver_cmt_manueldesporto)

#endregion

#region CLASSIFICAÇÕES

#CLASSIFICAR manuelnatureza
def gosto_manuelnatureza():
    f = open("classificacoes.text","a")
    f.write("manuelnatureza" + "\n")
    
    f= open("classificacoes.text","r")
    encontrar = f.read()
    num = encontrar.count("manuelnatureza")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta manuel já tem {num} gosto(s).")

#CLASSIFICAR manuelcarros
def gosto_manuelcarros():
    f = open("classificacoes.text","a")
    f.write("manuelcarros" + "\n")
    
    f= open("classificacoes.text","r")
    encontrar = f.read()
    num = encontrar.count("manuelcarros")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta manuel já tem {num} gosto(s).")

#CLASSIFICAR manuelarte
def gosto_manuelarte():
    f = open("classificacoes.text","a")
    f.write("manuelarte" + "\n")
    
    f= open("classificacoes.text","r")
    encontrar = f.read()
    num = encontrar.count("manuelarte")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta manuel já tem {num} gosto(s).")

#CLASSIFICAR manueldesporto
def gosto_manueldesporto():
    f = open("classificacoes.text","a")
    f.write("manueldesporto" + "\n")
    
    f= open("classificacoes.text","r")
    encontrar = f.read()
    num = encontrar.count("manueldesporto")

    messagebox.showinfo("Sucesso!",f"A sua classificação foi adicionada com sucesso! Esta manuel já tem {num} gosto(s).")

def ordenar_gostos():

    f= open("classificacoes.text","r")
    encontrar = f.read()
    manuelnatureza = encontrar.count("manuelnatureza")
    manuelcarros = encontrar.count("manuelcarros")
    manuelarte = encontrar.count("manuelarte")
    manueldesporto = encontrar.count("manueldesporto")

    p_manuelnatureza = False
    p_manuelcarros = False
    p_manuelarte = False
    p_manueldesporto = False

    #PRIMEIRA POSIÇÃO
    if manuelnatureza != 0 or manuelcarros != 0 or manuelarte != 0 or manueldesporto != 0:
        if manuelnatureza > manuelcarros and manuelnatureza > manuelarte and manuelnatureza > manueldesporto:
            button_manuelnatureza.place(x=55,y=90)
            p_manuelnatureza = True
        elif manuelcarros > manuelnatureza and manuelcarros > manuelarte and manuelcarros > manueldesporto:
            button_manuelcarros.place(x=55,y=90)
            p_manuelcarros = True
        elif manuelarte > manuelnatureza and manuelarte > manuelcarros and manuelarte > manueldesporto:
            button_manuelarte.place(x=55,y=90)
            p_manuelarte = True
        elif manueldesporto > manuelnatureza and manueldesporto > manuelcarros and manueldesporto > manuelarte:
            button_manueldesporto.place(x=55,y=90)
            p_manueldesporto = True

    s_manuelnatureza = False
    s_manuelcarros = False
    s_manuelarte = False
    s_manueldesporto = False

    #SEGUNDA POSIÇÃO
    if p_manuelnatureza == True:
        if manuelcarros > manuelarte and manuelcarros > manueldesporto:
            button_manuelcarros.place(x=450,y=90)
            s_manuelcarros = True
        elif manuelarte > manuelcarros and manuelarte > manueldesporto:
            button_manuelarte.place(x=450,y=90)
            s_manuelarte = True
        elif manueldesporto > manuelcarros and manueldesporto > manuelarte:
            button_manueldesporto.place(x=450,y=90)
            s_manueldesporto = True
    elif p_manuelcarros == True:
        if manuelnatureza > manuelarte and manuelnatureza > manueldesporto:
            button_manuelnatureza.place(x=450,y=90)
            s_manuelnatureza = True
        elif manuelarte > manuelnatureza and manuelarte > manueldesporto:
            button_manuelarte.place(x=450,y=90)
            s_manuelarte = True
        elif manueldesporto > manuelnatureza and manueldesporto > manuelarte:
            button_manueldesporto.place(x=450,y=90)
            s_manueldesporto = True
    elif p_manuelarte == True:
        if manuelnatureza > manuelcarros and manuelnatureza > manueldesporto:
            button_manuelnatureza.place(x=450,y=90)
            s_manuelnatureza = True
        elif manuelcarros > manuelnatureza and manuelcarros > manueldesporto:
            button_manuelcarros.place(x=450,y=90)
            s_manuelcarros = True
        elif manueldesporto > manuelnatureza and manueldesporto > manuelcarros:
            button_manueldesporto.place(x=450,y=90)
            s_manueldesporto = True
    elif p_manueldesporto == True:
        if manuelnatureza > manuelcarros and manuelnatureza > manuelarte:
            button_manuelnatureza.place(x=450,y=90)
            s_manuelnatureza = True
        elif manuelcarros > manuelnatureza and manuelcarros > manuelarte:
            button_manuelcarros.place(x=450,y=90)
            s_manuelcarros = True
        elif manuelarte > manuelnatureza and manuelarte > manuelcarros:
            button_manuelarte.place(x=450,y=90)
            s_manuelarte = True
    
    #TERCEIRA E QUARTA POSIÇÃO
    if s_manuelnatureza == True:
        if p_manuelcarros == True:
            if manuelarte > manueldesporto:
                button_manuelarte.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manueldesporto.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
        elif p_manuelarte == True:
            if manuelcarros > manueldesporto:
                button_manuelcarros.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manueldesporto.place(x=55,y=310)
                button_manuelcarros.place(x=450,y=310)
        elif p_manueldesporto == True:
            if manuelcarros > manuelarte:
                button_manuelcarros.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
            else:
                button_manuelcarros.place(x=450,y=310)
                button_manuelarte.place(x=55,y=310)
    elif s_manuelcarros == True:
        if p_manuelnatureza == True:
            if manuelarte > manueldesporto:
                button_manuelarte.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manueldesporto.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
        elif p_manuelarte == True:
            if manuelnatureza > manueldesporto:
                button_manuelnatureza.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manuelnatureza.place(x=450,y=310)
                button_manueldesporto.place(x=55,y=310)
        elif p_manueldesporto == True:
            if manuelnatureza > manuelarte:
                button_manuelnatureza.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
            else:
                button_manuelarte.place(x=55,y=310)
                button_manuelnatureza.place(x=450,y=310)
    elif s_manuelarte == True:
        if p_manuelnatureza == True:
            if manuelcarros > manueldesporto:
                button_manuelcarros.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manueldesporto.place(x=55,y=310)
                button_manuelcarros.place(x=450,y=310)
        elif p_manuelcarros == True:
            if manuelnatureza > manueldesporto:
                button_manuelnatureza.place(x=55,y=310)
                button_manueldesporto.place(x=450,y=310)
            else:
                button_manuelnatureza.place(x=450,y=310)
                button_manueldesporto.place(x=55,y=310)
        elif p_manueldesporto == True:
            if manuelnatureza > manuelcarros:
                button_manuelnatureza.place(x=55,y=310)
                button_manuelcarros.place(x=450,y=310)
            else:
                button_manuelnatureza.place(x=450,y=310)
                button_manuelcarros.place(x=55,y=310)
    elif s_manueldesporto == True:
        if p_manuelnatureza == True:
            if manuelcarros > manuelarte:
                button_manuelcarros.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
            else:
                button_manuelcarros.place(x=450,y=310)
                button_manuelarte.place(x=55,y=310)
        elif p_manuelcarros == True:
            if manuelnatureza > manuelarte:
                button_manuelnatureza.place(x=55,y=310)
                button_manuelarte.place(x=450,y=310)
            else:
                button_manuelnatureza.place(x=450,y=310)
                button_manuelarte.place(x=55,y=310)
        elif p_manuelarte == True:
            if manuelnatureza > manuelcarros:
                button_manuelnatureza.place(x=55,y=310)
                button_manuelcarros.place(x=450,y=310)
            else:
                button_manuelnatureza.place(x=450,y=310)
                button_manuelcarros.place(x=55,y=310)

#BOTÕES
button_gosto_manuelnatureza=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=6,height=1, command = gosto_manuelnatureza)
button_gosto_manuelcarros=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_manuelcarros)
button_gosto_manuelarte=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_manuelarte)
button_gosto_manueldesporto=Button(window, text="Gosto",fg="green", font = ("Calibri bold", 12),width=5,height=1, command = gosto_manueldesporto)

#endregion

#region GESTÃO DE CATEGORIAS

#CRIAÇÃO DOS CHECK BUTTONS COMO VARIÁVEIS
chk_g = IntVar()    #carlos E ROTEIROS
chk_g.set(1)
chk_m = IntVar()    #dora
chk_m.set(1)
chk_c = IntVar()    #cristina
chk_c.set(1)
chk_p = IntVar()    #manuel
chk_p.set(1)
chk_r = IntVar()    #rui
chk_t = IntVar()    #angela E OUTDOORS

def escolha_categorias():

    #CRIAÇÃO DE UMA NOVA JANELA
    JanEscolha = Toplevel(window)
    JanEscolha.title("Escolha de Categorias")

    #DIMENSIONAR E CENTRAR A JANELA
    w = 450
    h = 230
    ws = JanEscolha.winfo_screenwidth()
    hs = JanEscolha.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    JanEscolha.geometry('%dx%d+%d+%d' % (w, h, x, y))

    #TÍTULO DA PÁGINA
    label_escolha = Label(JanEscolha, text="Escolha as 4 Categorias que deseja:",font=("Calibri 11 bold"),width=40,height=1)
    label_escolha.place(x=225,y=25,anchor=CENTER)

    #CRIAÇÃO DOS CHECK BUTTONS
    chk_carlos = Checkbutton(JanEscolha, text="carlos e Roteiros", variable = chk_g)
    chk_dora = Checkbutton(JanEscolha, text="dora", variable = chk_m)
    chk_cristina = Checkbutton(JanEscolha, text="cristina", variable = chk_c)
    chk_manuel = Checkbutton(JanEscolha, text="manuel", variable = chk_p)
    chk_rui = Checkbutton(JanEscolha, text="rui", variable = chk_r)
    chk_angela = Checkbutton(JanEscolha, text="angela e Outdoors", variable = chk_t)

    #POSICIONAMENTO DOS CHECK BUTTONS
    chk_carlos.place(x=90, y=50)
    chk_dora.place(x=90,y=70)
    chk_cristina.place(x=90,y=90)
    chk_manuel.place(x=250,y=50)
    chk_rui.place(x=250,y=70)
    chk_angela.place(x=250,y=90)

    #BOTÃO DE CONFIRMAR A ESCOLHA 
    button_confirmar=Button(JanEscolha,text="Confirmar",bg="green",font = ("Calibri 12 bold"),fg="white",width=10,height=1,command=WindowAppAdmin)
    button_confirmar.place(x=225,y=190,anchor=CENTER)

#endregion

loginWindow()
window.mainloop()