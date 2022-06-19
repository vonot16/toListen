from database.database import Graph
from usuario.admin import Admin
from usuario.usuario import Usuario

def welcome():
    print(f"Bem Vindo ao toListen!")
    menu()

def menuUser(user):
    print("Menu Usuario")

def menuAdmin(admin):
    print("Menu Admin")

def entrar():
    print("Email:", end=" ")
    email = input()
    print("Senha: ", end=" ")
    senha = input()
    obj = db.login(email,senha)
    if(obj!=False):
        if(obj["type"]=="admin"):
            adm = Admin(obj["nome"],obj["email"],obj["senha"],obj["nascimento"],obj["pagamento"],obj["vencimento"],obj["cpf"])
            menuAdmin(adm)
        else:
            user = Usuario(obj["nome"],obj["email"],obj["senha"],obj["nascimento"],obj["pagamento"],obj["vencimento"],obj["cpf"])
            menuUser(user)

def registrar():
    print("Tipo de Conta: 1 - Usuario | 2 - Administrador | 0 - Cancelar")
    type = input()
    if(type=="0"):
        menu()
    elif(type != "1" and type != "2"):
        print("Opção Invalida!")
        registrar()
    else:
        nome = input("Nome: ")
        email = input("Email: ")
        senha = input("Senha: ")
        nascimento = input("Data de Nascimento: ")
        pagamento = input("Método de Pagamento: ")
        vencimento = input("Dia do Vencimento: ")
        cpf = input("CPF: ")
        
        if(type=="1"):
            user = Usuario(nome,email,senha,nascimento,pagamento,vencimento,cpf)
            user.createUsuario()
        else:
            adm = Admin(nome,email,senha,nascimento,pagamento,vencimento,cpf)
            adm.createUsuario()
        print("Conta criada com sucesso!")
        menu()

def menu():
    print("1 - Entrar | 2 - Registrar | 0 - Sair")
    op = input()
    if(op=="1"):
        entrar()
    elif(op=="2"):
        registrar()
    elif(op=="0"):
        pass
    else:
        print("Opção Invalida!")
        menu()

db = Graph(uri='bolt://localhost:7687',
                        user='neo4j', password='bd2')

welcome()