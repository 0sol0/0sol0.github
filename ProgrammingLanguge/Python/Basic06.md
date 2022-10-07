## 함수심화
### option 기본값
```Python
def options(num1=1, num2=2):
  return num1 + num2
result = options(num1, num2)
print(result)
# 3
```

### *args vs **kwargs.
```Python
# 1. *args : 
def add(*args):
    # args = (1, 2, 3, 4)
    result = 0
    for i in args:
        result += i
    return result
print(add())           # 0
print(add(1, 2, 3))    # 6
print(add(1, 2, 3, 4)) # 10

# 2. **kwargs
def set_profile(**kwargs):
    """
    kwargs = {
        name: "lee",
        gender: "man",
        age: 32,
        birthday: "01/01",
        email: "python@sparta.com"
    }
    """
    profile = {}
    profile["name"] = kwargs.get("name", "-")
    profile["gender"] = kwargs.get("gender", "-")
    profile["birthday"] = kwargs.get("birthday", "-")
    profile["age"] = kwargs.get("age", "-")
    profile["phone"] = kwargs.get("phone", "-")
    profile["email"] = kwargs.get("email", "-")
    
    return profile

profile = set_profile(
    name="lee",
    gender="man",
    age=32,
    birthday="01/01",
    email="python@sparta.com",
)
print(profile)
"""
{   
    'name': 'lee',
    'gender': 'man',
    'birthday': '01/01',
    'age': 32,
    'phone': '-',
    'email': 'python@sparta.com'
}
"""

# 3. *args, **kwargs
def print_arguments(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
print_arguments(
    1, # a
    2, # b
    3, 4, 5, 6, # args
    hello="world", keyword="argument" # kwargs
)
"""
1
2
(3, 4, 5, 6)
{'hello': 'hello', 'world': 'world'}
"""
```
