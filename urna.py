#Definção das variáveis
VictorRamos = 0
RafaelAlves = 0
HelenaRibeiro = 0
ValeriaVieira = 0
JairInacio = 0
JuanJamal = 0
MichaeleMoreira = 0
IvoneteSantana = 0
PaoloSantoro = 0
JamileCassia = 0
brancoVereador = 0
nuloVereador = 0

RogerioToledo = 0
CiceroPompeu = 0
MillenaMileno = 0
brancoPrefeito = 0
nuloPrefeito = 0

voto = 0
confirmacao = 0

quantidadeVotos = 0

#Apresentação
print("Seja Bem-vindo a Eleição do Ano de 2022")

#Apresentação dos Vereadores e seus Partidos
def lista_dos_vereadores():
    print("\n#############################################################################")
    print("Abaixo estão os Candidatos para Vereador:\n")
    print("->.......Victor Ramos...........Partido Amor e Cidadania...........Vote 11111;")
    print("->.......Rafael Alves..........Partido Benefífio do Povo..........Vote 22222;")
    print("->.......Helena Ribeiro........Partido Comando Pacifico...........Vote 33333;")
    print("->.......Valéria Vieira........Partido Democracia Total...........Vote 44444;")
    print("->.......Jair Inácio...........Partido Esperança do Povo..........Vote 55555;")
    print("->.......Juan Jamal............Partido Força e Alegria............Vote 66666;")
    print("->.......Michaele Moreira......Partido GeoPolítica Brasileira.....Vote 77777;")
    print("->.......Ivonete Santana.......Partido Histórico Partido..........Vote 88888;")
    print("->.......Paolo Santoro.........Partido Investimento e Educação....Vote 99999;")
    print("->.......Jamile de Cassia......Partido Jogando pela Democracia....Vote 54321;")
    print("->.......Branco...................................................Vote 12345.\n")
    print("#############################################################################")

#Apresentação dos Prefeitos e seus Partidos
def lista_dos_prefeitos():
    print("\n#############################################################################")
    print("Abaixo estão os Candidatos para Prefeito:\n")
    print("->.......Rogério Toledo........Partido Amor e Cidadania..............Vote 11;")
    print("->.......Cícero Pompeu.........Partido Benefício do Povo.............Vote 22;")
    print("->.......Millena Mileno........Partido Comando Pacífico..............Vote 33;")
    print("->.......Branco......................................................Vote 00.\n")
    print("#############################################################################")


#Início da Votação para Vereadores
def Escolha_dos_vereadores():
    voto = int(input("\n###########################################\n"
                     "DIGITE O NÚMERO DO CANDIDATO A VEREADOR: "))
    #Uso das variáveis dos Vereadores
    global VictorRamos
    global RafaelAlves
    global HelenaRibeiro
    global ValeriaVieira
    global JairInacio
    global JuanJamal
    global MichaeleMoreira
    global IvoneteSantana
    global PaoloSantoro
    global JamileCassia
    global brancoVereador
    global nuloVereador

    #Eleição dos Candidatos à Vereadores
    if voto == 11111:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Victor Ramos?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            VictorRamos = VictorRamos + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 22222:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Rafael Alves?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            RafaelAlves = RafaelAlves + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 33333:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Helena Ribeiro?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            HelenaRibeiro = HelenaRibeiro + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 44444:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Valéria Vieira?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            ValeriaVieira = ValeriaVieira + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 55555:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Jair Inácio?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            JairInacio = JairInacio + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 66666:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Juan Jamal?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            JuanJamal = JuanJamal + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 77777:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Michaele Moreira?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            MichaeleMoreira = MichaeleMoreira + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 88888:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Ivonete Santana?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            IvoneteSantana = IvoneteSantana + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 99999:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Paolo Santoro?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            PaoloSantoro = PaoloSantoro + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 54321:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Jamile de Cassia?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            JamileCassia = JamileCassia + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

    elif voto == 12345:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Branco?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            brancoVereador = brancoVereador + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()
    else:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Nulo?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            nuloVereador = nuloVereador + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_vereadores()

#Início da Votação para Prefeitos
def Escolha_dos_prefeitos():
    voto = int(input("\n##########################################\n"
                     "DIGITE O NÚMERO DO CANDIDATO A PREFEITO: "))
    #uso das variáveis dos Prefeito
    global RogerioToledo
    global CiceroPompeu
    global MillenaMileno
    global brancoPrefeito
    global nuloPrefeito

    #Eleição dos candidatos à Prefeito
    if voto == 11:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Rogério Toledo?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            RogerioToledo = RogerioToledo + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_prefeitos()

    elif voto == 22:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Cícero Pompeu?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            CiceroPompeu = CiceroPompeu + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_prefeitos()

    elif voto == 33:
        confirmacao =int(input(f"\nDeseja confirmar o voto {voto} para Millena Mileno?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            MillenaMileno = MillenaMileno + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_prefeitos()

    elif voto == 00:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Branco?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            brancoPrefeito = brancoPrefeito + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_prefeitos()
    else:
        confirmacao = int(input(f"\nDeseja confirmar o voto {voto} para Nulo?\n(Digite 1 para sim ou 2 para não.) "))
        if confirmacao == 1:
            nuloPrefeito = nuloPrefeito + 1
            print('voto computado com sucesso!')
        elif confirmacao == 2:
            print('voto cancelado! vote novamente')
            Escolha_dos_prefeitos()

#Métodos usados para encaminhar a votação
def votacao():
    Escolha_dos_vereadores()
    Escolha_dos_prefeitos()

#Boletim da Votação
def zerezima_f():
    print("\n#############################################################################")
    print("Abaixo estão os Candidatos para Vereador:\n")
    print(f"->......Victor Ramos..........Partido Amor e Cidadania............Tem {VictorRamos} Votos;")
    print(f"->......Rafael Alves.........Partido Benefífio do Povo...........Tem {RafaelAlves} Votos;")
    print(f"->......Helena Ribeiro.......Partido Comando Pacifico............Tem {HelenaRibeiro} Votos;")
    print(f"->......Valéria Vieira.......Partido Democracia Total............Tem {ValeriaVieira} Votos;")
    print(f"->......Jair Inácio..........Partido Esperança do Povo...........Tem {JairInacio} Votos;")
    print(f"->......Juan Jamal...........Partido Força e Alegria.............Tem {JuanJamal} Votos;")
    print(f"->......Michaele Moreira.....Partido GeoPolítica Brasileira......Tem {MichaeleMoreira} Votos;")
    print(f"->......Ivonete Santana......Partido Histórico Partido...........Tem {IvoneteSantana} Votos;")
    print(f"->......Paolo Santoro........Partido Investimento e Educação.....Tem {PaoloSantoro} Votos;")
    print(f"->......Jamile de Cassia.....Partido Jogando pela Democracia.....Tem {JamileCassia} Votos;")
    print(f"->......Branco...................................................Tem {brancoVereador} Votos;")
    print(f"->......Nulo.....................................................Tem {nuloVereador} Votos.")

    print("\nAbaixo estão os Candidatos para Prefeito:\n")
    print(f"->......Rogério Toledo.......Partido Amor e Cidadania............Tem {RogerioToledo} Votos;")
    print(f"->......Cícero Pompeu........Partido Benefício do Povo...........Tem {CiceroPompeu} Votos;")
    print(f"->......Millena Mileno.......Partido Comando Pacífico............Tem {MillenaMileno} Votos;")
    print(f"->......Branco...................................................Tem {brancoPrefeito} Votos;")
    print(f"->......Nulo.....................................................Tem {nuloPrefeito} Votos.")
    print("#############################################################################\n")

    print(f"\nA quantidade de eleitores que participaram da votação foram: {quantidadeVotos}.\n")

    #Apuração dos Votos para Prefeito
    if VictorRamos > RafaelAlves and VictorRamos > HelenaRibeiro and VictorRamos > ValeriaVieira and VictorRamos > JairInacio and VictorRamos > JuanJamal and VictorRamos > MichaeleMoreira and VictorRamos > IvoneteSantana and VictorRamos > PaoloSantoro and VictorRamos > JamileCassia:
        print("=> Victor Ramos ganhou a eleição.")

    elif RafaelAlves > VictorRamos and RafaelAlves > HelenaRibeiro and RafaelAlves > ValeriaVieira and RafaelAlves > JairInacio and RafaelAlves > JuanJamal and RafaelAlves > MichaeleMoreira and RafaelAlves > IvoneteSantana and RafaelAlves > PaoloSantoro and RafaelAlves > JamileCassia:
        print("=> Rafael Alves ganhou a eleição.")

    elif HelenaRibeiro > VictorRamos and HelenaRibeiro > RafaelAlves and HelenaRibeiro > ValeriaVieira and HelenaRibeiro > JairInacio and HelenaRibeiro > JuanJamal and HelenaRibeiro > MichaeleMoreira and HelenaRibeiro > IvoneteSantana and HelenaRibeiro > PaoloSantoro and HelenaRibeiro > JamileCassia:
        print("=> Helena Ribeiro ganhou a eleição.")

    elif ValeriaVieira > VictorRamos and ValeriaVieira > RafaelAlves and ValeriaVieira > HelenaRibeiro and ValeriaVieira > JairInacio and ValeriaVieira > JuanJamal and ValeriaVieira > MichaeleMoreira and ValeriaVieira > IvoneteSantana and ValeriaVieira > PaoloSantoro and ValeriaVieira > JamileCassia:
        print("=> Valeria Vieira ganhou a eleição.")

    elif JairInacio > VictorRamos and JairInacio > RafaelAlves and JairInacio > HelenaRibeiro and JairInacio > ValeriaVieira and JairInacio > JuanJamal and JairInacio > MichaeleMoreira and JairInacio > IvoneteSantana and JairInacio > PaoloSantoro and JairInacio > JamileCassia:
        print("=> Jair Inácio ganhou a eleição.")

    elif JuanJamal > VictorRamos and JuanJamal > RafaelAlves and JuanJamal > HelenaRibeiro and JuanJamal > ValeriaVieira and JuanJamal > JairInacio and JuanJamal > MichaeleMoreira and JuanJamal > IvoneteSantana and JuanJamal > PaoloSantoro and JuanJamal > JamileCassia:
        print("=> Juan Jamal ganhou a eleição.")

    elif MichaeleMoreira > VictorRamos and MichaeleMoreira > RafaelAlves and MichaeleMoreira > HelenaRibeiro and MichaeleMoreira > ValeriaVieira and MichaeleMoreira > JairInacio and MichaeleMoreira > JuanJamal and MichaeleMoreira > IvoneteSantana and MichaeleMoreira > PaoloSantoro and MichaeleMoreira > JamileCassia:
        print("=> Michaele Moreira ganhou a eleição.")

    elif IvoneteSantana > VictorRamos and IvoneteSantana > RafaelAlves and IvoneteSantana > HelenaRibeiro and IvoneteSantana > ValeriaVieira and IvoneteSantana > JairInacio and IvoneteSantana > JuanJamal and IvoneteSantana > MichaeleMoreira and IvoneteSantana > PaoloSantoro and IvoneteSantana > JamileCassia:
        print("=> Ivonete Santana ganhou a eleição.")

    elif PaoloSantoro > VictorRamos and PaoloSantoro > RafaelAlves and PaoloSantoro > HelenaRibeiro and PaoloSantoro > ValeriaVieira and PaoloSantoro > JairInacio and PaoloSantoro > JuanJamal and PaoloSantoro > MichaeleMoreira and PaoloSantoro > IvoneteSantana and PaoloSantoro > JamileCassia:
        print("=> Paolo Santoro ganhou a eleição.")

    elif JamileCassia > VictorRamos and JamileCassia > RafaelAlves and JamileCassia > HelenaRibeiro and JamileCassia > ValeriaVieira and JamileCassia > vereador4 and JamileCassia > JairInacio and JamileCassia > JuanJamal and JamileCassia > MichaeleMoreira and JamileCassia > IvoneteSantana and JamileCassia > PaoloSantoro:
        print("=> Jamile de Cassia ganhou a eleição.")
    #Em caso de empate para Vereador
    elif VictorRamos == RafaelAlves and VictorRamos == HelenaRibeiro and VictorRamos == ValeriaVieira and VictorRamos == JairInacio and VictorRamos == JuanJamal and VictorRamos == MichaeleMoreira and VictorRamos == IvoneteSantana and VictorRamos == PaoloSantoro and VictorRamos == JamileCassia:
        print("=> A Votação terminou com Empate entre os candidatos a vereador. Será necessário o segundo turno.")
    else:
        print("=> A Votação terminou com Empate entre os candidatos a vereador. Será necessário o segundo turno.")

    # Apuração dos Votos para Prefeito
    if RogerioToledo > CiceroPompeu and RogerioToledo > MillenaMileno:
        print("=> Rogério Toledo ganhou a eleição.")

    elif CiceroPompeu > RogerioToledo and CiceroPompeu > MillenaMileno:
        print("=> Cícero Pompeu ganhou a eleição.")

    elif MillenaMileno > RogerioToledo and MillenaMileno > CiceroPompeu:
        print("=> Millena Mileno ganhou a eleição.")
    # Em caso de Empate
    elif RogerioToledo == CiceroPompeu and RogerioToledo > MillenaMileno:
        print("=> A Votação terminou com Empate entre Rogério Toledo e Cícero Pompeu. Será necessário o segundo turno.")

    elif CiceroPompeu == MillenaMileno and CiceroPompeu > RogerioToledo:
        print("=> A Votação terminou com Empate entre Cícero Pompeu e Millena Mileno. Será necessário o segundo turno.")

    elif MillenaMileno == RogerioToledo and MillenaMileno > CiceroPompeu:
        print("=> A Votação terminou com Empate entre Rogério Toledo e Millena Mileno. Será necessário o segundo turno.")

    elif RogerioToledo == CiceroPompeu and RogerioToledo == MillenaMileno:
        print("=> A Votação terminou com Empate entre todos os candidatos a prefeito. Será necessário o segundo turno.")

#Opções do Menu
def menu():
    print('''
    1- Zerézima;
    2- Lista dos Vereador;
    3- Lista dos Prefeito;
    4- Votar; 
    0- Sair.
    ''')
    return int(input('Digite um número entre 0 e 5: '))

#Menu de Opções
while True:
    opcao = menu()
    if opcao == 0:
        print("A Votação foi encerrada.")
        break
    elif opcao == 1:
        zerezima_f()
    elif opcao == 2:
        lista_dos_vereadores()
    elif opcao == 3:
        lista_dos_prefeitos()
    elif opcao == 4:
        quantidadeVotos = quantidadeVotos + 1 #Contabilizando o número de eleitores
        votacao()