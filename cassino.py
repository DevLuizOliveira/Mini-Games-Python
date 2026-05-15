import random
import time

def rodar(money):
    money = money - 100
    print(f'\nGastou 100 reais. Saldo atual: {money}')
    
    num1 = random.randint(1, 5)
    num2 = random.randint(1, 5)
    num3 = random.randint(1, 5)
    
    time.sleep(0.5)
    print(f"[{num1}]", end=" ", flush=True)
    time.sleep(0.5)
    print(f"[{num2}]", end=" ", flush=True)
    time.sleep(0.5)
    print(f"[{num3}]")
    
    if num1 == num2 == num3:
        print("PARABÉNS! Você ganhou 1000!")
        money = money + 1000
    else:
        print("Não foi dessa vez...")

    print(f"Saldo final da rodada: R${money}")
    return money

def apostar(money):
    continuar = ""
    while money >= 100 and continuar == "":
        money = rodar(money)
        if money >= 100:
            continuar = input("Pressione [Enter] para rodar ou [x] para parar: ").lower()
    return money

jogar_novamente = "s"
money_acumulado = 0

while jogar_novamente.lower() == "s":
    print(f"\n--- CASSINO PYTHON (Saldo Atual: R${money_acumulado}) ---")
    valor_input = input("Valor para depositar: ")

    if valor_input.isdigit():

        money_da_rodada = int(valor_input) + money_acumulado
        money_acumulado = apostar(money_da_rodada)

        if money_acumulado < 100:
            print(f"\nSaldo de R${money_acumulado} é insuficiente para novas jogadas.")
            jogar_novamente = input("\nDeseja depositar mais? (s/n): ")
        else:
            print(f'\nVocê parou com R${money_acumulado}.')
            jogar_novamente = "n"
        
    else:
        print("Valor inválido! Use apenas números.")

print(f"\nFim de jogo! Você saiu com um total de R${money_acumulado}.")
print("Obrigado por jogar!")
