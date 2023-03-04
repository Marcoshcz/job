number = int(input('Qual número deseja encontrar? '))

first, second = 0, 1

while first < number:
    first, second = second, first + second

if first == number:
    print('O número {} foi encontrado na sequência'.format(number))
else:
    print('O número {} não foi encontrado na sequência'.format(number))