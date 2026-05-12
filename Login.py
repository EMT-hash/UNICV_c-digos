# Primeira Interface Gráfica

from encodings.punycode import T
import tkinter as tk # tkint    er para interface gráfica

contas = [] # variavel lista de contas (cada conta é uma tupla imutavel)
widgets_tela = [] # widgets do tkinter (textos , campos e botões )

def criar(): # função para criar uma conta
    botao1.pack_forget() # esconder botão 1
    botao2.pack_forget() # esconder botão 2
    botao3.pack_forget() # esconder botão 3
    texto1.config(text="Crie Uma Conta") # muda o texto1 de "Bem-Vindo ao Teste de Sistema de Conta\nEscolha Oque Deseja Fazer" para "Crie Uma Conta"

    mgs_usuario = tk.Label(janela,text=
             "Usuario",
             font=("Arial",12,"bold")) # texto "Usuario" da janela
    mgs_usuario.pack() # exibir texto "Usuario"
    entry_user = tk.Entry(janela) # cria campo para digitar o usuario
    entry_user.pack() # exibir o campo para digitar o usuario
    widgets_tela.append(mgs_usuario) # adiciona a variavel do texto "Usuario" na variavel widgets_tela
    widgets_tela.append(entry_user) # adiciona a variavel para de campo para digitar o usuario na variavel widgets_tela


    mgs_senha = tk.Label(janela,
        text="Senha",
        font=("Arial",12,"bold")) # texto "Senha" da janela
    mgs_senha.pack() # exibi o texto "Senha"
    widgets_tela.append(mgs_senha) # adiciona a variavel do texto "Senha" na varialvel widgets_tela

    entry_senha = tk.Entry(janela) # cria campo para digitar senha
    entry_senha.pack() # exibir o campo para digitar a senha
    widgets_tela.append(entry_senha) # adiciona a variavel para de campo para digitar a senha na variavel widgets_tela


    def registar_conta(): # sub função para o botão de registrar conta
        dados = (
            entry_user.get(), # adquir oque foi digitado no campo usuario
            entry_senha.get() # adquir oque foi digitado no campo senha
            ) # varial trasforma em uma tupla imutavel       
        contas.append(dados) # adiciona o valor da variavel "dados" em "contas"
        confirmar_cadastro.config(text="Cadastro Realizado com Sucesso") # muda o texto "" 
    # sai da subfunção

    registrar = tk.Button(
        janela, text = "Registrar", # cria o botão de Registrar
        font=("Arial",12,"bold"),
        command= registar_conta) # função registrar_conta
    registrar.pack(pady=10) # exibi o botão Registar alterando um pouco sua posição com "pady=10"
    widgets_tela.append(registrar) # adiciona o botão "Registrar" em "widgets_tela"
    confirmar_cadastro = tk.Label(janela,
        text="") # texto "" importante para exibir o texto "Cadastro Realizado com Sucesso"
    confirmar_cadastro.pack() # exibir texto ""
    widgets_tela.append(confirmar_cadastro)  # adicionar texto " na variavel "widgets_tela"

def acessar(): # função para acessar uma conta
    botao1.pack_forget() # esconder botão 1
    botao2.pack_forget() # esconder botão 2
    botao3.pack_forget() # esconder botão 3

    texto1.config(text="Acesse sua Conta")
    txt_usuario = tk.Label(janela,
             text="Usuario",
             font=("Arial",12,"bold")) # cria o texto "Usuario"
    txt_usuario.pack() # exibi o texto "usuario"
    widgets_tela.append(txt_usuario) # adiciona a variavel do texto "usuario" para "widgets_tela"

    login_user = tk.Entry(janela) # cria campo para digitar usuario
    login_user.pack() # exibi o campo para digitar usuario
    widgets_tela.append(login_user) # adiciona a variavel do campo "usuario" para "widgets_tela"

    txt_senha = tk.Label(janela,
             text="Senha",
             font=("Arial",12,"bold")) # cria o texto "Senha"
    txt_senha.pack() # exibi o texto "Senha"
    widgets_tela.append(txt_senha) # adiciona a variavel do texto "Senha" para "widgets_tela"


    login_senha = tk.Entry(janela) # cria campo para digitar usuario
    login_senha.pack()  # exibi o campo para digitar senha
    widgets_tela.append(login_senha) # adiciona a variavel do campo "Senha" para "widgets_tela"


    def logar(): # sub função para o botão "Logar"

        if (login_user.get(),login_senha.get()) in contas: # verifica se a tupla "login_user" e "login_senha" estão na lista "contas"
            mensagem.config(text= "Logado Com Sucesso") # modifica o texto "" caso esteja em contas
        
        else:
            mensagem.config(text="Acesso Negado") # modifica o texto "" caso não esteja em contas
    
    mensagem = tk.Label(janela,
        text="") # cria texto ""
    mensagem.pack() # exibi o texto ""
    widgets_tela.append(mensagem) # adiciona o texto "" para a variavel "widgets_tela"

    login = tk.Button(janela, # cria o botão de "login"
        text="login",
        command=logar) # função logar
    login.pack() # exibi botão "login"
    widgets_tela.append(login) # adiciona o botão "login" para "widgets_tela"
 
def excluir(): # função para deletar uma conta
    botao1.pack_forget() # esconder botão 1
    botao2.pack_forget() # esconder botão 2
    botao3.pack_forget() # esconder botão 3

    texto1.config(text="Deletar Conta") # muda o "texto1" para "Deletar Conta"

    txt_excluir_user = tk.Label(janela,
        text= "Usuario",
        font=("Arial",12,"bold")) # cria o texto "Usuario"
    txt_excluir_user.pack() # exibi o texto "Usuario"
    widgets_tela.append(txt_excluir_user) # adiciona o a variavel "txt_excluir_user" para "widgets_tela"

    entry_usuario_excluir = tk.Entry(janela) # cria o campo para digitar usuario
    entry_usuario_excluir.pack() # exibi campo para digitar usuario
    widgets_tela.append(entry_usuario_excluir) # adiciona o a variavel "entry_usuario_excluir" para "widgets_tela"

    txt_excluir_senha = tk.Label(janela,
        text="Senha",
        font=("Arial",12,"bold")) # cria o texto "Senha"
    txt_excluir_senha.pack() # exibi o texto "Senha"
    widgets_tela.append(txt_excluir_senha) # adiciona o a variavel "txt_excluir_senha" para "widgets_tela"
    
    entry_senha_excluir = tk.Entry(janela) # cria campo para digitar senha
    entry_senha_excluir.pack() # exibi campo para digitar senha
    widgets_tela.append(entry_senha_excluir) # adiciona o a variavel "entry_senha_excluir" para "widgets_tela"

    def deletando(): # sub função para botao "Deletar"
        if (entry_usuario_excluir.get(),entry_senha_excluir.get()) in contas: # verifica se o usuario e senha digitados (tupla) nos campos está na lista de "contas" registradas
            dados_deletar = (entry_usuario_excluir.get(),entry_senha_excluir.get()) # armazena o usuario e senha digitados (tupla) em uma variavel chamada "dados_deletar"
            contas.remove(dados_deletar) # remove a tupla de dados da variavel "contas"
            confirmar_delete.config(text="Conta deletada com sucesso") # confirma conta deletada
        else:
            confirmar_delete.config(text="Conta não encontrada") # conta não deletada

    deletar = tk.Button(janela,
        text="Deletar",
        command=deletando,
        font=("Arial",12,"bold"))
    deletar.pack(pady=20)
    widgets_tela.append(deletar)
    confirmar_delete = tk.Label(janela,
        text="")
    confirmar_delete.pack()
    widgets_tela.append(confirmar_delete) 
    
def botao_voltar(): # função para voltar 

    for widget in widgets_tela: # percorre toda a lista de widgets_tela
        widget.destroy() # destroi cada widgets que estava em tela
    # fora do for
    widgets_tela.clear() # limpa a variavel "widgets_tela"

    texto1.config(
        text="Bem-Vindo ao Teste de Sistema de Conta\nEscolha Oque Deseja Fazer"
    ) # volta para o texto original

    botao1.pack() # exibi novamente o botao 1
    botao2.pack(pady=20) # exibi novamente o botao 2
    botao3.pack(pady=10) # exibi novamente o botao 3

janela = tk.Tk() # começa a janela
janela.geometry("400x400") # defini o tamanho da janela
janela.title('login') # título da janela


texto1 = tk.Label(janela,
    text="Bem-Vindo ao Teste de Sistema de Conta\nEscolha Oque Deseja Fazer",
    font=("Arial",12,"bold")) # criar texto inicial
texto1.pack(pady=20) # exibir texto inicial

botao1 = tk.Button(janela,
    text="Criar Conta",
    command=criar, # função cria
    font=("Arial",12,"bold")) # criar botão "Criar Conta"
botao1.pack() # exibir botao "Criar Conta"

botao2 = tk.Button(janela,
    text="Acessar Conta",
    command=acessar, # função acessar
    font=("Arial",12,"bold")) #cria botão "Acessar Conta"
botao2.pack(pady=20) # exibi o botão "Acessar Conta"


botao3 = tk.Button(janela,
    text="Excluir Conta",
    command=excluir, # função Excluir
    font=("Arial",12,"bold")) # cria o botão "Excluir Conta"
botao3.pack(pady=10) # exibi o botão "Criar Conta"

voltar = tk.Button(janela,
    text="Voltar",
    command=botao_voltar, # função "botao_voltar"
    font=("Arial",10,"bold")) # cria o botão "Voltar"
voltar.place(x=20,y=358) # defini posição / exibi botão "Voltar"


janela.mainloop() # loop principal para a janela da interface continuar rodando