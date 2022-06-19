def welcome():
    print(f"Bem Vindo ao toListen!")
    menu()

def entrar():
    print(f"Entrar")

def registrar():
    print(f"Registrar")

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
        menu()
        
welcome()