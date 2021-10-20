import mysql.connector
import random
import time
import datetime
print('Criando conexão')
conn = mysql.connector.connect(
    host='localhost',
    user='newuser',
    password='newuser',
    database='cursos')

#criando um cursor
c = conn.cursor()


#Função para criar tabela
def createTable():
    c.execute("create table if not exists produtos(id integer not null primary key auto_increment,"\
              "data datetime,nome varchar(40),valor decimal(15,2))")

def insertTable():
    c.execute("insert into produtos(data,nome,valor) values('2020-09-09','Teclado',90.00)" )
    conn.commit()
    

def insertDadosVar():
    novaData = datetime.datetime.now()
    novoProduto = 'Monitor'
    novoValor = random.randrange(10,200)
    c.execute("insert into produtos(data,nome,valor) values(%s,%s,%s)",(novaData,novoProduto,novoValor))
    #Para o banco de dados SQLITE
    #c.execute("insert into produtos(data,nome,valor) values(?,?,?)",(novaData,novoProduto,novoValor))
    
    conn.commit()
def insertDadosComSetencas(novaData,novoProduto,novoValor):
    sql = "insert into produtos(data,nome,valor) values(%s,%s,%s)"
    dados = (novaData,novoProduto,novoValor)
    c.execute(sql,dados)
    conn.commit()

def insertDadosComSetencasLista(lista):
    #Note: no python caso você queira inserir mais de um valor, voce pode passar
    #uma lista de tupĺas como paramâmetro e utilizar um cursor, como um for
    sql = "insert into produtos(data,nome,valor) values(%s,%s,%s)"
    for rec in lista:        
        c.execute(sql,rec)   
       

def listaTudo():
    c.execute("select * from produtos")
    for linha in c.fetchall():
        print(linha)
        
def listaPorValor():
    c.execute("select * from produtos where valor > 60.0")
    for linha in c.fetchall():
        print(linha)

def listaPorValorVar(valor):
    c.execute("select * from produtos where valor > %s" %(valor))
    for linha in c.fetchall():
        print(linha)
        
def listaPorValorIniNomeVar(nome,valor):
    c.execute("select nome,valor from produtos where nome like '%s%%' and "\
              "valor > %s" %(nome,valor))
    for linha in c.fetchall():
        print(linha)        
    
def listaPorValorAnyNomeVar(nome,valor):
    c.execute("select nome,valor from produtos where nome like '%%%s%%' and "\
              "valor > %s" %(nome,valor))
    for linha in c.fetchall():
        print(linha)        

def listaColuna():
    c.execute("select * from produtos where valor ")
    for linha in c.fetchall():
        print(linha[3])

def atualizaDados(codigo,novoProduto,novaData,novoValor):
    c.execute("update produtos set nome = %s, data = %s, valor = %s where id = %s",(novoProduto,novaData,novoValor,codigo))
    conn.commit()
    
def deletaDados(codigo):
    c.execute("delete from produtos where id = %s"  %codigo)
    conn.commit()    
    
#Criando a tabela
createTable()

#Insere tabela
insertTable()

#Insere tabela
insertDadosComSetencas('2019-08-09','Mouse',25.00)

#Insert com lista de tupla
lista = [('2020-01-09','Mouse sem fio',50.00),
         ('2020-01-09','Teclado sem fio',70.00)]
insertDadosComSetencasLista(lista)

#Dando um commit na inserção por lista. Não executar o commit junto com o insert    
conn.commit()

#Gerando valore e inserindo na tabela
for i in range(10):
   insertDadosVar()
   time.sleep(1)
   
listaTudo()
listaPorValor()
listaPorValorVar(100)
listaColuna()
listaPorValorIniNomeVar('T',60)
listaPorValorAnyNomeVar('T',60)

#update
atualizaDados(1,'Mouse','2019-08-09',25.50)

#deleta dados
deletaDados(1)

#Fechando a conexao. Como eu vou executar várias inserção, só fecho no fina
c.close()
conn.close()
   
#Construir gráficos à partir de banco de dados



