import sqlite3
conexao = sqlite3.connect('armazenamento.db')
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO Produto(nome,preco,quantidade,descricao)
VALUES(
'Coca-Cola Original 2L',
11.99,
50,
'Refrigerante Coca-Cola Original de 2 litros, sabor tradicional, ideal para acompanhar refeições e confraternizações. Produto gaseificado, servido preferencialmente gelado.'               
)
""")
conexao.commit()