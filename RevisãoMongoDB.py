from pymongo import collection
def get_database():
    from pymongo import MongoClient
    import pymongo
    CONNECTION_STRING = "mongodb+srv://root:root@cluster0.xdig0.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)#Conexão com o cliente
    return client['exerCompass']#Base de dados
     
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
    #dbname = get_database()
    #c#ollection_name = dbname ["exerCompass"]
    #detalhes_itens = collection_name.distinct({"status":"PUBLISH"})
    #i=0
    #for item in detalhes_itens:
    #   i+=1
    #  print(item)
    #==============================================================
    #(3)Qual o título do livro, cujo ISBN é 1933988924? 
    #==============================================================
    #doc= collection_name.find_one({'isbn': '1933988924'})
    #print(doc['title'])
    #detalhes_itens = collection_name.find({"isbn":"1933988924"})
    #for item in detalhes_itens:
    #   print(item['title'])
    #==============================================================
    #(4)Qual a descrição do livro Machine Learning in Action?
    #===============================================================
    #detalhes_itens = collection_name.find({"title":"Machine Learning in Action"})
    #for item in detalhes_itens:
     #   print(item["shortDescription"])
    #=================================================================
    #(5)O Livro ArcGIS Web Development foi publicado?
    #=====================================================================
    #detalhes_itens = collection_name.find({"title":"ArcGIS Web Development"})#Não
    #for item in detalhes_itens:
    #    print(item['status'])
    #=========================================================================
    #(6)Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade? 
    #============================================================================
    #detalhes_itens = collection_name.find({"title":"Secrets Javascript apt Ninja Pijamas"})
    #for item in detalhes_itens:
    #    print(item['shortDescription'])
    #==================================================================================
    #(7)Qual a descrição do livro Secrets of the JavaScript Ninja pBook upgrade? 
    #===================================================================================
    #doc = collection_name.find_one()({"title":"Secrets Javascript apt Ninja pBook upgarde"})
    #try:
    #    print(doc['shortDescription'])
    #except KeyError:
    #    print("Chave não encontrada")
    #=============================================================================================
    #(8)Quantas páginas possui o livro Jess in Action? 
    #====================================================================================
    #detalhes_itens = collection_name.find({"title":"less in Action"})
    #for item in detalhes_itens:
    #    print(item["pageCount"])
    #detalhes_itens = collection_name.find().limit(3)
    #for item in detalhes_itens:
    #    print(item["title"])
    #==============================================================================================
    #(9)Qual o ID do livro, cujo ISBN é 1930110987? Ele é declarado ou setado pelo MongoDB?
    #===================================================================================================
    #detalhes_itens = collection_name.find({"isbn":"1930110987"})
    #for item in detalhes_itens:
    #    print(item[]) 