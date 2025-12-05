for i in range(3, 0, -1):
    A = input()
    if A not in ['Fizz', 'Buzz', 'FizzBuzz']:
        N = int(A)+i

if N%3 == 0 and N%5 == 0:
    print('FizzBuzz')
elif N%3 == 0 and N%5 != 0:
    print('Fizz')
elif N%3 != 0 and N%5 == 0:
    print('Buzz')
else:
    print(N)