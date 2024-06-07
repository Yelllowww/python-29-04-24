import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1')
print('Conexão:', conexao)
cursor = conexao.cursor()
sql = "CREATE DATABASE if not exists db_loja"
cursor.execute(sql)
cursor.close()
conexao.close()
print('\nConexão fechada.')
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_loja')
cursor = conexao.cursor()
print('Conexão:', conexao)

sql = '''CREATE TABLE if not exists tb_produto(
                idt INT NOT NULL AUTO_INCREMENT,
                nome VARCHAR(45) NOT NULL UNIQUE,
                preco DECIMAL(9,2) NOT NULL,
                dt_validade DATE NULL,
                PRIMARY KEY (idt))
      '''
cursor.execute(sql)
cursor.close()
conexao.close()
print('\nConexão fechada.')
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_loja')
cursor = conexao.cursor()
print('Conexão:', conexao)
insere_nome = input("Nome:")
insere_preco = input("Preço:")
insere_dt_validade = input("Data de validade:")
sql = f'''INSERT INTO tb_produto
            (nome,preco,dt_validade)
            VALUES ('{insere_nome}','{insere_preco}','{insere_dt_validade}')
       '''
cursor.execute(sql)
conexao.commit()
cursor.close()
conexao.close()
print('\nConexão fechada.')
import mysql.connector
conexao = mysql.connector.connect(user='root',
                                  password='',
                                  host='127.0.0.1',
                                  database='db_loja')
cursor = conexao.cursor()
print('Conexão:', conexao)
insere_nome = input("Nome do produto:")
sql = f'''SELECT * FROM tb_produto
            WHERE nome LIKE '%{insere_nome}%'
       '''
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)
cursor.close()
conexao.close()
print('Conexão fechada.')
