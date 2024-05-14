# Como podemos criar uma coleção usando o pymongo?
# Vamos criar uma coleção chamada "users" e inserir um documento nela.
# Para isso, precisamos criar uma instância do MongoClient e, em seguida, criar uma coleção e inserir um documento nela.
# Vamos ver como fazer isso.
# Importando o módulo pymongo
import pymongo
# Criando uma instância do MongoClient
client = pymongo.MongoClient("mongodb://localhost:27017/")
# Criando uma coleção
db = client["mydatabase"]
collection = db["users"]
# Inserindo um documento
user = {"name": "John", "address": "Highway 37"}
collection.insert_one(user)
# Imprimindo o id do documento
print(collection.find_one())
# O método insert_one() insere um documento na coleção. O documento é um dicionário que contém os campos e valores do documento.
# O método find_one() retorna o primeiro documento na coleção.
# O método find() retorna todos os documentos na coleção.
# O metodo keys() retorna todos os campos do documento.
# O método insert_many() insere vários documentos na coleção.
# O método delete_one() exclui o primeiro documento que corresponde à consulta.
# O método delete_many() exclui todos os documentos que correspondem à consulta.
# O método update_one() atualiza o primeiro documento que corresponde à consulta.
# O método update_many() atualiza todos os documentos que correspondem à consulta.
# O método limit() especifica o número de documentos a serem retornados.
# O método sort() especifica a ordem de classificação.
# O método count() retorna o número de documentos na coleção.
# O método drop() exclui a coleção.
# O método find() retorna todos os documentos na coleção.
# O método find() aceita um parâmetro de consulta que é usado para especificar um filtro.
# O método find() aceita um segundo parâmetro que é uma lista de campos para incluir ou excluir.
