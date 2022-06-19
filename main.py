from msilib.schema import Media
from database.database import Graph
from midia.midia import Midia
from usuario.admin import Admin
from usuario.usuario import Usuario

def welcome():
    print(f"Bem Vindo ao toListen!")
    menu()

def sair():
    print("Obrigado por usar o toListen!")

def musicaFormatada(music):
    print("Nome: ",end=" ")
    print(music["nome"])
    print("Criador: ",end=" ")
    print(music["criador"])
    print("Genero: ",end=" ")
    print(music["genero"])
    print("Lançamento: ",end=" ")
    print(music["lancamento"])
    print("Duração: ",end=" ")
    print(music["duracao"])
    print("")

def menuMusica(user):
    print(" 1 - Ver Todas Musicas \n 2 - Buscar uma Musica \n 3 - Adicionar Musica Favoritos \n 4 - Remover Musica Favoritos \n 5 - Adicionar Musica Ouvir Depois \n 6 - Remover Musica Ouvir Depois \n 0 - Voltar")
    mop = input()
    if(mop=="1"):
        for music in db.getAllMusics():
            musicaFormatada(music)
        menuMusica(user)
    elif(mop=="2"):
        print("Buscar por:", end=" ")
        musicName = input()
        music = user.acessaMidia(musicName)[0]
        if(len(music>0)):
            musicaFormatada(music)
        else:
            print("Musica Não Encontrada!")
            menuMusica(user)
    elif(mop=="3"):
        musicName = input("Musica: ")
        if(len(user.addMusicaFavorita(musicName)) > 0):
            print("Musica Adicionada!")
        else:
            print("Musica não encontrada!")
        menuMusica(user)
    elif(mop=="4"):
        musicName = input("Musica: ")
        user.deletaFavorito(musicName)
        print("Musica Deletada")

    elif(mop=="5"):
        musicName = input("Musica: ")
        if(len(user.ouvirDepois(musicName)) > 0):
            print("Musica Adicionada!")
        else:
            print("Musica não encontrada!")
        menuMusica(user)
    elif(mop=="6"):
        musicName = input("Musica: ")
        user.deletaOuvirDepois(musicName)
        print("Musica Deletada")
    elif(mop=="0"):
        menuUser(user)
    else:
        print("Opção Invalida!")
        menuMusica(user)

def menuAdmMusica(user):
    print(" 1 - Adicionar Musica \n 2 - Remover Musica \n 3 - Ver Todas Musicas \n 4 - Buscar uma Musica \n 5 - Adicionar Musica Favoritos \n 6 - Remover Musica Favoritos \n 7 - Adicionar Musica Ouvir Depois \n 8 - Remover Musica Ouvir Depois \n 0 - Voltar")
    mop = input()
    if(mop=="1"):
        nome = input("Nome: ")
        criador = input("Criador: ")
        genero = input("Genero: ")
        lancamento = input("Lançamento: ")
        duracao = input("Duraçao: ")
        music = Midia(nome,lancamento,criador,duracao,genero)
        music.createMidia()
        print("Musica criada com sucesso!")
        menuAdmMusica(user)
    elif(mop=="2"):
        midia = input("Nome Musica: ")
        user.deletaMidia(midia)
    elif(mop=="3"):
        for music in db.getAllMusics():
            musicaFormatada(music)
    elif(mop=="4"):
        print("Buscar por:", end=" ")
        musicName = input()
        music = user.acessaMidia(musicName)[0]
        if(len(music>0)):
            musicaFormatada(music)
        else:
            print("Musica Não Encontrada!")
        menuAdmMusica(user)
    elif(mop=="5"):
        musicName = input("Musica: ")
        if(len(user.addMusicaFavorita(musicName)) > 0):
            print("Musica Adicionada!")
        else:
            print("Musica não encontrada!")
        menuAdmMusica(user)
    elif(mop=="6"):
        musicName = input("Musica: ")
        user.deletaFavorito(musicName)
        print("Musica Deletada")

    elif(mop=="7"):
        musicName = input("Musica: ")
        if(len(user.ouvirDepois(musicName)) > 0):
            print("Musica Adicionada!")
        else:
            print("Musica não encontrada!")
        menuAdmMusica(user)
    elif(mop=="8"):
        musicName = input("Musica: ")
        user.deletaOuvirDepois(musicName)
        print("Musica Deletada")
        menuAdmMusica(user)
    elif(mop=="0"):
        menuAdmin(user)
    else:
        print("Opção Invalida!")
        menuAdmMusica(user)

def mostrarDados(user):
    print(f"Nome: {user.nome}")
    print(f"Email:{user.email}")
    print(f"Data de Nascimento:{user.data_de_nascimento}")
    print(f"CPF: {user.cpf}")
    print(f"Dia do Vencimento: {user.dia_do_vencimento}")
    print(f"Método de Pagamento: {user.metodo_de_pagamento}")
    print()

def menuAlteraInfo(user):
    print("1 - Altera Email | 2 - Mudar Dia de Vencimento | 3 - Altera Senha | 4 - Cancela Assinatura | 5 - Exclui Conta | 0 - Voltar")
    maiop = input()

    if(maiop=="1"):
        newEmail = input("Novo Email: ")
        user.alteraEmail(newEmail)
        print("Email alterado com sucesso!")
    elif(maiop=="2"):
        newVencimento = input("Novo Vencimento: ")
        user.alteraVencimento(newVencimento)
        print("Vencimento alterado com sucesso!")
    elif(maiop=="3"):
        newPass = input("Nova Senha: ")
        user.alteraSenha(newPass)
        print("Senha alterada com sucesso!")
    elif(maiop=="4"):
        user.cancelaAssinatura()
        print("Assinatura cancelada com sucesso!")
    elif(maiop=="5"):
        user.deletaConta()
        print("Conta Excluida com sucesso!")
        welcome()
    elif(maiop=="0"):
        pass
    else:
        print("Opção Invalida!")
    if isinstance(user, Admin):
        menuAdmin(user)
    else:
        menuUser(user)

def menuAdmAlteraInfo(admin):
    print("1 - Mostrar Dados Usuario | 2 - Altera Email | 3 - Mudar Dia de Vencimento | 4 - Cancela Assinatura | 5 - Exclui Conta | 0 - Voltar")
    maiop = input()

    if(maiop=="1"):
        usuario = input("Email Usuario: ")
        obj = admin.mostraDadosUsuario(usuario)
        if(obj!=False):
            user = Usuario(obj["nome"],obj["email"],obj["senha"],obj["nascimento"],obj["pagamento"],obj["vencimento"],obj["cpf"])
            mostrarDados(user)
            menuAdmAlteraInfo(admin)
        else:
            print("Usuario Não Encontrado!")
            menuAdmAlteraInfo(admin)
    elif(maiop=="2"):
        usuario = input("Email Usuario: ")
        newEmail = input("Novo Email: ")
        admin.alteraEmailAdmin(usuario,newEmail)
        print("Email alterado com sucesso!")
        menuAdmAlteraInfo(admin)
    elif(maiop=="3"):
        usuario = input("Email Usuario: ")
        newVencimento = input("Novo Vencimento: ")
        admin.alteraVencimentoAdmin(usuario,newVencimento)
        print("Vencimento alterado com sucesso!")
        menuAdmAlteraInfo(admin)
    elif(maiop=="4"):
        usuario = input("Email Usuario: ")
        admin.adminCancelaAssinatura(usuario)
        print("Assinatura cancelada com sucesso!")
        menuAdmAlteraInfo(admin)
    elif(maiop=="5"):
        usuario = input("Email Usuario: ")
        admin.adminDeletaConta(usuario)
        print("Conta Excluida com sucesso!")
        menuAdmAlteraInfo(admin)
    elif(maiop=="0"):
        menuAdmin(admin)
    else:
        print("Opção Invalida!")
        menuAdmAlteraInfo(admin)

def menuUser(user):
    print("Menu Usuario")
    print("1 - Musicas | 2 - Ver Perfil | 3 - Alterar Informações | 0 - Sair")
    uop = input()
    if(uop=="1"):
        menuMusica(user)
    elif(uop=="2"):
        mostrarDados(user)
        menuUser(user)
    elif(uop=="3"):
        menuAlteraInfo(user)
    elif(uop=="0"):
        menu()
    else:
        print("Opção Invalida!")
        menuUser()

def menuAdmin(admin):
    print("Menu Administrador")
    print("1 - Musicas | 2 - Ver Perfil | 3 - Alterar Informações | 4 - Informações Usuarios | 0 - Sair")
    uop = input()
    if(uop=="1"):
        menuAdmMusica(admin)
    elif(uop=="2"):
        mostrarDados(admin)
        menuUser(admin)
    elif(uop=="3"):
        menuAlteraInfo(admin)
    elif(uop=="4"):
        menuAdmAlteraInfo(admin)
    elif(uop=="0"):
        menu()
    else:
        print("Opção Invalida!")
        menuUser()

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
    else:
        print("Conta não encontrada!")
        entrar()

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
        sair()
    else:
        print("Opção Invalida!")
        menu()

db = Graph(uri='bolt://localhost:7687',
                        user='neo4j', password='bd2')

welcome()