import random
number = random.randint(0,20)
print("                   ---- Welcome to the Guessing Game!! ----   created by Lucas Santana")



def guess_and_verify(): # function to verify and obtain only int inputs between 0 and 20
    while True:
        try: 
            num = int(input("Digite um número entre 0 e 20: "))
            if num>20 or num<0:
                raise ValueError("Seu número não está entre o valor pedido...")
        except ValueError as e:
            print("Valor inválido:",e)
        else:
            break
    return num

guessNumber = guess_and_verify()
c=1

while guessNumber != number:
    if guessNumber < number:
        print("Seu número é MENOR do que o número sorteado")
        guessNumber = guess_and_verify()
        c+=1
    
    elif guessNumber > number:
        print("Seu número é MAIOR do que o número sorteado")
        guessNumber = guess_and_verify()
        c+=1

            
if guessNumber == number:
    print("Parabéns! Você acertou o número sorteado!")
    print("Você preisou de",c,"tentativas no total")