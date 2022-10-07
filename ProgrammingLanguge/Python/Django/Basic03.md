## Django 기본 기능
## 우리가만든 User 모델 업그레이드 하기
### class
```Python
class A:
    def 기능_A_1:
        return '기능 A_1'
    def 기능_A_2:
        return '기능_A_2'

class B:
    def 기능_B_1:
        return '기능_B_1'
```

```Python
class B(A):
    def 기능_B_!:
        return '기능_B_1'
```

user/models.py
```Python
from django.contrib.auth.models import AbstractUser

class UserModel(AbstractUser):
    class Meta:
        db_table = 'my_user'

    bio = models.CharField(max_length=256, default='')
```

web_project/setting.py
```python
AUTH_USER_MODEL = 'user.UserModel'
```

## Django의 사용자 모델을 적용하기 - 회원가입 수정하기

## Django의 사용자 모델을 적용하기 - 로그인 수정하기