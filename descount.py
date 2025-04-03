Value = float(input('Type a value: '))

def calculate_descount(Value):
    return Value * 0.95


def aplica_desconto(descount):
    print(f'O preço com desconto é R${descount}')

descount = calculate_descount(Value)
aplica_desconto(descount)