#!/usr/bin/env python
# coding: utf-8

# # White Space (공백 문자)

# ---

# ## Pet Peeves

# Pet Peeves는 애완동물(pet)을 입양했더니 짜증(peev)을 유발한다는 것에서 유래한 말이라고 합니다. 강아지를 입양했더니 여기저기 어지르는 상황이 예가 될 것 같습니다. 의역하면 "내가 싫어하는 것", "불쾌한 것", "화나는 것" 정도로 해석하면 될 것 같습니다.

# 파이썬에서 기본 원칙으로 제시하는 것은 "공백을 남용하지 말자" 입니다. 공백은 꼭 필요한 곳에 필요한 만큼만 쓰면 됩니다. 
# 몇가지 예제를 살펴보도록 하겠습니다.

# ### 괄호를 사용하는 경우는 괄호 안에 불필요한 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


spam(ham[1], {eggs: 2})


# - 나쁜 예

# In[ ]:


spam( ham[ 1 ], { eggs: 2 } )


# ### 괄호에서 콤마를 마지막에 사용하는 경우 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


foo = (0,)


# - 나쁜 예

# In[ ]:


bar = (0,  )


# ### 콤마( , ), 세미콜론( ; ), 콜론( : ) 바로 앞에는 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


if x == 4: print x, y; x, y = y, x


# - 나쁜 예

# In[ ]:


if x == 4 : print x , y ; x , y = y , x


# ### 슬라이싱에서 콜론이 이항 연산자와 같이 사용된다면 콜론 기준으로 양쪽에 동일한 스페이스를 줍니다.

# - 좋은 예

# In[ ]:


ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]


# - 나쁜 예

# In[ ]:


ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]


# ### 함수의 인자를 표시하는 괄호의 경우 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


spam(1)


# - 나쁜 예

# In[ ]:


spam (1)


# ### 인덱싱이나 슬라이싱에 괄호를 사용하는 경우 시작 부분에 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


dct['key'] = lst[index]


# - 나쁜 예

# In[ ]:


dct ['key'] = lst [index]


# ### 대입 연산자( = ) 한칸의 공백만 줍니다. 변수 정렬을 위해 불필요한 공백은 사용하지 않습니다.

# - 좋은 예

# In[ ]:


x = 1
y = 2
long_variable = 3


# - 나쁜 예

# In[ ]:


x             = 1
y             = 2
long_variable = 3


# ## Other Recommendations

# ### 연산자와 관련한 공백

# 코딩 파일 전반에 걸쳐 명령어의 마지막에 불필요한 공백을 남겨놓지 않도록 합니다.
# 왜냐하면 한 줄의 마지막에 공백이 있을 경우 눈에 보이지 않기 때문에 혼동을 유발할 수 있습니다.
# 
# 대입 연산자 ( = ), 증강 대입 연산자 ( +=, -= 등), 비교 연산자(==, <, >, !=, <>, <=, >=, in, not in, is, is not), 불 연산자 (and, or, not)와 같은 이항 연산자는 전후에 공백을 하나씩 추가합니다.
# 
# 만약 연산자가 괄호와 같은 우선순위를 표시한 구문과 연산자가 같이 쓰인다면 가장 낮은 연산 순위를 갖는 연산자 주변에 공백을 추가합니다. 하지만 이 경우에도 불필요하게 2개 이상의 공백을 추가하지 않는 것이 좋습니다.

# - 좋은 예

# In[ ]:


i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)


# - 나쁜 예

# In[ ]:


i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)


# ### 함수 인자 및 리턴값 관련 공백

# 함수 인자의 자료형을 설명하는 콜론과 함수의 리턴 자료형을 명시하는 설명 연산자 ( -> ) 사이에는 공백을 씁니다.

# - 좋은 예 

# In[ ]:


def foo(input: AnyStr): 
    ...

def foo() -> PosInt: 
    ...


# - 나쁜 예

# In[ ]:


def foo(input:AnyStr): 
    ...

def foo() ->PosInt: 
    ...


# 함수의 키워드 인자값을 지정하기 위한 등호 ( = ) 주변에는 공백을 사용하지 않습니다.

# - 좋은 예

# In[ ]:


def complex(real, imag=0.0):
    return magic(r=real, i=imag)


# - 나쁜 예

# In[ ]:


def complex(real, imag = 0.0):
    return magic(r = real, i = imag)


# 함수 인자의 설명과 디폴트(기본)값을 동시에 사용하는 경우는 등호 ( = ) 주변에 공백을 사용합니다.

# - 좋은 예

# In[ ]:


def foo(sep: AnyStr = None): 
    ...

def foo(input: AnyStr, sep: AnyStr = None, limit=1000): 
    ...


# - 나쁜 예

# 

# In[ ]:


def foo(input: AnyStr=None): 
    ...

def foo(input: AnyStr, limit = 1000): 
    ...


# 여러개의 문(statement, 명령어)을 한줄에 몰아서 쓰는 것은 추천하지 않습니다.

# - 좋은 예

# In[ ]:


if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()


# - 나쁜 예

# In[ ]:


if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()


# 아주 짧은 if문, for문, while문을 사용할 경우 한줄로 코딩하는 것은 괜찮습니다(코드가 간결해지기 때문입니다). 그러나 다수의 조건과 결합되는 코딩을 하는 경우는 긴 라인을 한줄로 표현하면 안됩니다. 가독성이 매우 떨어지게 됩니다.

# - 나쁜 예

# In[ ]:


if foo == 'blah': do_blah_thing()
for x in lst: total += x
while t < 10: t = delay()


# - 더 나쁜 예

# In[ ]:


if foo == 'blah': do_blah_thing()
else: do_non_blah_thing()

try: something()
finally: cleanup()

do_one(); do_two(); do_three(long, argument,
                             list, like, this)

if foo == 'blah': one(); two(); three()


# ---
