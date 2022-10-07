input = 20

def find_prime_list_under_number(number):
    # 정수 이하의 소수를 반환
    # 소수 : 1 < x, a % b = 0 == 1, x
    for num in range(2, number):
        char = []
        if num % num == 0:
            char.append(num)

    return char 

result = find_prime_list_under_number(input)
print(result)