from src.backend.api.database.connect import client

class DoadorController:
    def __init__(self):
        self.db = client['db'] # Conectando ao banco sangue
        self.colecao = self.db['doador'] # Selecionando a collection doadores

    # Projection necessário!!
    # O fastapi encrenca com o _id: ObjectID ...
    # TODO: Arranjar alguma forma de contornar isso futuramente.
    def findOne(self):
        item = self.colecao.find_one({}, {'_id':0,'idDoador':1,'nomDoador':1,"enderecoDoador.dscCidadeDoador": 1,"enderecoDoador.dscUFDoador": 1,'indTipoSangDoador': 1,'indFatoRhDoador': 1})
        print(item)
        return item