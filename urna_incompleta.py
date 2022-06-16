
#Variáveis dos Vereadores e Prefeitos
vereador1 = 0
vereador2 = 0
vereador3 = 0
vereador4 = 0
vereador5 = 0
vereador6 = 0
vereador7 = 0
vereador8 = 0
vereador9 = 0
vereador0 = 0
brancoVereador = 0
nuloVereador = 0

prefeito1 = 0
prefeito2 = 0
prefeito3 = 0
brancoPrefeito = 0
nuloPrefeito = 0

quantidadeVotos = 0

#Apresentação
print("\n\nSeja Bem-vindo a Eleição do Ano de 2022\n"
      "#######################################")

iniciar = 1
while iniciar == 1:

#Definção das variáveis dos Votos
    votoVereador = 0
    votoPrefeito = 0

#Definição da Zerézima
    zerezima = int(input("\nVocê deseja imprimir Zerézima? \n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
    if zerezima == 1 :
        print("\n#######################################\n"
              "Abaixo estão os Candidatos para Vereador:")
        print(f"        Vereador1, do Partido AAA, com {vereador1};")
        print(f"        Vereador2, do Partido BBB, com {vereador2};")
        print(f"        Vereador3, do partido CCC, com {vereador3};")
        print(f"        Vereador4, do partido DDD, com {vereador4};")
        print(f"        Vereador5, do partido EEE, com {vereador5};")
        print(f"        Vereador6, do partido FFF, com {vereador6};")
        print(f"        Vereador7, do partido GGG, com {vereador7};")
        print(f"        Vereador8, do partido HHH, com {vereador8};")
        print(f"        Vereador9, do partido III, com {vereador9};")
        print(f"        Vereador0, do partido JJJ, com {vereador0};")
        print(f"        Branco, com {brancoVereador};")
        print(f"        Nulo, com {nuloVereador}.")

        print("\nAbaixo estão os Candidatos para Prefeito:")
        print(f"        Prefeito1, do partido AAA, com {prefeito1};")
        print(f"        Prefeito2, do partido BBB, com {prefeito2};")
        print(f"        Prefeito3, do partido CCC, com {prefeito3};")
        print(f"        Branco, com {brancoPrefeito};")
        print(f"        Nulo, com {nuloPrefeito}.")

        print(f"\nO número total de eleitores são: {quantidadeVotos}.")

    elif zerezima == 2:
        print("Vamos para a próxima etapa.\n")

#Lista dos Vereadores
    cont = int(input("\n#######################################\n"
                     "Deseja ver a lista dos candidatos para Vereador? \n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
    if cont == 1:
        print("\n#######################################\n"
              "Abaixo estão os Candidatos para Vereador:")
        print("         Vereador1, do Partido AAA, vote 11111;")
        print("         Vereador2, do Partido BBB, vote 22222;")
        print("         Vereador3, do partido CCC, vote 33333;")
        print("         Vereador4, do partido DDD, vote 44444;")
        print("         Vereador5, do partido EEE, vote 55555;")
        print("         Vereador6, do partido FFF, vote 66666;")
        print("         Vereador7, do partido GGG, vote 77777;")
        print("         Vereador8, do partido HHH, vote 88888;")
        print("         Vereador9, do partido III, vote 99999;")
        print("         Vereador0, do partido JJJ, vote 54321;")
        print("         para votar em Branco, digite 00000.")

        print("\nLembrete: o seu voto é SECRETO. Vote consciente.\n")

    elif cont == 2:
        print("Então vamos continuar.")
        print("\nLembrete: o seu voto é SECRETO. Vote consciente.\n")

#Escolha dos Vereadores
    confirmacao = 0
    while votoVereador == 0 or confirmacao == 2:
        votoVereador = int(input("\n#######################################\n"
                                 "DIGITE O NÚMERO DO CANDIDATO: "))

        if votoVereador == 11111:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador1?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador1 = vereador1 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 22222:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador2?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador2 = vereador2 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 33333:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador3?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador3 = vereador3 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 44444:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador4?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador4 = vereador4 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 55555:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador5?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador5 = vereador5 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 66666:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador6?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador6 = vereador6 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 77777:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador7?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador7 = vereador7 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 88888:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador8?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador8 = vereador8 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 99999:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador9?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador9 = vereador9 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 12345:
            print(f"\nDeseja confirmar o voto {votoVereador} para Vereador0?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                vereador0 = vereador0 + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador == 54321:
            print(f"\nDeseja confirmar o voto {votoVereador} em Branco?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                brancoVereador = brancoVereador + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

        if votoVereador != 54321 and votoVereador != 11111 and votoVereador != 22222 and votoVereador != 33333 and votoVereador != 44444 and votoVereador != 55555 and votoVereador != 66666 and votoVereador != 77777 and votoVereador != 88888 and votoVereador != 99999 and votoVereador != 12345 and votoVereador != 0:
            print(f"\nDeseja confirmar o voto {votoVereador} para Nulo?")
            confirmacao = int(input("\n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                nuloVereador = nuloVereador + 1
                pass
            elif confirmacao == 2:
                votoVereador = 0

    print("Os votos para Vereador foram computados.\n\n"
          "#######################################\n"
          "Agora escolha o candidato para Prefeito.\n")

#Escolha dos Prefeitos
    cont = int(input("Deseja ver a lista dos candidatos para Prefeito? \n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
    if cont == 1:
        print("\nAbaixo estão os Candidatos para Prefeito:")
        print("         Prefeito1, do partido AAA, vote 11;")
        print("         Prefeito2, do partido BBB, vote 22;")
        print("         Prefeito3, do partido CCC, vote 33;")
        print("         Para votar em Branco, digite 00.")
        print("\nLembrete: o seu voto é SECRETO. Vote consciente.\n")

    elif cont == 2:
        print("Então vamos continuar.")
        print("\nLembrete: o seu voto é SECRETO. Vote consciente.\n")

    cofirmação = 0
    while votoPrefeito == 0 or confirmacao == 2:
        votoPrefeito = int(input("\n#######################################\nDIGITE O NÚMERO DO CANDIDATO: "))

        if votoPrefeito == 11:
            print(f"\nDeseja confirmar o voto {votoPrefeito} para Prefeito1?")
            confirmacao = int(input("-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                prefeito1 = prefeito1 + 1
                pass
            elif confirmacao == 2:
                votoPrefeito = 0

        if votoPrefeito == 22:
            print(f"\nDeseja confirmar o voto {votoPrefeito} para Prefeito2?")
            confirmacao = int(input("-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                prefeito2 = prefeito2 + 1
                pass
            elif confirmacao == 2:
                votoPrefeito = 0

        if votoPrefeito == 33:
            print(f"\nDeseja confirmar o voto {votoPrefeito} para Prefeito3?")
            confirmacao = int(input("-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                prefeito3 = prefeito3 + 1
                pass
            elif confirmacao == 2:
                votoPrefeito = 0

        if votoPrefeito == 21:
            print(f"\nDeseja confirmar o voto {votoPrefeito} em Branco?")
            confirmacao = int(input("-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                brancoPrefeito = brancoPrefeito + 1
                pass
            elif confirmacao == 2:
                votoPrefeito = 0

        if votoPrefeito != 54321 and votoPrefeito != 11 and votoPrefeito != 22 and votoPrefeito != 33 and votoPrefeito != 0:
            print(f"\nDeseja confirmar o voto {votoPrefeito} para Nulo?")
            confirmacao = int(input("-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
            if confirmacao == 1:
                nuloPrefeito = nuloPrefeito + 1
                pass
            elif confirmacao == 2:
                votoPrefeito = 0

    print("\nOs votos para Prefeito foram computados.\n##################################################")

    iniciar = int(input("\nDeseja fazer uma nova votação? \n-> Digite 1 para 'SIM'.\n-> Digite 2 para 'NÃO'.\n"))
    if iniciar == 1:
        print("Programa em andamento.\n")
        quantidadeVotos = quantidadeVotos + 1
    elif iniciar == 2 :
        print("Estamos finalizando a votação.")
        quantidadeVotos = quantidadeVotos + 1

#Apresentações finais
while iniciar == 2 or fim == 1:
    print("\n##################################################\n"
          "Abaixo esta o Boletim para Vereador:")
    print(f"        Vereador1, do Partido AAA, com {vereador1};")
    print(f"        Vereador2, do Partido BBB, com {vereador2};")
    print(f"        Vereador3, do partido CCC, com {vereador3};")
    print(f"        Vereador4, do partido DDD, com {vereador4};")
    print(f"        Vereador5, do partido EEE, com {vereador5};")
    print(f"        Vereador6, do partido FFF, com {vereador6};")
    print(f"        Vereador7, do partido GGG, com {vereador7};")
    print(f"        Vereador8, do partido HHH, com {vereador8};")
    print(f"        Vereador9, do partido III, com {vereador9};")
    print(f"        Vereador0, do partido JJJ, com {vereador0};")
    print(f"        Branco, com {brancoVereador};")
    print(f"        Nulo, com {nuloVereador}.")

    print("\nAbaixo esta o Boletim para Prefeito:")
    print(f"        Prefeito1, do partido AAA, com {prefeito1};")
    print(f"        Prefeito2, do partido BBB, com {prefeito2};")
    print(f"        Prefeito3, do partido CCC, com {prefeito3};")
    print(f"        Branco, com {brancoPrefeito};")
    print(f"        Nulo, com {nuloPrefeito}.")

    print(f"\nO número total de eleitores são: {quantidadeVotos}.\n")

#Apuração dos votos para Vereador
    if vereador1 > vereador2 and vereador1 > vereador3 and vereador1 > vereador4 and vereador1 > vereador5 and vereador1 > vereador6 and vereador1 > vereador7 and vereador1 > vereador8 and vereador1 > vereador9 and vereador1 > vereador0:
        print("=> vereador1 ganhou a eleição.")

    elif vereador2 > vereador1 and vereador2 > vereador3 and vereador2 > vereador4 and vereador2 > vereador5 and vereador2 > vereador6 and vereador2 > vereador7 and vereador2 > vereador8 and vereador2 > vereador9 and vereador2 > vereador0:
        print("=> vereador2 ganhou a eleição.")

    elif vereador3 > vereador1 and vereador3 > vereador2 and vereador3 > vereador4 and vereador3 > vereador5 and vereador3 > vereador6 and vereador3 > vereador7 and vereador3 > vereador8 and vereador3 > vereador9 and vereador3 > vereador0:
        print("=> vereador3 ganhou a eleição.")

    elif vereador4 > vereador1 and vereador4 > vereador2 and vereador4 > vereador3 and vereador4 > vereador5 and vereador4 > vereador6 and vereador4 > vereador7 and vereador4 > vereador8 and vereador4 > vereador9 and vereador4 > vereador0:
        print("=> vereador4 ganhou a eleição.")

    elif vereador5 > vereador1 and vereador5 > vereador2 and vereador5 > vereador3 and vereador5 > vereador4 and vereador5 > vereador6 and vereador5 > vereador7 and vereador5 > vereador8 and vereador5 > vereador9 and vereador5 > vereador0:
        print("=> vereador5 ganhou a eleição.")

    elif vereador6 > vereador1 and vereador6 > vereador2 and vereador6 > vereador3 and vereador6 > vereador4 and vereador6 > vereador5 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("=> vereador6 ganhou a eleição.")

    elif vereador7 > vereador1 and vereador7 > vereador2 and vereador7 > vereador3 and vereador7 > vereador4 and vereador7 > vereador5 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> vereador7 ganhou a eleição.")

    elif vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> vereador8 ganhou a eleição.")

    elif vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> vereador9 ganhou a eleição.")

    elif vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> vereador0 ganhou a eleição.")
# Em caso de Empate com vereador 1
    elif vereador2 == vereador1 and vereador2 > vereador3 and vereador2 > vereador4 and vereador2 > vereador5 and vereador2 > vereador6 and vereador2 > vereador7 and vereador2 > vereador8 and vereador2 > vereador9 and vereador2 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito2. Será necessário o segundo turno.")

    elif vereador3 == vereador1 and vereador3 > vereador2 and vereador3 > vereador4 and vereador3 > vereador5 and vereador3 > vereador6 and vereador3 > vereador7 and vereador3 > vereador8 and vereador3 > vereador9 and vereador3 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito3. Será necessário o segundo turno.")

    elif vereador4 == vereador1 and vereador4 > vereador2 and vereador4 > vereador3 and vereador4 > vereador5 and vereador4 > vereador6 and vereador4 > vereador7 and vereador4 > vereador8 and vereador4 > vereador9 and vereador4 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito4. Será necessário o segundo turno.")

    elif vereador5 == vereador1 and vereador5 > vereador2 and vereador5 > vereador3 and vereador5 > vereador4 and vereador5 > vereador6 and vereador5 > vereador7 and vereador5 > vereador8 and vereador5 > vereador9 and vereador5 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito5. Será necessário o segundo turno.")

    elif vereador6 == vereador1 and vereador6 > vereador2 and vereador6 > vereador3 and vereador6 > vereador4 and vereador6 > vereador5 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito6. Será necessário o segundo turno.")

    elif vereador7 == vereador1 and vereador7 > vereador2 and vereador7 > vereador3 and vereador7 > vereador4 and vereador7 > vereador5 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito0 e Prefeito1. Será necessário o segundo turno.")
#Em caso de empate com vereador 2
    elif vereador3 == vereador2 and vereador3 > vereador1 and vereador3 > vereador4 and vereador3 > vereador5 and vereador3 > vereador6 and vereador3 > vereador7 and vereador3 > vereador8 and vereador3 > vereador9 and vereador3 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito3. Será necessário o segundo turno.")

    elif vereador4 == vereador2 and vereador4 > vereador1 and vereador4 > vereador3 and vereador4 > vereador5 and vereador4 > vereador6 and vereador4 > vereador7 and vereador4 > vereador8 and vereador4 > vereador9 and vereador4 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito4. Será necessário o segundo turno.")

    elif vereador5 == vereador2 and vereador5 > vereador1 and vereador5 > vereador3 and vereador5 > vereador4 and vereador5 > vereador6 and vereador5 > vereador7 and vereador5 > vereador8 and vereador5 > vereador9 and vereador5 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito5. Será necessário o segundo turno.")

    elif vereador6 == vereador2 and vereador6 > vereador1 and vereador6 > vereador3 and vereador6 > vereador4 and vereador6 > vereador5 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito6. Será necessário o segundo turno.")

    elif vereador7 == vereador2 and vereador7 > vereador1 and vereador7 > vereador3 and vereador7 > vereador4 and vereador7 > vereador5 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador2 and vereador8 > vereador1 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador2 and vereador9 > vereador1 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador2 and vereador0 > vereador1 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito0 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate com Vereador3
    elif vereador4 == vereador3 and vereador4 > vereador1 and vereador4 > vereador2 and vereador4 > vereador5 and vereador4 > vereador6 and vereador4 > vereador7 and vereador4 > vereador8 and vereador4 > vereador9 and vereador4 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito4. Será necessário o segundo turno.")

    elif vereador5 == vereador3 and vereador5 > vereador1 and vereador5 > vereador2 and vereador5 > vereador4 and vereador5 > vereador6 and vereador5 > vereador7 and vereador5 > vereador8 and vereador5 > vereador9 and vereador5 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito5. Será necessário o segundo turno.")

    elif vereador6 == vereador3 and vereador6 > vereador1 and vereador6 > vereador2 and vereador6 > vereador4 and vereador6 > vereador5 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito6. Será necessário o segundo turno.")

    elif vereador7 == vereador3 and vereador7 > vereador1 and vereador7 > vereador2 and vereador7 > vereador4 and vereador7 > vereador5 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador3 and vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador3 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador3 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito3 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador4
    elif vereador5 == vereador4 and vereador5 > vereador1 and vereador5 > vereador2 and vereador5 > vereador3 and vereador5 > vereador6 and vereador5 > vereador7 and vereador5 > vereador8 and vereador5 > vereador9 and vereador5 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito5. Será necessário o segundo turno.")

    elif vereador6 == vereador4 and vereador6 > vereador1 and vereador6 > vereador2 and vereador6 > vereador3 and vereador6 > vereador5 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito6. Será necessário o segundo turno.")

    elif vereador7 == vereador4 and vereador7 > vereador1 and vereador7 > vereador2 and vereador7 > vereador3 and vereador7 > vereador5 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador4 and vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador4 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador4 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito4 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador5
    elif vereador6 == vereador5 and vereador6 > vereador1 and vereador6 > vereador2 and vereador6 > vereador3 and vereador6 > vereador4 and vereador6 > vereador7 and vereador6 > vereador8 and vereador6 > vereador9 and vereador6 > vereador0:
        print("A Votação terminou com Empate entre Prefeito5 e Prefeito6. Será necessário o segundo turno.")

    elif vereador7 == vereador5 and vereador7 > vereador1 and vereador7 > vereador2 and vereador7 > vereador3 and vereador7 > vereador4 and vereador7 > vereador6 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito5 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador5 and vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador6 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito5 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador5 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito5 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador5 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito5 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador6
    elif vereador7 == vereador6 and vereador7 > vereador1 and vereador7 > vereador2 and vereador7 > vereador3 and vereador7 > vereador4 and vereador7 > vereador5 and vereador7 > vereador8 and vereador7 > vereador9 and vereador7 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito6 e Prefeito7. Será necessário o segundo turno.")

    elif vereador8 == vereador6 and vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador7 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito6 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador6 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador7 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito6 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador6 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador7 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito6 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador 7
    elif vereador8 == vereador7 and vereador8 > vereador1 and vereador8 > vereador2 and vereador8 > vereador3 and vereador8 > vereador4 and vereador8 > vereador5 and vereador8 > vereador6 and vereador8 > vereador9 and vereador8 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito7 e Prefeito8. Será necessário o segundo turno.")

    elif vereador9 == vereador7 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador8 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito7 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereador7 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador8 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito7 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador 8
    elif vereador9 == vereador8 and vereador9 > vereador1 and vereador9 > vereador2 and vereador9 > vereador3 and vereador9 > vereador4 and vereador9 > vereador5 and vereador9 > vereador6 and vereador9 > vereador7 and vereador9 > vereador0:
        print("=> A Votação terminou com Empate entre Prefeito8 e Prefeito9. Será necessário o segundo turno.")

    elif vereador0 == vereado8 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador9:
        print("=> A Votação terminou com Empate entre Prefeito8 e Prefeito2. Será necessário o segundo turno.")
#Em caso de Empate vereador 9
    elif vereador0 == vereado9 and vereador0 > vereador1 and vereador0 > vereador2 and vereador0 > vereador3 and vereador0 > vereador4 and vereador0 > vereador5 and vereador0 > vereador6 and vereador0 > vereador7 and vereador0 > vereador8:
        print("=> A Votação terminou com Empate entre Prefeito9 e Prefeito2. Será necessário o segundo turno.")

    elif vereador1 == vereador2 and vereador1 == vereador3 and vereador1 == vereador4 and vereador1 == vereador5 and vereador1 == vereador6 and vereador1 == vereador7 and vereador1 == vereador8 and vereador1 == vereador9 and vereador1 == vereador0:
        print("=> A Votação terminou com Empate entre todos os candidatos a prefeito. Será necessário o segundo turno.")

#Apuração dos Votos para Prefeito
    if prefeito1 > prefeito2 and prefeito1 > prefeito3:
        print("=> Prefeito1 ganhou a eleição.")

    elif prefeito2 > prefeito1 and prefeito2 > prefeito3:
        print("=> Prefeito2 ganhou a eleição.")

    elif prefeito3 > prefeito1 and prefeito3 > prefeito2:
        print("=> Prefeito3 ganhou a eleição.")
#Em caso de Empate
    elif prefeito1 == prefeito2 and prefeito1 > prefeito3:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito2. Será necessário o segundo turno.")

    elif prefeito2 == prefeito3 and prefeito2 > prefeito1:
        print("=> A Votação terminou com Empate entre Prefeito2 e Prefeito3. Será necessário o segundo turno.")

    elif prefeito3 == prefeito1 and prefeito3 > prefeito2:
        print("=> A Votação terminou com Empate entre Prefeito1 e Prefeito3. Será necessário o segundo turno.")

    elif prefeito1 == prefeito2 and prefeito1 == prefeito3:
        print("=> A Votação terminou com Empate entre todos os candidatos a prefeito. Será necessário o segundo turno.")

print("#######################################")