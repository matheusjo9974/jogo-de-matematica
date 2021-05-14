#importando bibliotecas
import os
from random import randint

#Função que inicia  a interface do programa
def interface():
    print("\n===========================================================\n"
          "---------------BEM VINDO AO JOGO DE MATEMÁTICA-------------\n"
          "===========================================================\n"
          "-----------------------------------------------------------\n"
          "O jogo será sobre perguntas ,de matemática, que ficarão mais\n"
          "dificeis conforme você for acertando, caso você erre muitas\n"
          "perguntas o estágio atual terá de ser  reiniciado. Para co-\n"
          "mpletar o jogo complete todos os estágios. BOA SORTE!!!!!!!\n"
          "-----------------------------------------------------------\n"
          "Digite [sair] e tecle ENTER  a qualquer momento para SAIR.")
    start = input("DIgite [iniciar] e tecle ENTER para INICIAR: ")
    #Bloco condicional que identifica se o usuario quer iniciar o jogo ou sair.
    if start.lower() == "iniciar":
        print("-----------------------------------------------------------\n"
              "------------------------Vamos começar----------------------\n"
              "-----------------------------------------------------------")
        choise_operation()
    elif start.lower() == "sair":
        exit()
    # Caso o valor do usuario for diferente ele trata como incorreto e reinicia o programa.
    else:
        os.system("cls")
        print("\033[31mvalor incorreto. tente novamente\033[m")
        interface()

# Função que de escolha da operação que o usuario quer jogar.
def choise_operation():
    print("Adição[+]----Subtração[-]----Multiplicação[x]----Divisão[/]")
    operation = input("Escolha uma das operações acima e digite seu simbolo: ")
    # Bloco condicional que identifica a operação que o usuario escolheu ou se deseja sair do programa.
    if operation == "+":
        start_stage1()
    elif operation == "-":
        start_stage4()
    elif operation == "x":
        start_stage7()
    elif operation == "/":
        start_stage10()
    elif operation.lower() == "sair":
        exit()
    # Caso o valor não esteja no bloco acima ele define como invalido e chama a função choise_operation() novamente.
    else:
        print("\033[31mSimbolo incorreto. tente novamente.\033[m")
        choise_operation()

# Função que identifica se o usuario digitou um valor numerico ou se deseja sair do programa.
def verify_number(num):
    if num.lower() == "sair":
        return exit()
    try:
        float(num)
        return num
    # Caso seja um valor diferente ele envia uma mensagem de erro e reinicia a função.
    except:
        pass

    print("\033[31mSimbolo invalido. Digite apenas números\033[m")
    return verify_number(input())

# Função que mostra as perguntas que o usuario errou. Caso nao tenha errado ele só continua a programa.
def view_error(box):
    if len(box) != 0:
        print("\033[33mVocê errou as questôes:\033[m", end=" ")
        for i in box:
            print("\033[33m",i ,"\033[m", end=" ")
        print("\n")
    else:
        return

# Função que formata valores de ponto flutuante para apenas uma casa decimal após a virgula.
def truncate(f):
    # Peguei na internet, mas explicarei o que ela faz de uma forma simples.

    n = 1 # numero de casa decimais que eu quero.
    s = '{}'.format(f) # Converte o valor float para string e armazena em s.
    i, p, d = s.partition('.') #s Aqui o float ja convertido em string é particionado em 3 partes. o I recebe a parte inteira, o P recebe o ponto, eo D recebe a parte decimal.
    return '.'.join([i, (d+'0'*n)[:n]])

    # explicação disso |'.'.join([i, (d+'0'*n)[:n]])| em partes
    # |".".join|aqui começa a contenação novamente o ponto será o termo que vai unilos
    # entao voce terá o como resultado final |1°Arg.2°Arg| --- Os parâmetros são passados
    # dentro do join --- |'.'.join([i, |como primeiro parametro temos o 'i' que é a parte
    # inteira do número --- |(d+'0'*n)| completa com zeros caso o numero não tenha as casas
    # decimais desejadas --- |[:n]]| formata para o numero de casas decimais escolhida pelo usuario.
    # e no final fica |'.'.join([i, (d+'0'*n)[:n]])|'''

# Função com o ultimo estagio do caminho da divisão.
def start_stage12():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 03-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(100, 999)
        value2 = randint(100, 999)
        print(lace, "- Questão: quanto é:", value1, "/", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if truncate(answer) == truncate(value1 / value2): # Comparação depois dos valores serem formatados com a truncate().
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mPARABÉNS VOCÊ COMPLETOU ESTE JOGO. !!!!!VOCÊ É DEMAIS!!!!!!\033[m\n"
              "-----------------------------------------------------------")
        exit() # Finaliza o jogo caso ele tenha conseguido alcançar os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage12() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o segundo estagio do caminho da divisão.
def start_stage11():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 02-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(10, 99)
        value2 = randint(10, 99)
        print(lace, "- Questão: quanto é:", value1, "/", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if truncate(answer) == truncate(value1 / value2): # Comparação depois dos valores serem formatados com a truncate().
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage12() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage11() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o primeiro estagio do caminho da divisão.
def start_stage10():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 01-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(0, 9)
        value2 = randint(1, 9)
        print(lace, "- Questão: quanto é:", value1, "/", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if truncate(answer) == truncate(value1 / value2): # Comparação depois dos valores serem formatados com a truncate().
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage11() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage10() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o ultimo estagio do caminho da multiplicação.
def start_stage9():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 03-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(100, 999)
        value2 = randint(100, 999)
        print(lace, "- Questão: quanto é:", value1, "x", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 * value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mPARABÉNS VOCÊ COMPLETOU ESTE JOGO. !!!!!VOCÊ É DEMAIS!!!!!!\033[m\n"
              "-----------------------------------------------------------")
        exit() # Finaliza o jogo caso ele tenha conseguido alcançar os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage9() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o segundo estagio do caminho da multiplicação.
def start_stage8():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 02-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(10, 99)
        value2 = randint(10, 99)
        print(lace, "- Questão: quanto é:", value1, "x", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 * value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage9() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage8() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o primeiro estagio do caminho da multiplicação.
def start_stage7():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 01-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(0, 9)
        value2 = randint(0, 9)
        print(lace, "- Questão: quanto é:", value1, "x", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 * value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage8() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage7() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o ultimo estagio do caminho da subtração.
def start_stage6():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 03-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(100, 999)
        value2 = randint(100, 999)
        print(lace, "- Questão: quanto é:", value1, "-", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 - value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mPARABÉNS VOCÊ COMPLETOU ESTE JOGO. !!!!!VOCÊ É DEMAIS!!!!!!\033[m\n"
              "-----------------------------------------------------------")
        exit() # Finaliza o jogo caso ele tenha conseguido alcançar os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage6() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o segundo estagio do caminho da subtração.
def start_stage5():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 02-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(10, 99)
        value2 = randint(10, 99)
        print(lace, "- Questão: quanto é:", value1, "-", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 - value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage6() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage5() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o primeiro estagio do caminho da subtração.
def start_stage4():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 01-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(0, 9)
        value2 = randint(0, 9)
        print(lace, "- Questão: quanto é:", value1, "-", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 - value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage5() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage4() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o ultimo estagio do caminho da adição.
def start_stage3():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 03-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(100, 999)
        value2 = randint(100, 999)
        print(lace, "- Questão: quanto é:", value1, "+", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 + value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mPARABÉNS VOCÊ COMPLETOU ESTE JOGO. !!!!!VOCÊ É DEMAIS!!!!!!\033[m\n"
              "-----------------------------------------------------------")
        exit() # Finaliza o jogo caso ele tenha conseguido alcançar os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage3() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o segundo estagio do caminho da adição.
def start_stage2():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 02-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(10, 99)
        value2 = randint(10, 99)
        print(lace, "- Questão: quanto é:", value1, "+", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 + value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage3() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage2() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.

# Função com o primeiro estagio do caminho da adição.
def start_stage1():
    global storage_error
    hits = 0
    lace = 1
    storage_error = [] # Vetor apenas para armazenar as perguntas incorretas.
    print("--------------------------STAGE 01-------------------------\n"
          "-----------------------------------------------------------")
    while lace < 6: # Laço que faz as 5 perguntas.
        value1 = randint(0, 9)
        value2 = randint(0, 9)
        print(lace, "- Questão: quanto é:", value1, "+", value2)
        answer = verify_number(input()) # Chamada a função verify_number() que verifica se o que o usuario digitou é um número.
        if int(answer) == value1 + value2: # comparação entre o valor do usuario e a resposta do problema.
            hits += 1
        else:
            storage_error.append(lace)
        lace += 1
    if hits >= 3:
        print("-----------------------------------------------------------\n"
              "você acertou", hits, "de um total de 5 questês.")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("\033[32mParabéns você completou esse estágio, agora seguiremos para\n"
              "o próximo. Boa sorte!!!!!\033[m\n"
              "-----------------------------------------------------------")
        start_stage2() # Chama o proximo estagio caso o usuario tenha conseguido os minimos.
    else:
        print("-----------------------------------------------------------")
        view_error(storage_error) # Chamada a função que mostra os erros passando de parâmetro o vetor.
        print("Infelismente você não conseguiu terá de recomeçar. Boa sorte\n"
              "-----------------------------------------------------------")
        start_stage1() # Reinicia a função caso o usuario nao tenha conseguido alcançar o valor minimo.


# Chamada a função que inicia a interface do programa.
interface()