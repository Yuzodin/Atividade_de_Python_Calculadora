def soma(n1,n2):
    r = n1+n2
    return r

def sub(n1,n2):
    r = n1-n2
    return r 

def mul(n1,n2):
    r = n1*n2
    return r

def div(n1,n2):
    r = n1/n2
    return r
x = 0
op =0
v = []
while op != 5 and x != 10:
    print('-'*12)
    print('CALCULADORA')
    print('-'*12)

    op = input('''
    Escolha qual opção deseja realizar na calculadora:
    1 para Adição
    2 para subtração
    3 para multiplicação
    4 para Divisão
    5 para Sair da caluladora                                 
    ''')
    if op == '5':
        break;
    elif op < '6':
      
        n1= int (input ('Digite o primeiro numero: '))
        n2= int (input ('Digite o segundo numero: '))

        if op == '1':
            print ('{} + {} = {}'. format(n1,n2, n1+n2))
            r = soma(n1,n2)
            
        elif op == '2':
            print('{} - {} = {}'.format(n1, n2, n1-n2))
            r = sub(n1,n2)

        elif op == '3':
            print('{} * {} = {}'.format(n1,n2,n1*n2))
            r = mul(n1,n2)

        elif op == '4':
            print('{} / {} = {}'.format(n1, n2,n1/n2))
            r = div(n1,n2)
        
        v.append(r)
    else: 
        print('Opção digitada não encontrada tente novamente.')
        x+x+10
print (v)