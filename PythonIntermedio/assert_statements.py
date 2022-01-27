def divisor(num):
    assert num > 0, "Debes ingresar un número mayor a 0"
    return [i for i in range(1, num+1) if num % i == 0]

def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisor(int(num)))


if __name__ == '__main__':
    run()