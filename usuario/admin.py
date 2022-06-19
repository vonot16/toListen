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
        return self.db.execute_query('MATCH (u:Usuario {email:$nome}) SET u.dia_do_vencimento = $vencimento RETURN u',
                                     {'nome': usuario, 'vencimento': vencimento})

    def alteraEmailAdmin(self, usuario, email):
        return self.db.execute_query('MATCH (u:Usuario {email:$nome}) SET u.email = $email RETURN u',
                                     {'nome': usuario, 'email': email})

    def adminCancelaAssinatura(self, usuario):
        return self.db.execute_query('MATCH (u:Usuario {email:$nome}) SET u.premium = $premium RETURN u',
                                     {'nome': usuario, 'premium': False})

    def adminDeletaConta(self, usuario):
        return self.db.execute_query('MATCH (u:Usuario {email:$nome}) DELETE u',
                                     {'nome': usuario})
    def mostraDadosUsuario(self, usuario):
        aux =  self.db.execute_query('MATCH (u:Usuario {email:$nome}) return u',
                                     {'nome': usuario})
        if(len(aux)>0):
            user = {"nome":aux[0]["nome"],
                    "email":aux[0]["email"],
                    "senha":aux[0]["senha"],
                    "nascimento":aux[0]["data_de_nascimento"],
                    "pagamento":aux[0]["metodo_de_pagamento"],
                    "vencimento":aux[0]["dia_do_vencimento"],
                    "cpf":aux[0]["cpf"]}
            return user
        else:
            return False