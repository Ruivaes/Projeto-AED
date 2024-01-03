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
    
    labbel_utilizador.place(x = 30,y = 20)
    text_utilizador.place(x = 230,y = 22)

    #PLACE DA ENTRY EMAIL
    
    labbel_email.place(x = 30,y = 50)
    text_email.place(x = 230,y = 53)

    #PLACE DA ENTRE PASSWORD
    
    labbel_passe.place(x = 30,y = 80)
    text_passe.place(x = 230,y = 83)

    #PLACE DA ENTRY PARA CONFIRMAR PASSOWRD
    
    labbel_confirmarpasse.place(x = 30,y = 110)
    text_confirmarpasse.place(x = 230,y = 113)

    #PLACE DO BOTÃO CRIAR 
    
    button_criar.place(x = 240,y = 160)
    button_retornar.place(x = 70, y = 160)

    #APAGAR OS BOTÕES DE LOGIN E DE CRIAR CONTA
    
    button_login.place_forget()
    button_criarconta.place_forget()
