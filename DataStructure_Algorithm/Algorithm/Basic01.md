## 최댓값 구하기
### Case 1
```Python
input_ = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    for num in array:
        for compare_num in array:
            if num < compare_num:
                break
            else:
                return num

result = find_max_num(input_)
print(result)
```

##3 Case 2
```Python
input_ = [3, 5, 6, 1, 2, 4]

def find_max_num(array):
    max_num = array[0]
    for num in array:
        if num > max_num:
            max_numm = num

    return max_num

result = find_max_num(input_)
```

## 최빈값 구하기
###
```Python
def find_alphabet_occurrence_array(string):
    alphabet_occurrence_array = [0] * 26
        for i, s in enumerate(string):
            if s[i].isalpha():
                index = ord(s[i]) - ord('a')
                    alphabet_occurrence_array[index] += 1
                    max_num = alphabet_occurence_array[0]
                    if s > max_num:
                            max_num = s
                
                retrun max_num
                

    return alphabet_lccurrence_array

print(find_alphabet_occurrence_array('Hello my name is sparta'))
```

### Case
```python
def find_alphabet_occurrence_array(string):
    aphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1

    return alphabet_occurrence_array

print(find_alphabet_occurrence_array('Hello my name is sparta'))
```

### Case 1
```Python
def find_max_occurred_alphabet(string):
    alphabet_arry = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 
                    'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
                    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                
    max_occurrence = 0
    max_alphabet = alphabet_array[0]

    for alphabet in alphabet_array:
        occurrence = o
        for char in string:
            if cahr == alphabet:
                occurrence += 1
        
        if occurrence > max_occurrence:
            max_occurrence = occurrence
            max_alphabet = alphabet
        
    return max_alphabet

result = find_max_occurred_alphabet(input)
print(result)
```

### Case 2
```Python
def find_max_occurred_alphabet(string):
    aphabet_occurrence_array = [0] * 26
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
        
        max_occurrence = 0
        max_alphabet_index = 0

        for index in range(len(alphabet_occurrence_array)):
            alphabet_occurrence = alphabet_occurrence_array[index]

            if alphabet_occurrence > max_occurrence:
                max_ooccurrence = alphabet_occurrence
        return chr(max_alphabet_index + ord('a'))


```

```Python
def is_number_exist(number, array):
    for element in arry:
        if number == element:
            return True
    
    return False

result = is_number_exist(3, input)
print(result)
```

 ```Python
def find_max_plus_or_multiply(array):
    multiply_sum = 0
    for number in array:
        if number <= 1 or multiply_sum <= 1:
            multiply_sum += number
        else:
            multiply_sum *= number

    return num

result = find_max_plus_or_multiplly(input)
print(result)
 ```

 ```Python
input = 'abadabac'
def find_not_repeating_first_character(string):
        alphaet_occurrence_array = [0] * 26

        for char in string:
            if not char.isalpha():
                continue
            arr_inddex = ord(char) - ord('a')
            alphaet_occurrence_array[arr_index] += 1
        
        not_repeating_character_array = []
        for index in range(len(alphabet_coccurrence_array)):
            alphabet_occurrence = alphabet_occurrence_array[index]
            if alphabet_occurrence ==1:
                not_repeating_character_array.append(chr(ord(index) + ord('a')))
        
        for char in string:
            if char in not_repeating_character_array:
                return char

        return '_'

result = find_not_repeating_first_character(input)
print(result)
 ```
## 시간복잡도
인자 = N
조건문, 대입, 비교 += 1
반복문 *= len(인자)

## 공간복잡도
인자의 길이 += len(인자)
변수 += 1

## 점근 표기법
빅오 : 최악의 성능이 나올 때
빅오메가 : 최선의 성능이 나올 때
