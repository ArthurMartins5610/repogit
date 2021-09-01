from pymongo import collection

def get_database():
    from pymongo import MongoClient
    import pymongo

    #URL de conexao
    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.qqxjf.mongodb.net/mytestdb"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#Conexão com o cliente

    return client['soulcodeTeste2']#Base de dados


def cadastrarDocumento():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]   

    i = 1
    num = int(input("Quantos documentos você deseja criar? "))
    while(i<=num):
      n = int(input("Quantos campos terá seu documento: "))
      d = dict(input("Digite a chave e o valor separado por espaços: ").split() for _ in range(n))
      print(d)
      collection_name.insert_one(d)
      print("Documento inserido com sucesso!")
      i+=1

def cadastrarDocumento():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]

    i = 1
    num = int(input("Quantos documentos você deseja criar? "))
    while(i<=num):
        n = int(input("Quantos campos terá seu documento: "))
        d = dict(input("Digite a chave e o valor separado por espaços: ")).split()for _ in range(n))
        print(d)
        collection_name.insert_one(d)
        print("Documento inserido com sucesso!")
        i+=1

def mostrarDocumentos():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]
    detalhes_itens  = collection_name.find()
    for item in detalhes_itens:
       print(item)

def mostrarDocumentos():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)

def atualizarDocumento():
   dbname = get_database()
   collection_name = dbname["itens_soulcode"]
   temp = str(input("O que você deseja?\n1-Atualizar por ID: \n2-Atualizarpor campo: "))
   if (temp=="1"):
      id = str(input("Digite o ID a ser alterado: "))
      chave = str(input("Digite o campo a ser alterado: "))
      valor = str(input("Digite o novo valor: "))
      collection_name.update_one({"_id":id}, {"$set":{chave:valor}})
      print("Modificação realizada!")
      mostrarDocumentos()

   elif (temp=="2"):
      chave = str(input("Digite a chave a ser buscada: "))
      valor = str(input("Digite o valor a ser buscado: "))
      chave2 = str(input("Digite a chave a ser alterada: "))
      valor2 = str(input("Digite o novo valor: "))
      collection_name.update_many({chave:valor}, {"$set": {chave2:valor2}})
      print("Modificação realizada!")
      mostrarDocumentos()      

def atualizarDocumento():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]
    temp = str(input("O que você deseja? \n 1-Atualizar por ID: \n 2-Atualizar campo: "))
    if (temp =="1"):
        id = str(input("Digite o ID a ser alterado: "))
        chave = str(input("Digite o campo a ser alteardo: "))
        valor = str(input("Digite o novo valor: "))
        collection_name.update_one({"_id":id},{"$set":{chave:valor}})
        print("Modificação realizada!")
        mostrarDocumentos()

    elif(temp=="2"):
        chave = str(input("Digite a chave a ser buscada: "))
        valor = str(input("Digite o valor a ser buscado: "))
        chave2 = str(input("Digite a chave a ser alterada: "))
        valor2 = str(input("Digite o novo valor: "))
        collection_name.update_many({chave:valor},{"$set":{chave2:valor2}})
        print("Modificação realiazada!")
        mostrarDocumentos()


def deletarDocumentos():
   dbname = get_database()
   collection_name = dbname["itens_soulcode"]
   id = str(input("Qual o ID do documento que você deseja deletar? "))
   collection_name.delete_one({"_id": id})
   print("Documento excluído com sucesso!")
   detalhes_itens  = collection_name.find()
   for item in detalhes_itens:
      print(item)   


def deletarDocumentos():
    dbname = get_database()
    collection_name = dbname["itens_soulcode"]
    id = str(input("Qual o ID do documento que você deseja deletar? "))
    collection_name.delete_one({"_id":id})
    print("Documento excluído com sucesso!")
    detalhes_itens = collection_name.find()
    for item in detalhes_itens:
        print(item)


def deletarTudo():
   dbname = get_database()
   collection_name = dbname["itens_soulcode"]
   ver = str(input("Você realmente deseja excluir todos os documentos? S/N"))
   if (ver == 'S'):
      dbname = get_database()
      collection_name = dbname["itens_soulcode"]
      #collection_name.drop()#Deleta toda coleção.
      collection_name.delete_many({})#Deleta todos os documentos da coleção.
      print("Todos os documentos da sua coleção foram deletados!")
      detalhes_itens  = collection_name.find()
      for item in detalhes_itens:
         print(item)  
   elif (ver == 'N'):
      print("Nenhuma alteração foi realizada!")
#==========================================================      
#(1)Quantos livros possuem número de páginas 0? 
#===================================================================          
    dbname = get_database()
    collection_name = dbname ["exerCompass"]
    detalhes_itens = collection_name.count_documents({"pageCount":0})
    i=0
    for item in detalhes_itens:
        i+=1
        print(item) 

#========================================================
#(2)Quantos livros foram publicados?
#=========================================================
    dbname = get_database()
    collection_name = dbname ["exerCompass"]
    detalhes_itens = collection_name.distinct({"status":"PUBLISH"})
    i=0
    for item in detalhes_itens:
        i+=1
        print(item)
#==============================================================
#(3)Qual o título do livro, cujo ISBN é 1933988924? 
#==============================================================
    doc= collection_name.find_one({'isbn': '1933988924'})
    print(doc['title'])

    detalhes_itens = collection_name.find({"isbn":"1933988924"})
    for item in detalhes_itens:
        print(item['title'])
#==============================================================
#(4)Qual a descrição do livro Machine Learning in Action?
#===============================================================
    detalhes_itens = collection_name.find({"title":"Machine Learning in Action"})
    for item in detalhes_itens:
        print(item["shortDescription"])
#=================================================================
#(5)O Livro ArcGIS Web Development foi publicado?
#=====================================================================
    detalhes_itens = collection_name.find({"title":"ArcGIS Web Development"})#Não
    for item in detalhes_itens:
        print(item['status'])
#=========================================================================
#(6)Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade? 
#============================================================================
    detalhes_itens = collection_name.find({"title":"Secrets Javascript apt Ninja Pijamas"})
    for item in detalhes_itens:
        print(item['shortDescription'])
#==================================================================================
#(7)Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade? 
#===================================================================================
    doc = collection_name.find_one()({"title":"Secrets Javascript apt Ninja pBook upgarde"})
    try:
        print(doc['shortDescription'])
    except KeyError:
        print("Chave não encontrada")
#=============================================================================================
#(8)Quantas páginas possui o livro Jess in Action? 
#====================================================================================
    detalhes_itens = collection_name.find({"title":"less in Action"})
    for item in detalhes_itens:
        print(item["pageCount"])
    detalhes_itens = collection_name.find().limit(3)
    for item in detalhes_itens:
        print(item["title"])
#==============================================================================================
#(9)Qual o ID do livro, cujo ISBN é 1930110987? Ele é declarado ou setado pelo MongoDB?
#===================================================================================================
    detalhes_itens = collection_name.find({"isbn":"1930110987"})
    for item in detalhes_itens:
        print(item[])


    

