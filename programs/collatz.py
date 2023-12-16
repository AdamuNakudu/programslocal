
import sys

try:
    number = int(input('Integer: '))
except:
    print('not an integer')
    sys.exit()

def collatz(divideBy):
    try:
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            result = 3 * number + 1
            print(result)
            return result
            
    except:
        print('error')

while number != 1:
    number = collatz(number)
    

    
    