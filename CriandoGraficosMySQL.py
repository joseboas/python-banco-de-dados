import mysql.connector
import matplotlib.pyplot as plt
print('Criando conexão')
conn = mysql.connector.connect(
    host='localhost',
    user='newuser',
    password='newuser',
    database='cursos')

#criando um cursor
c = conn.cursor()

def criaGrafico():
    c.execute("select id, valor from produtos")
    ids= []
    valores = []
    dados = c.fetchall()
    for items in dados:
        ids.append(items[0])
        valores.append(items[1])
        
    plt.bar(ids,valores)
    plt.show()
    
criaGrafico()