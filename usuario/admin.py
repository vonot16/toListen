from usuario.usuario import Usuario


class Admin(Usuario): 
    def __init__(self, nome, email, senha, data_de_nascimento, metodo_de_pagamento, dia_do_vencimento, cpf):
        super().__init__(nome, email, senha, data_de_nascimento, metodo_de_pagamento, dia_do_vencimento, cpf)