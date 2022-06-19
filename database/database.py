from neo4j import GraphDatabase


class Graph:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            nodes = session.run(query, parameters)
            results = [record for record in nodes]
            for node in results:
                obj = {}
                key = list(node.data())[0]
                labels = list(node[key].labels)
                obj = node.data()[key]
                obj["labels"] = labels
                data.append(obj)
            return data
    
    def login(self, email, senha):
        
        aux = self.execute_query("match(n:Usuario where n.email = $email and n.senha = $senha) return n",
        {'email':email, 'senha':senha})
        if(aux.count>0):
            user = {aux[0]["nome"],
                    aux[0]["email"],
                    aux[0]["senha"],
                    aux[0]["data_de_nascimento"],
                    aux[0]["metodo_de_pagamento"],
                    aux[0]["dia_do_vencimento"],
                    aux[0]["cpf"]}
            if(aux[0]["labels"]=="Usuario"):
                return {user, "usuario"}
            elif(aux[0]["labels"]=="Admin"):
                return {user, "admin"}
        else:
            return False