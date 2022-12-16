import random
number = random.randint(0,20)
print("                   ---- Welcome to the Guessing Game!! ----   created by Lucas Santana")



def guess():
    while True:
        try: 
            num = int(input("Digite um NÚMERO entre 0 e 20: "))
            if num>20 or num<0:
                raise ValueError("Seu número está incorreto!")

        except ValueError as e:
            print("Valor inválido:",e)
        else:
            break

    return num

guessNumber = guess()
c=1

while guessNumber != number:
    if guessNumber < number:
        print("Digite um número maior para acertar ")
        guessNumber = guess()
        
        c+=1
    
    elif guessNumber > number:
        print("Digite um número menor para acertar ")
        guessNumber = guess()
        
        c+=1

            
if guessNumber == number:
    print("Parabéns! Você acertou o número sorteado!")
    print("Você preisou de",c,"tentativas no total")