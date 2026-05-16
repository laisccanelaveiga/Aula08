# def calcular_desconto(vlr_comp):
#     desconto = vlr_comp * 0.16
#     vlr_total = vlr_comp - desconto
#     return vlr_total, desconto

# compra = float(input("Informe o valor da compra: "))

# if compra > 250:
#     total, desconto = calcular_desconto(compra)
#     print(f'Compra: R$ {compra:.2f}')
#     print(f'Desconto: R$ {desconto:.2f}')
#     print(f'Total: R$ {total:.2f}')
# else:
#     print("Não haverá desconto")
#     print(f'Compra: R$ {compra:.2f}')


def calc_desc(compra):
    if compra > 250:
        desc = compra * 0.16
        tot = compra - desc
    else:
        desc = 0
        tot = compra
        
    return tot , desc


vlr_compra = float(input("Informe o valor da compra: "))
total, desconto = calc_desc(vlr_compra)

print(f'Valor da Compra: {vlr_compra:.2f}')
print(f'Valor do Desconto: {desconto:.2f}')
print(f'Valor do Total: {total:.2f}')



    