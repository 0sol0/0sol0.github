## class
```python
class Review:
    title = ''
    content = ''
    user = ''
    
    def __init__(self, title=title, content=content, user=user) -> None:
        self.title = title
        self.content = content
        self.user = user

review = Review(title='제목', content='내용', user='사용자')
review1 = Review(title='제목1', content='내용1', user='사용자1')
review2 = Review(title='제목2', content='내용2', user='사용자2')
```

## db
SQL : db조작을 위한 언어
Queryset형식 data

`sqlite test`
```sql
CREATE TABLE Review (
    "ID" INTEGER NOT NULL
    "Title" TEXT NOT NULL
    "Content" TEXT NOT NULL
    "User" TEXT NOT NULL
    PRIMARY KEY("ID" AUTOINCREMENT)
);
INSERT INTO Review  (ID, Title, Content, User)
VALUES (1, '제목', '내용', '사용자');
SELECT * FROM Review
1|제목|내용|사용자
```
스키마 : table의 구조
필드 : 각 변수
레코드 : 변수 값

## ORM(Object Relational Mapping)
class에 있는 데이터들을 SQL 형식으로 바꿔서 저장해주는 것
models.py에서 ()안에 넣는 것 = class로 된 코드를 SQL로 바꿀 때 SQL이 알아들을 수 있도록 필요한 정보를 넣는 것

models.py
```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
```

SQL
```sql
BEGIN;
--
-- Create model Article
--
CREATE TABLE "articles_article" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    "title" varchar(10) NOT NULL, 
    "content" text NOT NULL, 
    "create_at" datetime NOT NULL
    );
COMMIT;
```
