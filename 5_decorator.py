def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if type(result) is int:
            print('Простое')
        else:
            print('Составное')
        return result

    return wrapper


@is_prime
def sum_three(num1=0, num2=0, num3=0):
    num_list = [num1, num2, num3]
    return sum(num_list)


sum_result = sum_three(52, 79, 17)
print(sum_result)
