import pymysql
import matplotlib.pyplot as plt

conexao = pymysql.connect (
    host = 'localhost', 
    user = 'root',
    password = '',
    db = 'loja'
);

cursor = conexao.cursor(); #Inicia a conexão com o banco de dados

cursor.execute("SELECT * FROM produtos");
produtos = cursor.fetchall(); #Guarda todos os resultados organizados

nomes = [coluna[1] for coluna in produtos];
quantidades = [coluna[2] for coluna in produtos];

plt.bar(nomes, quantidades);
plt.xlabel('Produtos');
plt.ylabel('Quantidades');
plt.title('Relação de produtos e quantidades');
plt.show();

