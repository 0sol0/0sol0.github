// console.log(변수) 는, 콘솔 창에 괄호 안의 값을 출력해줍니다.
// 개발자가 결과값을 보기 편하도록!

// console.log(변수1,변수2) 로 여러 변수를 한번에 출력할 수도 있어요.
// 아래를 복사해서 붙여넣어보세요.

console.log("Hello World!");

let num = 20
num = 'Bob'

// 변수는 값을 저장하는 박스예요.
// 한 번 선언했으면, 다시 선언하지 않고 값을 넣습니다.

let a = 1
let b = 2

a+b // 3
a/b // 0.5

let first = 'Bob'
let last = 'Lee'

first+last // 'BobLee'

first+' '+last // 'Bob Lee'

first+a // Bob1 -> 문자+숫자를 하면, 숫자를 문자로 바꾼 뒤 수행합니다.

let first_name = 'bob' // snake case라고 합니다.

// 또는,

let firstName = 'bob' // camel case라고 합니다. 회사마다 규칙이 있죠.

// 과 같이, 쉽게 알아볼 수 있게 쓰는 게 중요합니다.
// 다른 특수문자 또는 띄워쓰기는 불가능합니다!

let a_list = []  // 리스트를 선언. 변수 이름은 역시 아무렇게나 가능!

// 또는,

let b_list = [1,2,'hey',3] // 로 선언 가능

b_list[1] // 2 를 출력
b_list[2] // 'hey'를 출력

// 리스트에 요소 넣기
b_list.push('헤이')
b_list // [1, 2, "hey", 3, "헤이"] 를 출력

// 리스트의 길이 구하기
b_list.length // 5를 출력

let a_dict = {}  // 딕셔너리 선언. 변수 이름은 역시 아무렇게나 가능!

// 또는,

let b_dict = {'name':'Bob','age':21} // 로 선언 가능
b_dict['name'] // 'Bob'을 출력
b_dict['age'] // 21을 출력

b_dict['height'] = 180 // 딕셔너리에 키:밸류 넣기
b_dict // {name: "Bob", age: 21, height: 180}을 출력

names = [{'name':'bob','age':20},{'name':'carry','age':38}]

// names[0]['name']의 값은? 'bob'
// names[1]['name']의 값은? 'carry'

new_name = {'name':'john','age':7}
names.push(new_name)

// names의 값은? [{'name':'bob','age':20},{'name':'carry','age':38},{'name':'john','age':7}]
// names[2]['name']의 값은? 'john'

// 예를 들면, '나눗셈의나머지'를 구하고 싶은 경우

let a = 20
let b = 7

a % b = 6

// 또, 모든 알파벳을 대문자로 바꾸고 싶은 경우

let myname = 'spartacodingclub'

myname.toUpperCase() // SPARTACODINGCLUB

// 또, 특정 문자로 문자열을 나누고 싶은 경우

let myemail = 'sparta@gmail.com'

let result = myemail.split('@') // ['sparta','gmail.com']

result[0] // sparta
result[1] // gmail.com

let result2 = result[1].split('.') // ['gmail','com']

result2[0] // gmail -> 우리가 알고 싶었던 것!
result2[1] // com

myemail.split('@')[1].split('.')[0] // gmail -> 간단하게 쓸 수도 있다!

// 특정 문자로 나누고 싶은 경우 2

let txt = '서울시-마포구-망원동'

let names = txt.split('-'); // ['서울시','마포구','망원동']

// 특정 문자로 합치고 싶은 경우

let result = names.join('>'); // '서울시>마포구>망원동' (즉, 문자열 바꾸기!)

// 만들기
// function 함수이름(필요한 변수들) {내릴 명령들을 순차적으로 작성}
// 사용하기 = 함수이름(필요한 변수들);

// 두 숫자를 입력받으면 더한 결과를 돌려주는 함수
function sum(num1, num2) {
	console.log('num1: ', num1, ', num2: ', num2);
	return num1 + num2;
}

sum(3, 5); // 8
sum(4, -1); // 3

function is_adult(age){
	if(age > 20){
		alert('성인이에요')
	} else {
		alert('청소년이에요')
	}
}

is_adult(25)

function is_adult(age){
	if(age > 20){
		alert('성인이에요')
	} else if (age > 10) {
		alert('청소년이에요')
	} else {
		alert('10살 이하!')
	}
}

is_adult(12)

// AND 조건은 이렇게
function is_adult(age, sex){
	if(age > 20 && sex == '여'){
		alert('성인 여성')
	} else if (age > 20 && sex == '남') {
		alert('성인 남성')
	} else {
		alert('청소년이에요')
	}
}

// 참고: OR 조건은 이렇게
function is_adult(age, sex){
	if (age > 65 || age < 10) {
		alert('탑승하실 수 없습니다')
	} else if(age > 20 && sex == '여'){
		alert('성인 여성')
	} else if (age > 20 && sex == '남') {
		alert('성인 남성')
	} else {
		alert('청소년이에요')
	}
}

is_adult(25,'남')

console.log(0)
console.log(1)
console.log(2)
console.log(3)
console.log(4)
console.log(5)

console.log(99)

// 이렇게 쓰기엔 무리가 있겠죠? 그래서, 반복문이라는 것이 존재합니다!

for (let i = 0; i < 100; i++) {
	console.log(i);
}

// for (1. 시작조건; 2. 반복조건; 3. 더하기) {4. 매번실행}

// 1 -> 2체크하고 -> (괜찮으면) -> 4 -> 3
// -> 2체크하고 -> (괜찮으면) -> 4 -> 3
// -> 2체크하고 -> (괜찮으면) -> 4 -> 3
// -> 2체크하고 -> (괜찮으면) -> 4 -> 3

// 와 같은 순서로 실행됩니다.
// i가 증가하다가 반복조건에 맞지 않으면, 반복을 종료하고 빠져나옵니다.

let people = ['철수','영희','민수','형준','기남','동희']

// 이렇게 하면 리스트의 모든 원소를 한번에 출력할 수 있겠죠?
// i가 1씩 증가하면서, people의 원소를 차례대로 불러올 수 있게 됩니다.
for (let i = 0 ; i < people.length ; i++) {
	console.log(people[i])
}

let scores = [
	{'name':'철수', 'score':90},
	{'name':'영희', 'score':85},
	{'name':'민수', 'score':70},
  {'name':'형준', 'score':50},
  {'name':'기남', 'score':68},
  {'name':'동희', 'score':30},
]

for (let i = 0 ; i < scores.length ; i++) {
	console.log(scores[i]);
}

// 이렇게 하면 리스트 내의 딕셔너리를 하나씩 출력할 수 있고,

for (let i = 0 ; i < scores.length ; i++) {
	if (scores[i]['score'] < 70) {
		console.log(scores[i]['name']);
	}
}

// 이렇게 하면 점수가 70점 미만인 사람들의 이름만 출력할 수도 있습니다.

document.getElementById("element").style.display = "none";

$('#element').hide();