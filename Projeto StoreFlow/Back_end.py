import sqlite3
conexao = sqlite3.connect('armazenamento.db')
cursor = conexao.cursor()
widgets = []

def adicionar(nome,sobrenome,cpf,idade,user,email,senha):
    cursor.execute("""
INSERT INTO Cliente_Usuario(nome,sobrenome,cpf,idade,nome_usuario,email,senha)
VALUES (?,?,?,?,?,?,?)""",

(nome,
sobrenome,
cpf,
idade,
user,
email,
senha 
 ))
    conexao.commit()


def login(login_user,login_senha,textlogin):

    cursor.execute("""
SELECT id_cliente
FROM Cliente_Usuario
WHERE nome_usuario = ?
AND senha = ? """,
(login_user,
 login_senha
 ))
    id_cliente = cursor.fetchone()

    if id_cliente is not None: 
        textlogin.config(
text='Logado com sucesso',
bg='#141314',
fg="#FFFFFF", 
font=('arial',9))
           
        return id_cliente[0]
        
    else:
        textlogin.config(
text='Acesso negado',
bg='#141314',
fg="#FFFFFF", 
font=('arial',9))


def prod_info():
    cursor.execute("""
SELECT * 
FROM produto                   
                              
                   """)
    
    prods = cursor.fetchall()
    return prods


def registrar_compra(client_id,produto_id,qtd,name_prod,indice,total,registrotext,data_compra):

    cursor.execute("""
INSERT INTO Compra(data_compra,preco_total,fk_Cliente_id_cliente)
VALUES(?,?,?)""",
(
data_compra,
total,
client_id
))
    
    id_compra = cursor.lastrowid

    cursor.execute("""
INSERT INTO item_compra(fk_Compra_id_compra,fk_Produto_id_produto,quantidade,preco_unitario,total)              
VALUES(?,?,?,?,?)""",
(
id_compra,
produto_id,
qtd,
name_prod[indice][2],
total
))
    conexao.commit()


def consultar_carinho(client_id):
    cursor.execute("""
SELECT Produto.nome,item_compra.quantidade,item_compra.preco_unitario,item_compra.total
FROM compra

INNER JOIN item_compra
ON Compra.id_compra = item_compra.fk_Compra_id_compra
                   
INNER JOIN Produto
ON item_compra.fk_Produto_id_produto = Produto.id_produto

WHERE Compra.fk_Cliente_id_cliente = ?               
                   """,(client_id,))
    lista = cursor.fetchall()
    return lista
    