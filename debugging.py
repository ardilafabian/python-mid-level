def divisors(num):
    # return [i for i in range(1,num+1) if num%i == 1]
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    try:
        num = int(input('Ingresa un número: '))
        if num < 0:
            raise ValueError('Numero no puede ser negativo')
        print(divisors(num))
        print('terminó mi programa')
    except ValueError as ve:
        if str(ve) == 'Numero no puede ser negativo':
            print('Debes ingresar un número positivo')
        else:
            print('debes ingresar un número')

if __name__=='__main__':
    main()