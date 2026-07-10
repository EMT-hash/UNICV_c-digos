
import tkinter as tk
import Back_end as bk
from datetime import date


janela = tk.Tk()
janela.geometry('400x400')  
janela.title('StoreFlow')
janela.configure(bg="#141314" )
janela.iconbitmap('carrinho-carrinho.ico')


def cadastro():
    cad.forget()
    login.forget()
    info.place_forget()

    text1.config(
text='Cadastro',
font=('arial',22,'bold'))
    
    text2 = tk.Label(janela,
text='Preencha com suas informações',
background='#141314',
foreground="#FFFFFF",
font=('arial',10,'bold'))
    text2.place(x=25,y=60)
    bk.widgets.append(text2)


    textnome = tk.Label(janela,
text='Nome',
background='#141314',
foreground="#FFFFFF",
font=('arial',10))
    textnome.place(x=25,y=90)
    bk.widgets.append(textnome)
    
    nome = tk.Entry(janela,
background='#141314',
foreground="#FFFFFF",
width=15,
font=('arial',9))
    nome.place(x=25,y=115)
    bk.widgets.append(nome)


    textsobrenome = tk.Label(janela,
text='Sobrenome',
background='#141314',
foreground="#FFFFFF",
font=('arial',10,))
    textsobrenome.place(x=150,y=90)
    bk.widgets.append(textsobrenome)

    sobrenome = tk.Entry(janela,                         
bg='#141314',
fg="#FFFFFF",
font=('arial',9))
    sobrenome.place(x=150,y=115)
    bk.widgets.append(sobrenome)
    
    textcpf =tk.Label(janela,
text='CPF',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
    textcpf.place(x=25,y=150)                        
    bk.widgets.append(textcpf) 

    cpf = tk.Entry(janela,
bg='#141314',
fg="#FFFFFF",
width=25,
font=('arial',9))
    cpf.place(x=25,y=170)
    bk.widgets.append(cpf)


    textidade = tk.Label(janela,
text='Idade',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
    textidade.place(x=230,y=150)
    bk.widgets.append(textidade)

    idade = tk.Entry(janela,
bg='#141314',
fg="#FFFFFF",
width=9,
font=('arial',9))
    idade.place(x=230,y=170)
    bk.widgets.append(idade)                     
                     

    textemail = tk.Label(janela,
text='Email',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
    textemail.place(x=25,y=195)                        
    bk.widgets.append(textemail)

    email = tk.Entry(janela,
bg='#141314',
fg="#FFFFFF",
width=35,
font=('arial',9))
    email.place(x=25,y=220)
    bk.widgets.append(email)


    textuser = tk.Label(janela,
text='Usuário',
bg='#141314',
fg="#FFFFFF",                        
font=('arial',10))
    textuser.place(x=25,y=245)                        
    bk.widgets.append(textuser)

    user = tk.Entry(janela,
bg='#141314',
fg="#FFFFFF",
font=('arial',9))
    user.place(x=25,y=270)
    bk.widgets.append(user)

    textsenha = tk.Label(janela,
text='Senha',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
    textsenha.place(x=200,y=245)
    bk.widgets.append(textsenha)

    senha =tk.Entry(janela,
bg='#141314',
fg="#FFFFFF",
font=('arial',9))
    senha.place(x=200,y=269)
    bk.widgets.append(senha)                          
                         
    def cadastrar():
        bk.adicionar(nome.get(),sobrenome.get(),cpf.get(),idade.get(),user.get(),email.get(),senha.get())         

        textconfir.config(
text='Cadastro realizado com sucesso',            
bg='#141314',
fg="#FFFFFF", 
font=('arial',9))
        textconfir.after(5000, textconfir.place_forget)
        
    
        

    cadtrar = tk.Button(janela,
text='Cadastrar',
command=cadastrar,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',12,'bold'))                        
    cadtrar.place(x=150,y=320)
    bk.widgets.append(cadtrar)
                  
    textconfir = tk.Label(janela,
text='',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
    textconfir.place(x=100,y=292)
    bk.widgets.append(textconfir)                          


def logar():
    cad.forget()
    login.forget()
    info.place_forget()

    text1.config(
text='Acesse sua Conta',
background="#141314",
foreground="#FFFFFF",
font=('arial black',20))

    text_login_user = tk.Label(janela,
text='Usuário',
background='#141314',
foreground="#FFFFFF",
font=('arial',15))                         
    text_login_user.place(x=165,y=80)
    bk.widgets.append(text_login_user)

    login_user = tk.Entry(janela,
background='#141314',
foreground="#FFFFFF",
width=20,
font=('arial',9))
    login_user.place(x=130,y=110)
    bk.widgets.append(login_user)                                                
                         

    text_login_senha = tk.Label(janela,
text='Senha',
background='#141314',
foreground="#FFFFFF",
font=('arial',15))                         
    text_login_senha.place(x=165,y=145)
    bk.widgets.append(text_login_senha)

    login_senha = tk.Entry(janela,
background='#141314',
foreground="#FFFFFF",
width=20,
font=('arial',9))
    login_senha.place(x=130,y=180)   
    bk.widgets.append(login_senha)

    textlogin = tk.Label(janela,
text='',
bg='#141314',
fg="#FFFFFF", 
font=('arial',9))
    textlogin.place(x=150,y=205)
    bk.widgets.append(textlogin)                         

    client_id = None                         
    def acessar():
        nonlocal client_id
        client_id = bk.login(login_user.get(),login_senha.get(),textlogin)
        if client_id is not None:
            text_login_user.place_forget()
            login_user.place_forget()

            text_login_senha.place_forget()
            login_senha.place_forget()

            acesso.place_forget()
            textlogin.place_forget()


            text1.config(
text=f'Seja Bem-Vindo Novamente \n{login_user.get()} \nEscola sua ação',
background="#141314",   
foreground="#FFFFFF",
font=('arial black',17))

            def compra():
                comprar.forget()
                carrinho.forget()

                text1.config(text='Produtos Disponiveis:',background="#141314",   
foreground="#FFFFFF",
font=('arial black',20))


                nome_prod_text = tk.Label(janela,text='Produto',width=6,bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                nome_prod_text.place(x=140,y=65)
                bk.widgets.append(nome_prod_text)

                nome_prod = tk.Text(janela,
                width=10,height=1,bg='#141314',fg="#FFFFFF",font=('arial',18,'bold'))
                nome_prod.place(x=100,y=90)
                bk.widgets.append(nome_prod)



                preco_prod_text = tk.Label(janela,text='Preço',width=5,height=1,bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                preco_prod_text.place(x=260,y=65)
                bk.widgets.append(preco_prod_text)

                preco_prod = tk.Text(janela,width=5,height=1,bg='#141314',fg="#FFFFFF",font=('arial',18,'bold'))
                preco_prod.place(x=250,y=90)
                bk.widgets.append(preco_prod)

                                


                indice = 0
                indice_tupla = 0
                

                name_prod = bk.prod_info() #produtos
                produto_id = name_prod[indice_tupla][0]

                nome_prod.insert(tk.END,name_prod[indice][1])
                nome_prod.config(state='disable')

                preco_prod.insert('1.0',name_prod[indice][2])



                quantidadetxt = tk.Label(janela,text='Quantidade',bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                quantidadetxt.place(x=155,y=127)
                bk.widgets.append(quantidadetxt)

                quantidade = tk.Text(janela,width=5,height=1,bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                quantidade.place(x=175,y=150)
                bk.widgets.append(quantidade)
                

                qtd = 1

                quantidade.insert(tk.END,qtd)
                quantidade.config(state='disabled')

                def proximoqtd():
                    nonlocal quantidade
                    nonlocal qtd

                    quantidade.config(state='normal')
                    qtd +=1
                    
                    quantidade.delete('1.0',tk.END)
                    quantidade.insert(tk.END,qtd)

                    quantidade.config(state='disable')   
                    


                seguinteqtd =tk.Button(janela,text='>',command=proximoqtd,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',7,'bold'))
                seguinteqtd.place(x=220,y=150) 
                bk.widgets.append(seguinteqtd)

                def voltarqtd():
                    nonlocal quantidade
                    nonlocal qtd

                    quantidade.config(state='normal')
                    qtd -=1

                    if qtd >= 1:
                        quantidade.delete('1.0',tk.END)
                        quantidade.insert(tk.END,qtd)

                        quantidade.config(state='disable')

                    else:
                        qtd = 1
                        quantidade.delete('1.0',tk.END)
                        quantidade.insert(tk.END,qtd)
                        quantidade.config(state='disabled')                      



                anteriorqtd =tk.Button(janela,text='<',command=voltarqtd,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',7,'bold'))
                anteriorqtd.place(x=155,y=150)
                bk.widgets.append(anteriorqtd)  

                descricao = tk.Label(janela,text='Descrição',bg='#141314',fg="#FFFFFF",font=('arial',8,'bold')) 
                descricao.place(x=170,y=170)        
                bk.widgets.append(descricao)

                desc = tk.Text(janela,width=50,height=5,bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                desc.place(x=25,y=190)
                bk.widgets.append(desc)
                
                
                desc.insert(tk.END,name_prod[indice][4])
                desc.config(state='disable')


                def proximo():
                    nonlocal indice_tupla
                    nonlocal indice
                    nonlocal name_prod
                    nonlocal desc
                    nonlocal preco_prod

                    produtos = []
                    for produto in name_prod:
                        produtos.append(produto[1])
                    

                    
                    indice += 1
                    indice_tupla += 1

                    if indice < len(produtos):
                        nome_prod.config(state='normal')
                        nome_prod.delete('1.0',tk.END)
                        nome_prod.insert(tk.END,name_prod[indice][1])
                        nome_prod.config(state='disable')

                        desc.config(state='normal')
                        desc.delete('1.0',tk.END)
                        desc.insert(tk.END,name_prod[indice][4])
                        desc.config(state='disable')

                        preco_prod.delete('1.0',tk.END)
                        preco_prod.insert(tk.END,name_prod[indice][2])


                    else:
                        nome_prod.config(state='normal')
                        indice = 0
                        indice_tupla = 0
                        nome_prod.delete('1.0',tk.END)
                        nome_prod.insert(tk.END,name_prod[indice][1])
                        nome_prod.config(state='disable')

                        desc.config(state='normal')
                        desc.delete('1.0',tk.END)
                        desc.insert(tk.END,name_prod[indice][4])
                        desc.config(state='disable')

                        preco_prod.delete('1.0',tk.END)
                        preco_prod.insert(tk.END,name_prod[indice][2])

                        
                seguinte = tk.Button(janela,text='>',command=proximo,
background="#4A3278",
foreground="#FFFFFF",
width=5,
font=('arial',12,'bold'))
                seguinte.place(x=300,y=300)
                bk.widgets.append(seguinte)


                def Voltar():
                        nonlocal indice
                        nonlocal indice_tupla
                        nonlocal name_prod # produtos
                        nonlocal nome_prod # texto
                        nonlocal desc



                        indice -= 1
                        indice_tupla -= 1

                        if indice >= 0:
                            nome_prod.config(state='normal') 
                            nome_prod.delete('1.0',tk.END)
                            nome_prod.insert(tk.END,name_prod[indice][1])
                            nome_prod.config(state='disable')

                            desc.config(state='normal')
                            desc.delete('1.0',tk.END)
                            desc.insert(tk.END,name_prod[indice][4])
                            desc.config(state='disable') 

                            preco_prod.delete('1.0',tk.END)
                            preco_prod.insert(tk.END,name_prod[indice][2])                           


                        else:
                            nome_prod.config(state='normal')
                            indice = 0
                            indice_tupla = 0
                            nome_prod.delete('1.0',tk.END)
                            nome_prod.insert(tk.END,name_prod[indice][1])                            
                            nome_prod.config(state='disable')

                            desc.config(state='normal')
                            desc.delete('1.0',tk.END)
                            desc.insert(tk.END,name_prod[indice][4])
                            desc.config(state='disable')

                            preco_prod.delete('1.0',tk.END)
                            preco_prod.insert(tk.END,name_prod[indice][2])                             


                anterior = tk.Button(janela,text='<',command=Voltar,
background="#4A3278",
foreground="#FFFFFF",
width=5,
font=('arial',12,'bold'))
                anterior.place(x=50,y=300)
                bk.widgets.append(anterior)

                registrotext = tk.Label(janela,text='',
bg='#141314',
fg="#FFFFFF", 
font=('arial',10))
                registrotext.place(x=120,y=345)
                bk.widgets.append(registrotext)
               
                data_compra = date.today()
                def compra_registrada():
                    nonlocal indice
                    nonlocal name_prod
                    nonlocal client_id
                    nonlocal produto_id
                    nonlocal registrotext
                    
                    total = name_prod[indice][2] * qtd

                    registro = bk.registrar_compra(client_id,produto_id,qtd,name_prod,indice,total,registrotext,data_compra)


                     




                confir_compra = tk.Button(janela,
text='Comprar',
width=15,
command=compra_registrada,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',12,'bold'))
                confir_compra.place(x=125,y=300)
                bk.widgets.append(confir_compra)


            comprar = tk.Button(janela,
text='Comprar',
width=12,
command=compra,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',14,'bold'))
            comprar.pack(pady=20)
            bk.widgets.append(comprar)

            def ver_carinho():
                comprar.forget()
                carrinho.forget()
                
                text1.config(text='Suas Compras',font=('arial',25,'bold'))

                nonlocal client_id
                lista_carrinho = bk.consultar_carinho(client_id)

                carrinho_text = tk.Text(janela,width=50,height=14,bg='#141314',fg="#FFFFFF",font=('arial',10,'bold'))
                carrinho_text.place(x=25,y=90)
                bk.widgets.append(carrinho_text)

                for num,(produto,quantidade,valor_unitario,total) in enumerate(lista_carrinho,start=1):
                    carrinho_text.insert(tk.END,f"""
Compra Nº: {num}
Produto:{produto}
Quantidade:{quantidade}
Preço Unitário:{valor_unitario}
Valor Total:{total}
\n
""")
                        




            carrinho = tk.Button(janela,
text='Ver Carrinho',
width=12,
command=ver_carinho,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',14,'bold'))
            carrinho.pack(pady=25)
            bk.widgets.append(carrinho)



    acesso = tk.Button(janela,
text='Login',
command=acessar,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',12,'bold'))
    acesso.place(x=170,y=230)
    bk.widgets.append(acesso)


def infos():
    cad.forget()
    login.forget()

    text1.config(
text='Informações',
background="#141314",
foreground="#FFFFFF",
font=('arial black',20))



    textinfo = tk.Text(janela,width=35,height=15,bg="#141314",foreground="#FFFFFF",font=('arial',12))
    textinfo.place(x=30,y=70)
    bk.widgets.append(textinfo)

    scroll = tk.Scrollbar(janela)
    scroll.place(x=350,y=70,width=20,height=275)
    bk.widgets.append(scroll)

    textinfo.config(yscrollcommand=scroll.set) 
    scroll.config(command=textinfo.yview)                  

    textinfo.insert(tk.END,
"""
    Este é o projeto que chamei de StoreFlow.
Nele reuni um pouco de tudo o que aprendi 
nos últimos meses estudando programação em Python.
                    
    Mesmo sendo um projeto simples foi um projeto que eu gostei de fazer e foi oque mais eu pude perceber minha evolução.
                    
    Se você tiver alguma dica, sugestão ou 
feedback, vou ficar muito feliz em receber. 
É só me chamar no Discord: g_u_a_r_a_n_a.

Sobre o projeto

    O StoreFlow é um projeto que simula o funcionamento de uma loja virtual. Nele é possível realizar o cadastro de usuários, fazer login e efetuar compras, que ficam vinculadas à conta do usuário.

    Como este projeto foi desenvolvido com foco nos meus estudos, algumas implementações não seguem os padrões utilizados em aplicações profissionais. Tenho ciência de que existem formas mais seguras e eficientes de armazenar e gerenciar essas informações, porém o objetivo principal foi colocar em prática os conhecimentos adquiridos durante meus estudos em Python.



 """)


def volta():
    for widget in bk.widgets:
        widget.destroy()
    bk.widgets.clear()

    text1.config(text='Bem vindo a StoreFlow',
font=('arial black',20))
    text1.pack(pady=20)                 
    cad.pack(pady=20)
    login.pack(pady=20)
    info.place(x=350,y=350)
    


text1 = tk.Label(janela,
text='Bem vindo a StoreFlow',
background="#141314",
foreground="#FFFFFF",
font=('arial black',20))
text1.pack(pady=20)



cad = tk.Button(
text='Cadastar',
width=13,
command=cadastro,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',14,'bold'))
cad.pack(pady=20)


login = tk.Button(janela,
text='Login',
width=13,
command=logar,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',14,'bold'))
login.pack(pady=20)


voltar = tk.Button(janela,
text='Voltar',
background="#4A3278",
foreground="#FFFFFF",
command=volta,                   
font=('arial',12,'bold'))                   
voltar.place(x=15,y=350)


info = tk.Button(janela,
text='info',
command=infos,
background="#4A3278",
foreground="#FFFFFF",
font=('arial',12,'bold'))                                  
info.place(x=350,y=350)




janela.mainloop()

