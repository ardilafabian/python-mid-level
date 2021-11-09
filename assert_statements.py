def divisors(num):
    # return [i for i in range(1,num+1) if num%i == 1]
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def main():
    num = input('Ingresa un número: ')
    assert num.isnumeric(), 'Es un número lo que se espera'
    print(divisors(int(num)))
    print('terminó mi programa')

if __name__=='__main__':
    main()