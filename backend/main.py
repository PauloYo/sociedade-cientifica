from connect import client

db = client['db'] # Conectando ao banco sangue
colecao = db['doador'] # Selecionando a collection doadores

resultados = colecao.find_one({})
print(resultados)
for doc in resultados:
    print(doc)
