from database.database import Graph

class Midia:
    def __init__(self, nome, lancamento, criador, duracao, genero):
        self.nome = nome
        self.lancamento = lancamento
        self.criador = criador
        self.duracao = duracao
        self.genero = genero
        self.db = Graph(uri='bolt://localhost:7687',
                        user='neo4j', password='bd2')
    
    def createMidia(self):
        return self.db.execute_query('CREATE (m:Midia {nome:$nome, lancamento:$lancamento, criador:$criador, duracao:$duracao, genero:$genero}) return m',
                                     {'nome': self.nome, 'lancamento': self.lancamento, 'criador': self.criador, 'duracao': self.duracao, 'genero': self.genero})