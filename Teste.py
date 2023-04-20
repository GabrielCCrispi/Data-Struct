Anoversario = input("Digite o ano que você nasceu: ")
Mesversario = input("Digite o mês que você nasceu: ")
AnoAtual = input("Digite o ano atual: ")

Ano = int(AnoAtual) - int(Anoversario)

if int(Mesversario) < 6:
    print(f"Você tem {Ano} anos") 
else:
    print(f"Você tem {Ano -1} anos") 
      
    