import random
number = random.randint(0,20)
print("                   ---- Welcome to the Guessing Game!! ----   created by Lucas Santana")
guessNumber = input("Digite um número entre 0 e 20: ")

while guessNumber == '':
    guessNumber = input("Por favor, digite um NÚMERO entre 0 e 20: ")

guessNumber = int(guessNumber)

def guess(text):
    num = input(text)
    while num == '':
        num = input("Por favor, digite um NÚMERO entre 0 e 20: ")
    num=int(num)
    return num

def verify(num):
    while num>20 or num<0:
            print("Seu número está incorreto!")
            num = input("Por favor, digite um número entre 0 e 20: ")
            while num == '':
                num = input("Por favor, digite um NÚMERO entre 0 e 20: ")
            num=int(num)

    return num

verify(guessNumber)

c=1

while guessNumber != number:
    if guessNumber < number:
        print("Digite um número maior para acertar ")
        guessNumber = guess("")
        verify(guessNumber)
        c+=1
    
    elif guessNumber > number:
        print("Digite um número menor para acertar ")
        guessNumber = guess("")
        verify(guessNumber)
        c+=1

            
if guessNumber == number:
    print("Parabéns! Você acertou o número sorteado!")
    print("Você preisou de",c,"tentativas no total")