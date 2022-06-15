from database.database import Graph

class Usuario: 
    def __init__(self, nome, email, senha, data_de_nascimento, metodo_de_pagamento, dia_do_vencimento, cpf):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_de_nascimento = data_de_nascimento
        self.metodo_de_pagamento = metodo_de_pagamento
        self.dia_do_vencimento = dia_do_vencimento
        self.cpf = cpf
        self.db = Graph(uri='bolt://localhost:7687',
                        user='neo4j', password='bd2')

    def createUsuario(self):
        return self.db.execute_query('CREATE (u:Usuario {nome:$nome, email:$email, senha:$senha, data_de_nascimento:$data_de_nascimento, metodo_de_pagamento:$metodo_de_pagamento, dia_do_vencimento:$dia_do_vencimento, cpf:$cpf, premium:$premium}) return u',
                                     {'nome': self.nome, 'email':self.email, 'senha': self.senhavoc, 'data_de_nascimento': self.data_de_nascimento, 'metodo_de_pagamento': self.metodo_de_pagamento, 'dia_do_vencimento': self.dia_do_vencimento, 'cpf': self.cpf, 'premium': True})

    def acessaMidia(self, musica):
        return self.db.execute_query('MATCH (m:Midia {nome:$musica}) RETURN m',
                                     {'musica': musica})
    
    def mostraDados(self):
        return f"nome: {self.nome}, email: {self.email}, dia do vencimento: {self.dia_do_vencimento}, metodo de pagamento: {self.metodo_de_pagamento}"

    def alteraVencimento(self, vencimento):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.dia_do_vencimento = $vencimento RETURN u',
                                     {'nome': self.nome, 'dia do vencimento': vencimento})
    
    def alteraEmail(self, email):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.email = $email RETURN u',
                                     {'nome': self.nome, 'email': email})

    def alteraVencimento(self, senha):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.senha = $senha RETURN u',
                                     {'nome': self.nome, 'senha': senha})

    def deletaConta(self):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) DELETE u',
                                     {'nome': self.nome})

    def verificaPremium(self):
        return self.db.execute_query('MATCH u:Usuario {nome:$nome}) RETURN n.premium',
                                     {'nome': self.nome})

    def cancelaAssinatura(self):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.premium = $premium RETURN u',
                                     {'nome': self.nome, 'premium': False})

    def addMusicaFavorita(self, musica):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}), (m:Midia {nome:$musica}) CREATE (u)-[r:FAVORITA]->(m) RETURN r, u, m',
                                     {'nome': self.nome, 'musica': musica})

    def deletaFavorito(self, musica):
        return self.db.execute_query('MATCH (u:Usuario{nome: $nome})-[r:FAVORITA]->(m:Midia{nome:$musica}) DELETE r',
                                     {'nome': self.nome, 'musica': musica})

    def ouvirDepois(self, musica):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}), (m:Midia {nome:$musica}) CREATE (u)-[r:OUVIR_DEPOIS]->(m) RETURN r, u, m',
                                     {'nome': self.nome, 'musica': musica})                                                                                  

    def deletaOuvirDepois(self, musica):
        return self.db.execute_query('MATCH (u:Usuario{nome: $nome})-[r:OUVIR_DEPOIS]->(m:Midia{nome:$musica}) DELETE r',
                                     {'nome': self.nome, 'musica': musica})    

