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
    
    def createMidia(self, midia):
        return self.db.execute_query('CREATE (m:Midia {nome:$nome, lancamento:$lancamento, criador:$criador, duracao:$duracao, genero:$genero}) return m',
                                     {'nome': midia['nome'], 'lancamento': midia['lancamento'], 'criador': midia['criador'], 'duracao': midia['duracao'], 'genero': midia['genero']})