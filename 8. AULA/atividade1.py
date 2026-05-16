# def limite_pesca(pesc):
#     if pesc > 100:
#         excedente = pesc - 100
#         vlr_exc = excedente * 4
#         print(f"Excedente: R$ {vlr_exc:.2f}")
#     else:
#         vlr_exc = 0
#         print(f'Sem excedente')
#     return vlr_exc


# pescado = float(input("Insira o total pescado: "))
# limite_pesca(pescado)


def excedente_pesca(pescado):
    kilo_exced = pescado - 100
    excedente = kilo_exced * 4
    return excedente, kilo_exced


pesc = float(input("Insira a quantidade pescada: "))

if pesc > 100:
    vlr_exc, kg_excedente = excedente_pesca(pesc)
    print(f'Total de kilos excedidos: {kg_excedente} kg \nValor excedente: R$ {vlr_exc:.2f}')
else:
    print('Não há excedente')