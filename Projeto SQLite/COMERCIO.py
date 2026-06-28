# teste git
import inquirer
import sqlite3
import os

conexao = sqlite3.connect('Database/Cadastro de Clientes.db')
cursor = conexao.cursor()


def comprar():
    os.system('cls')
    while True:

        opcao_compra = [inquirer.List('opcao_compra',
message='Escolha sua ação',
choices=['Produto','Voltar'])
        ]

        resposta_compra = inquirer.prompt(opcao_compra)

    
        match resposta_compra['opcao_compra']:
            case 'Produto':
                cursor.execute("""
                SELECT nome
                FROM Clientes          
                                """)
                peg_conta = cursor.fetchall()
                clientes = []

                for cliente in peg_conta:
                    clientes.append(cliente[0])

                os.system('cls')
                conta = [inquirer.List('esc_conta',
message='Escolha o Cliente para realizar a comprar',
choices=clientes
                    )]

                conta_cliente = inquirer.prompt(conta)

                cursor.execute(f"""
            SELECT id_cliente
            FROM Clientes
            WHERE nome = '{conta_cliente['esc_conta']}'                        
                                
                                """)
                id_cliente = cursor.fetchone()        

                
                cursor.execute("""
        Select nome
        FROM Produtos                             
                            """)
                prodt = cursor.fetchall()

                prod_list = []

                for prod in prodt:
                    prod_list.append(prod[0])
                
                os.system('cls')
                comprar = [inquirer.List('comprar_prod',
message='Escolha um Produto para comprar',
choices=prod_list
                )]
                esc_compra = inquirer.prompt(comprar)

                cursor.execute(f"""
SELECT id_produto
FROM Produtos
WHERE nome = '{esc_compra['comprar_prod']}'                                                      
                               """)
                id_prod = cursor.fetchone()


                cursor.execute(f"""
SELECT preço
FROM Produtos
WHERE id_produto = '{id_prod[0]}'                                
                               """)
                preco_prod = cursor.fetchone()                

                cursor.execute(f"""
SELECT quantidade
FROM Produtos
WHERE '{id_prod[0]}'                                  
                               """)
                
                prod_qtd = cursor.fetchone()
                

                valid_qtd = True
                while valid_qtd == True:
                    qtd = int(input('Quanto do produto deseja comprar?\n'))

                    if qtd > prod_qtd[0]:
                        print('Quantidade fora de Estoque')
                    else:
                        valid_qtd = False
                
                total_value = qtd * int(preco_prod[0])

                cursor.execute("""
INSERT INTO Vendas(id_cliente,id_produto,quantidade,valor_unitario,valor_total)   
VALUES(?,?,?,?,?)         
                               """,(
int(id_cliente[0]),
int(id_prod[0]),
qtd,
float(preco_prod[0]),
float(total_value)
                     )
)
                conexao.commit()

            case 'Voltar':
                break             


                



                


                









            case 'Voltar':
                break

def cadastrar():
    os.system('cls')

    while True:
        os.system('cls')

        cad_opcao = [inquirer.List("cad_escolha",
    message="oque Cadastrar",
    choices=["Cliente","Produto","voltar"]                             
                                )
        ]
        cad_resposta = inquirer.prompt(cad_opcao)
        match cad_resposta['cad_escolha']:
            case 'Cliente':
                cad_list = []
                while True:
                    cadastro_c = {
                        'cad_nome' : input('Digite o nome do Cliente:\n').upper(),
                        'cad_sobrenome' : input('Digite o sobrenome do Cliente:\n').upper(),
                        'cad_cpf' : input('Digite o CPF do Cliente:\n').upper()
                    }

                    cad_list.append(cadastro_c)
                    continuar_cad = input('Deseja adicionar mais Clientes?(S/N)')

                    if continuar_cad.upper() != 'S':
                        break
                for cad in cad_list:
                        cursor.execute("""
    INSERT INTO Clientes(nome,sobrenome,cpf)
    VALUES(?,?,?)                              
    """,
        (
        cad['cad_nome'],
        cad['cad_sobrenome'],
        cad['cad_cpf']
        )
                    )
                conexao.commit()
            
            case 'Produto':
                prod_list = []
                while True:
                    cad_prod = {
                        'nome_prod' : input('Digite o nome do Produto:\n').upper(),
                        'preco_prod' : input('Digite o preço do Produto:\n').upper(),
                        'qnt_prod' : input('Digite a quantidade do Produto:\n').upper()
                    }
                    prod_list.append(cad_prod)

                    continuar_cad_prod = input('Deseja cadastrar mais produtos?(S/N)')
                    if continuar_cad_prod.upper() != 'S':
                        break

                for prod in prod_list:
                        cursor.execute("""
    INSERT INTO Produtos(nome,preço,quantidade)
    VALUES(?,?,?)                                   
    """,
    (
        prod['nome_prod'],
        int(prod['preco_prod']),
        int(prod['qnt_prod'])

    ))
                conexao.commit()     

            case  'voltar':
                break
                
def atualizar():
    os.system('cls')

    att_opcoes = [inquirer.List('atualizar',
        message='Escolha oque atualizar',
        choices=['Clientes','Produtos','Voltar']
                   )
                   ]
    att_resposta = inquirer.prompt(att_opcoes)
    try:
        cursor.execute(f"""
    PRAGMA table_info('{att_resposta['atualizar']}')                   
                    """)
        coluna_id = cursor.fetchall()
        
        id_collum_list = []
        for id_coluna in coluna_id:
            id_collum_list.append(id_coluna[1])

        cursor.execute(f"""
    SELECT {id_collum_list[1]}
    FROM {att_resposta['atualizar']}                    
    """)
        all_info = cursor.fetchall()
        lista_info = []
        for info in all_info:
            lista_info.append(info[0])

        os.system('cls')

        att_info = [inquirer.List('info_att',
    message='Escolha oque atualizar',
    choices=lista_info                             
    )
        ]
        choice = inquirer.prompt(att_info)

        cursor.execute(f"""
    SELECT {id_collum_list[0]}
    FROM {att_resposta['atualizar']}
    WHERE {id_collum_list[1]} = '{choice['info_att']}'
                    """)
        bd_id = cursor.fetchone()[0]

        lista_collum = []
        cursor.execute(f"""
    PRAGMA table_info('{att_resposta['atualizar']}')                   
    """)
        colunas = cursor.fetchall()
        for coluna in colunas:
            lista_collum.append(coluna[1])
        
        lista_collum.pop(0)
        
        collum_opcao = [inquirer.List('coluna',
    message='Escolha que tipo de informação atualizar',
    choices=lista_collum                                 
                                    )]
        collum_resposta = inquirer.prompt(collum_opcao)

        nova_info = input(f'Digite o(a) {collum_resposta['coluna']} atualizado(a)')

        cursor.execute(f"""
    UPDATE {att_resposta['atualizar']} 
    SET {collum_resposta['coluna']} = '{nova_info.upper()}'
    WHERE {id_collum_list[0]} = '{bd_id}'                    
                    
                    """)
    except:
        os.system('cls')
        while True:

            break
    
def ver():
    os.system('cls')
    cursor.execute("""
SELECT nome || ' ' || sobrenome AS nome_completo
FROM Clientes                  
                   """)
    name = cursor.fetchall()

    nomes = []

    for nome in name:
        nomes.append(nome[0])
    
    
    vizu_cliente = [inquirer.List('compra',
message='Escolha um Cliente para Vizualizar Compras',
choices=nomes                                   
                                    
                                    )]
    cliente_vizu = inquirer.prompt(vizu_cliente)

    nome , sobrenome = cliente_vizu['compra'].split(" ",1) 

    cursor.execute(f"""
SELECT id_cliente
FROM Clientes
WHERE nome = '{nome}'
AND sobrenome = '{sobrenome}'

                   """)

    cliente_id = cursor.fetchone()



    cursor.execute(f"""
Select Clientes.nome,Produtos.nome
FROM Vendas
INNER JOIN Clientes
ON Vendas.id_cliente = Clientes.id_cliente

INNER JOIN Produtos
ON Vendas.id_produto = Produtos.id_produto

WHERE Vendas.id_cliente = {cliente_id[0]}
           
                   """)
    cliente_produto = cursor.fetchall()
    
    for cliente,produto in cliente_produto:

        print(f"{cliente},{produto}")
    

    input("""Pressione 'Enter' para voltar""")

















    
while True:
    os.system('cls')
    opcao = [inquirer.List('escolha',
    message="Escolha a ação",
    choices=["Comprar","Cadastrar","Ver Compras","Atualizar","Apagar"]    
    )
    ]

    resposta = inquirer.prompt(opcao)

    match resposta['escolha']:
        case 'Comprar':
            comprar()

        case 'Cadastrar':
            cadastrar()

        case 'Atualizar':
            atualizar()

        case 'Ver Compras':
            ver()

        case 'Apagar':
            cursor.execute('DELETE FROM Clientes')
            cursor.execute('DELETE FROM Produtos')
            cursor.execute('DELETE FROM Vendas')

    conexao.commit()