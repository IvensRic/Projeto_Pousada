#Universidade Mogi das Cruzes
#Aluno: Ivens Richard Rodrigues da Silva - RGM: 11252100378
#Aluno: Caue Sena Santos - RGM: 11252100698
#Atividade avaliativa da matéria Software Básico.
import os

#ESPAÇO CRIATIVO.
#cores
resetar = "\033[0m"
amarelo = "\033[0;33m"
vermelho = "\033[0;31m"
azul = "\033[0;34m"
verde = "\033[0;32m"
ciano = "\033[0;36m"
azul_negrito = "\033[1;34m"
amarelo_negrito = "\033[1;33m"
branco_negrito = "\033[1;37m"
verde_negrito = "\033[1;32m"

#Divisorias
div = (f"---"*25)
div2 = (f"==="*25)

Tit = (f'''{ciano}
 _______     ___   _____  _____   ______        _       ______        _       
|_   __ \  .'   `.|_   _||_   _|.' ____ \      / \     |_   _ `.     / \      
  | |__) |/  .-.  \ | |    | |  | (___ \_|    / _ \      | | `. \   / _ \     
  |  ___/ | |   | | | '    ' |   _.____`.    / ___ \     | |  | |  / ___ \    
 _| |_    \  `-'  /  \ \__/ /   | \____) | _/ /   \ \_  _| |_.' /_/ /   \ \_  
|_____|    `.___.'    `.__.'     \______.'|____| |____||______.'|____| |____| 
{resetar}''')

valores = (f'''
           {azul_negrito}> Bem-vindo ao sistema de cotação e reservas!{resetar}

             +--------------------------------------+
             | {azul}Hóspedes{resetar} |   {azul}Comum{resetar}   |   {azul}Executivo{resetar}   |                                           
             |    {ciano}1{resetar}     | {verde}R$ 20.00{resetar}  |    {verde}R$ 25.00{resetar}   |
             |    {ciano}2{resetar}     | {verde}R$ 28.00{resetar}  |    {verde}R$ 34.00{resetar}   |
             |    {ciano}3{resetar}     | {verde}R$ 35.00{resetar}  |    {verde}R$ 42.00{resetar}   |
             |    {ciano}4{resetar}     | {verde}R$ 42.00{resetar}  |    {verde}R$ 50.00{resetar}   |
             |    {ciano}5{resetar}     | {verde}R$ 48.00{resetar}  |    {verde}R$ 57.00{resetar}   |
             |    {ciano}6{resetar}     | {verde}R$ 53.00{resetar}  |    {verde}R$ 63.00{resetar}   |
             +--------------------------------------+                      
''')

Sub = (f'''
{amarelo_negrito}> Aqui você poderá:{resetar}
    {branco_negrito}1. Cadastrar o nome do colaborador responsável.
    2. Escolher o tipo de apartamento:
        - (1) Comum
        - (2) Executivo
    3. Definir a quantidade de hóspedes (mín. 1 | máx. 6).
    4. Selecionar o período de hospedagem (mín. 1 | máx. 7 dias).
    5. Gerar a cotação final da estadia.{resetar}
{amarelo_negrito}> Preencha os campos abaixo.{resetar}\n''')

print(Tit)
print(valores)
print(Sub)

#Entrada de dados

tabela = {     #Tabela de valores.
    1: (20.00, 25.00),
    2: (28.00, 34.00),
    3: (35.00, 42.00),
    4: (42.00, 50.00),
    5: (48.00, 57.00),
    6: (53.00, 63.00)
}

while True:

    while True:
        nome = str(input(f"{branco_negrito}Nome do colaborador: {resetar}"))
        if nome.replace(' ', '').isalpha() and len(nome) > 0:
            break           #.replace remove os espaços, .isalpha Verifica se tem apenas letras, len(nome) > 0 confirma se não está vazio.
        else:
            print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Nome deve conter apenas Letras.{resetar}")

    while True: #Escolha do tipo de Ap.
        try:
            print(f'''{branco_negrito}Escolher o tipo de apartamento:
         (1) Comum
         (2) Executivo
                  {resetar}''')
            ap = int(input(f"{branco_negrito}Escolha entre 1 ou 2: {resetar}"))
            if ap in [1,2]:
                break
            else:   #Detecção de possiveis erros.
                print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}O Tipo de apartamento deve ser 1 ou 2.{resetar}\n")
        except ValueError:
            print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Digite apenas números (opções 1 ou 2){resetar}\n")

    while True: #Total de hóspedes.
        try:
            num_pessoas = int(input(f"{branco_negrito}> Quantidade de pessoas (Min.1 | Máx.6): {resetar}"))
            if 1 <= num_pessoas <= 6:
                break
            else:   #Detecção de possiveis erros.
                print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Mínimo de 1 e máximo de 6 hóspedes.{resetar}\n")
        except ValueError:
            print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Digite apenas números (Entre 1 e 6).{resetar}\n")

    while True: #Periodo de hospedagem.
        try:
            num_dias = int(input(f"{branco_negrito}> Quantidade de dias (Min.1 | Máx.7) {resetar}"))
            if 1<= num_dias <=7:
                break
            else:   #Detecção de possiveis erros.
                    print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Escolha entre 1 e 7 dias.{resetar}\n")
        except ValueError:
            print(f"{vermelho}*Informação inválida!*{resetar} {branco_negrito}Digite apenas numeros (Entre 1 e 7).{resetar}\n")
    
    Confirmacao = input(f"Pressione {verde}ENTER{resetar} para prosseguir com a cotação ou pressione '{vermelho}C{resetar}' para corrigir: ").lower()   
    if Confirmacao == "c":      #Confirmação de cotação.                                                                                   #.lower() converte as letras para minusculas.
        continue
    else:
        pass

    #Processamento de dados
    preço_pessoa = tabela[num_pessoas] #Busca na tabela o número de pessoas.
    ind_preço = ap - 1  #Calcula o indice.

    preço_diaria_por_pessoa = preço_pessoa[ind_preço] #Pega o preço por pessoa baseado no tipo do ap.
    valor_diaria_total = preço_diaria_por_pessoa * num_pessoas  #Calcula o valor da diaria por pessoa.
    valor_total = valor_diaria_total * num_pessoas  #Calcula o valor total da estadia.

    #Saída de dados
    os.system("cls")

    print(Tit)
    print()
    print(f"{ciano}{div2} {resetar}\n")

    print(f"{vermelho} >> Conferência de informações << {resetar}\n")
    print(f"Colaborador: {azul}{nome}{resetar}\n")      #Exibe nome do colaborador.
    print(f"Escolha de apartamento: {azul}Tipo {ap} {resetar}\n")       #Exibe a escolha de do ap.
    print(f"Total de {azul}{num_pessoas}{resetar} hóspedes\n")      #Exibe quantidade de hóspedes.
    print(f"Período de hospedagem total de {azul}{num_dias} dias{resetar}\n")       #Exibe quantidade de dias.
    print(f"{ciano} {div} {resetar}\n")

    print(f"{vermelho}>>> Cotação Final <<<{resetar}\n")
    print(f"Valor da diária: {verde_negrito}R${preço_diaria_por_pessoa:.2f} {resetar}")     #Exibe valor do dia conforme o tipo do ap.
    print(f"Valor da diária total ({azul}{num_pessoas} pessoas{resetar}): {verde_negrito}R${valor_diaria_total:.2f}{resetar}")      #Exibe total da diaria com base na quantidade de hospedes.
    print(f"Valor total para {azul}{num_dias}{resetar} dias: {verde_negrito}R${valor_total:.2f}{resetar}\n")        #Exibe o total conforme os dias e hóspedes escolhidos.
    print(f"{ciano} {div2} {resetar}\n")

    opção = input(f"Pressione '{verde}S{resetar}' para prosseguir com a reserva, ou '{vermelho}R{resetar}' para recomeçar: ").lower()
    print(F"{ciano}{div}{resetar}")                 #Possibilidade de fazer uma nova cotação.
    if opção == "r":    
        continue
    elif opção == "s":
        print(f"{vermelho}EM MANUTENÇÃO{resetar}\n")        #Abre a oportunidade para continuidade.
        break
    else:
        continue
