def division(number):
    try:
        return 10/number
    except ZeroDivisionError:
        print('Can\'t divide by zero')
    except:
        print('Invalid argument')

print(division(5))      
print(division(1.2))
print(division(0))
print(division(6))
print(division('av'))
