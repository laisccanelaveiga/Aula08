def calcular_bonus(venda):
    bonus = venda * 0.10
    total = venda + bonus
    return bonus, total 


v = float(input("Insia o valor da venda: "))

if v > 12000:
    b, t = calcular_bonus(v)
    print(f'Venda: R$ {v:.2f}')
    print(f'Bônus: R$ {b:.2f}')
    print(f'Total: R$ {t:.2f}')
else: 
    print("Sem bônus")
    print(f'Venda: R$ {v:.2f}')






