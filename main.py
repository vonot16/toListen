from pprintpp import pprint as pp
from database.database import Graph


class toListen(object):
    def __init__(self):
        self.db = Graph(uri='bolt://localhost:7687',
                        user='neo4j', password='bd2')

    def createUsuario(self, usuario):
        return self.db.execute_query('CREATE (u:Usuario {nome:$nome, email:$email, senha:$senha, data_de_nascimento:$data_de_nascimento, metodo_de_pagamento:$metodo_de_pagamento, dia_do_vencimento:$dia_do_vencimento, cpf:$cpf, premium:$premium}) return u',
                                     {'nome': usuario['nome'], 'email': usuario['email'], 'senha': usuario['senha'], 'data_de_nascimento': usuario['data_de_nascimento'], 'metodo_de_pagamento': usuario['metodo_de_pagamento'], 'dia_do_vencimento': usuario['dia_do_vencimento'], 'cpf': usuario['cpf'], 'premium': usuario['premium']})

    def createMidia(self, midia):
        return self.db.execute_query('CREATE (m:Midia {nome:$nome, lancamento:$lancamento, criador:$criador, duracao:$duracao, genero:$genero}) return m',
                                     {'nome': midia['nome'], 'lancamento': midia['lancamento'], 'criador': midia['criador'], 'duracao': midia['duracao'], 'genero': midia['genero']})
