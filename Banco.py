global saldo
saldo = 0

def main():
    print(f'''
Banco Zão

(1) para mostrar
(2) para depositar
(3) para sacar
(0) para sair''')P


def mostrar():
    global saldo
    print(f'Você possui {saldo} reais')
    return saldo


def depositar(valor):
    global saldoP
    saldo += valor
    print(f'Depósito bem sucedido, {valor} reais foram adicionados à sua conta')
    return saldo


def notas(valor):
    valor_nota = [100, 50, 20, 10, 5, 2, 1]
    contador = []  
#contador representa a quantidade de notas, sendo cada posição um valor, começando pelo maior ($100)'
    restos = []
    len_cont = len(valor_nota)

    for x in valor_nota:
        n = valor%x
        restos.append(n)
        m = int(valor/x)
        contador.append(m)
        valor = n

    for y in range(len_cont):
        if contador[y] != 0:
            print(f'{contador[y]} de {valor_nota[y]} reais')


def sacar(valor):
    global saldo
    if saldo < valor or saldo <= 0:
        print(f'Falha no saque, você possui apenas {saldo} reais no momento')
        return saldo

    elif saldo >= valor:
        saldo -= valor
        print('Saque bem sucedido, retire suas cédulas:')
        notas(valor)
        return saldo


while True:
    main()
    numero = int(input('''
Digite uma das opções acima: '''))
    if numero == 1:
        mostrar()

    if numero == 2:
        valor = int(input('''Digite o valor em reais a ser depositado: '''))
        depositar(valor)
    if numero == 3:
        valor = int(input('''Digite o valor em reais a ser sacado: '''))
        sacar(valor)
    if numero == 0:
        print("Obrigado por usar o Banco Zão!")
        break