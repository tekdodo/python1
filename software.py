 import random

print("@@@ JOGO DA ADIVINHAÇÃO @@@")
print("Adivinhe o número que estou pensando, de 1 a 10")
limite_tentativas = 3
tentativa = 1
while (limite_tentativas >= tentativa):
    print("tentativa", tentativa)
    tentativa = tentativa + 1
chute = int(input("Digite o seu chute:", tentativa, ":"))
print(sorteio)
print(chute)

if (chute == sorteio)
    print("Parabéns, você acertou o número era", sorteio)
if (chute != sorteio):
    print("Você errou! O número era", sorteio)