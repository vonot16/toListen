from usuario.usuario import Usuario


class Admin(Usuario): 
    def __init__(self, nome, email, senha, data_de_nascimento, metodo_de_pagamento, dia_do_vencimento, cpf):
        super().__init__(nome, email, senha, data_de_nascimento, metodo_de_pagamento, dia_do_vencimento, cpf)
    
    def createUsuario(self):
        return self.db.execute_query('CREATE (a:Usuario:Admin {nome:$nome, email:$email, senha:$senha, data_de_nascimento:$data_de_nascimento, metodo_de_pagamento:$metodo_de_pagamento, dia_do_vencimento:$dia_do_vencimento, cpf:$cpf, premium:$premium}) return a',
                                     {'nome': self.nome, 'email':self.email, 'senha': self.senha, 'data_de_nascimento': self.data_de_nascimento, 'metodo_de_pagamento': self.metodo_de_pagamento, 'dia_do_vencimento': self.dia_do_vencimento, 'cpf': self.cpf, 'premium': True})

    def deletaMidia(self, midia):
        return self.db.execute_query('MATCH (m:Midia {nome:$nome}) DELETE m',
                                     {'nome': midia})

    def alteraVencimentoAdmin(self, usuario, vencimento):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.dia_do_vencimento = $vencimento RETURN u',
                                     {'nome': usuario.nome, 'dia do vencimento': vencimento})

    def alteraEmailAdmin(self, usuario, email):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.email = $email RETURN u',
                                     {'nome': usuario.nome, 'email': email})

    def adminCancelaAssinatura(self, usuario):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) SET u.premium = $premium RETURN u',
                                     {'nome': usuario.nome, 'premium': False})

    def adminDeletaConta(self, usuario):
        return self.db.execute_query('MATCH (u:Usuario {nome:$nome}) DELETE u',
                                     {'nome': usuario.nome})
                                                                          
                                     