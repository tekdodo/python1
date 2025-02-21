import random

print("@@@ JOGO DA ADIVINHAÇÃO @@@")
print("Adivinhe o número que estou pensando, de 1 a 10")
sorteio = random.randint(1,10)
limite_tentativas = 30
tentativa = 1
while (limite_tentativas >= tentativa): # enquanto (ver)
    print("tentativa", tentativa)
   
    chute = int(input("Digite o seu chute:"))

    #se (condição)
    if (chute == sorteio):
        print("Parabéns, você acertou o número era", sorteio)
        break
    elif (chute > sorteio):
        print("Chute um numero menor!")
        break
    elif (chute < sorteio):
        print("Chute um numero maior")
    
    # while (ENQUANTO) VERDADEIRO: EXECUTA OS CODIGOS / FALSO: PARA DE EXECUTAR OS CODIGOS
   
    tentativa = tentativa + 1
