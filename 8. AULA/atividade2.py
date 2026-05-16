def calc_imc(h,p):
    imc = p / (h * h)
    return imc


altura = float(input('Altura: '))
peso = float(input('Peso: '))

indice = calc_imc(altura,peso)
print(f"\nSeu imc é {indice:.2f}")

if indice > 40:
    print("Obesidade grau III")
elif indice >= 35:
    print("Obesidade grau II")
elif indice >= 30:
    print("Obesidade grau I")
elif indice >= 25:
    print("Acima do peso")
elif indice >= 18.5:
    print("Peso normal")
elif indice >= 17:
    print("Abaixo do peso")
else:
    print('Muito abaixo do peso')
    
