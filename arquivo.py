import re
try: 
    ''' para o cliente fazer cadastro '''
    resposta = 'N'
    print("Cadastro:")
    while resposta == 'N':
        nome = input("Digite o seu nome: ").upper()
        if re.search("\d", nome):
           erro = "Nomes não podem conter números"
           raise ValueError
        sobrenome = input("Digite o seu sobrenome: ").upper()
        if re.search("\d", sobrenome):
          erro = "Sobrenomes não podem conter números"
          raise ValueError
        telefone = input("Digite o seu telefone com o DDD: ")
        if not re.search("\d(10,11)", telefone) or len(telefone) > 11:
          erro = "Telefones devem conter entre 10-11 dígitos"
          raise ValueError
        email = input("Digite o seu e-mail: ")
        cep = input("Digite seu CEP (somente dígitos): ")
        if not re.search("\d{8}", cep) or len(cep)>8:
            erro = "CEP deve conter 8 dígitos"
            raise ValueError
        regiao = input("Digite a sua Região: ").upper()
        if re.search("\d", regiao):
            erro = "Regiões não podem conter números"
        senha = input("Escolha uma senha: ")

        ''' para o cliente poder conferir os seus dados e poder mudá-los caso deseje '''
        print("Confira seus dados:")
        print(f"Nome: {nome}")
        print(f"Sobrenome: {sobrenome}")
        if len(telefone) == 10:
            tele = "(" + telefone[0:2] + ")" + telefone[2:6] + "-" + telefone[6:]
        else:
            tele = "(" + telefone[0:2] + ")" + telefone[2:7] + "-" + telefone[7:]
        print(f"Telefone: {tele}")
        print(f"E-mail: {email}")
        pec = cep[0:5] + "-" + cep[5:]
        print(f"CEP: {pec}")
        print(f"Região: {regiao}")
        print(f"Senha: {senha}")
        print(f"Os dados estão corretos? [S/N]")
        resposta = str(input()).upper().strip()[0]

    ''' para o cliente fazer login '''
    print("Login:")
    loginemail = input("Digite o e-mail cadastrado: ")
    loginsenha = input("Digite a senha cadastrada: ")
    while (loginemail != email or loginsenha != senha):
        ''' se a senha ou o e-mail cadastrados não forem iguais aos inseridos na hora do login '''
        erro = "E-mail ou senha inválido"
        print(erro)
        print("Tente novamente")
        loginemail = input("Digite o e-mail cadastrado: ")
        loginsenha = input("Digite a senha cadastrada: ")

    ''' o cliente pode decidir se quer ou não fazer o questionário abaixo '''
    answer = 'S'
    answer = input("Você gostaria de responder nosso questionário? [S/N]").upper().strip()[0]
    while answer == 'S':

        ''' para saber qual tipo de plantação o cliente quer '''
        colheita = ['', '[1] Frutas', '[2] Legumes', '[3] Verduras']
        print(f"Qual tipo de colheita você gostaria de plantar? {colheita[1:4]}")
        colescolha = int(input())
        if colescolha > 3 or colescolha < 1:
            erro = "Opção inválida"
            print(erro)
            colescolha = int(input())
        crop = colheita[colescolha]
        print(f"Resposta: {crop}")

        ''' para saber quais são as possíveis colhetias que pode ter em determinada área'''
        area = float(input("Qual é o tamanho da sua área para plantar? (Em metros)"))
        print(f"Resposta: {area}")

        ''' caso o agricultor já tenha outras plantações e queira colocar poder colher alguma outra em algum mês específico '''
        mes = [' ', '[1] Janeiro', '[2] Fevereiro', '[3] Março', '[4] Abril', '[5] Maio', '[6] Junho', '[7] Julho', '[8] Agosto', '[9] Setembro', '[10] Outubro', '[11] Novembro', '[12] Dezembro', '[13] Não sei']
        print(f"Qual é o melhor mês para colheita que entre em sua rotina? {mes[1:14]}")
        mescolheita = int(input())
        if mescolheita > 13 or mescolheita < 1:
            erro = "Opção inválida! Tente novamente:"
            print(erro)
            mescolheita = int(input())
        mesescolhido = mes[mescolheita]
        print(f"Resposta: {mesescolhido}")

        ''' quanto tempo o agricultor quer que a plantação dure '''
        tempo = int(input("Em média, quantos dias você gostaria que a plantação durasse?"))
        if tempo < 1: 
            erro = "Opção inválida! Tente novamente:"
            print(erro)
            tempo = int(input())
        print(f"Resposta: {tempo}")
        
        ''' qual é a cor do solo, em média as cores do solo têm características específicas para cada plantação '''
        cor = ['', '[1] Avermelhados', '[2] Amarelos', '[3] Claros', '[4] Escuros']
        print(f"Qual é a cor do solo em que você pretende plantar? {cor[1:5]}")
        corsolo = int(input())
        if corsolo < 1 or corsolo > 4:
            erro = "Opção inválida! Tente novamente:"
            print(erro)
            corsolo = int(input())
        corescolhida = cor[corsolo]
        print(f"Resposta: {corescolhida}")

        ''' qual é a textura do solo, em média as texturas do solo têm características específicas para cada plantação '''
        textura = ['', '[1] Arenoso', '[2] Argiloso', '[3] Orgânico', '[4] Siltoso', '[5] Humífero']
        print(f"Qual é a textura do solo em que você pretende plantar? {textura[1:]}")
        textsolo = int(input())
        if textsolo < 1 or textsolo > 5:
            erro = "Opção inválida! Tente novamente:"
            print(erro)
            textsolo = int(input())
        textescolhida = textura[textsolo]
        print(f"Resposta: {textescolhida}")
           
        ''' quantas pessoas trabalham com o agricultor, quanto mais pessoas trabalharem com ele, há mais possibilidades de colheita  '''
        pessoas = int(input("Quantas pessoas trabalham contigo? (Se ninguém te ajudar, digite 0) "))
        if pessoas < 0:
            erro = "Opção inválida! Tente novamente:"
            print(erro)
            pessoas = int(input())
        print(f"Resposta: {pessoas}")

        ''' prévia de resultados usando apenas algumas variáveis (perguntas) do questionário, as respostas abaixo são apenas estimativas, o agricultor poderá ter respostas mais certeiras na aba perfil no site AgroSeed '''
        print("Prévia de resultados:")
        if textsolo == 1:
            resultado = 'O seu solo precisará de alguns cuidados antes! Veja mais sobre com a nossa IA.'
            print(resultado)
        elif textsolo == 2 and (mescolheita == 8 or colescolha == 1 or 60 < tempo < 85):
            print("Morangos são uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 2 and (mescolheita == 2 or mescolheita == 3 or mescolheita == 6 or mescolheita == 7 or colescolha == 2 or tempo< 85):
            print("Milho é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 2 and (colescolha == 2 or mescolheita == 6 or 8 <= mescolheita <= 11 or tempo < 85):
            print("Brócolis é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 3 and (colescolha == 1 or mescolheita<= 11 or mescolheita >=9):
            print("Cerejas são uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 3 and (colescolha == 2 or tempo == 80):
            print("Abobrinha é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 3 and (colescolha == 3 or 3 <= mescolheita <= 6 or 9<= mescolheita<= 11):
            print("Espinafre é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 4 and (colescolha == 1 or tempo <= 360):
            print("Pêssego é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 4 and (colescolha == 2 or mescolheita <= 9):
            print("Feijão é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 4 and (colescolha == 3 or mescolheita == 13):
            print("Cebola é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 5 and (colescolha == 1 or mescolheita <= 9 or mescolheita >= 4):
            print("Mirtilos são uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 5 and (colescolha == 2 or mescolheita<= 6):
            print("Pimentas são uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        elif textsolo == 5 and (colescolha == 3 or mescolheita == 1 or mescolheita == 3 or mescolheita == 4):
            print("Alface é uma ótima escolha para a sua plantação! Caso queira mais opções, consulte com nossa IA.")
        else: 
            print("Consulte com nossa IA resultados específicos para a sua colheita.")
        
        print("Esses resultados são apenas uma prévia! Para mais informações, consulte nossa IA na aba de seu perfil.")
        answer = input("Você gostaria de refazer nosso questionário?[S/N] ").upper().strip()[0]                                
        ''' todas as informações dadas acima (resultados) foram baseados em pesquisas no site da EMBRAPA (Empresa Brasileira de Pesquisa Agropecuária)'''

except ValueError:
    print(erro)

print("Fim de programa")