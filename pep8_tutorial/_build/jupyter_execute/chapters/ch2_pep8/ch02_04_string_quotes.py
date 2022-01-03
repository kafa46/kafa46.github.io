#!/usr/bin/env python
# coding: utf-8

# # String Quotes (문자열 따옴표 사용)

# 파이썬 문자열 처리에서 활용하는 작은 따옴표( ' )와 큰 따옴표( " )는 아무런 차이가 없습니다. PEP 8에서는 따옴표 사용에 대한 어떠한 추천 사항도 없습니다. 개발자 각자 문자열 처리에서 따옴표를 사용하는 규칙(습관)을 정하고 일관성 있게 사용하는 것이 중요합니다.

# 하나의 문장에서 작은 따옴표나 큰 따옴표를 사용할 경우 서로 다른 따옴표를 사용하는 것이 좋습니다. 동일한 따옴표를 사용할 경우 백슬래시( \ )를 사용해야 하므로 가독성을 떨어뜨릴 수 있습니다.

# 아래 코드는 정확히 같은 역할을 합니다.

# - 동일한 따옴표를 사용한 예

# In[1]:


print('오늘의 메뉴는 \'갈비탕\' 입니다.')


# - 문자열 처리에서 서로 다른 따옴표를 혼합한 예

# In[2]:


print("오늘의 메뉴는 '갈비탕' 입니다.")


# In[3]:


print('오늘의 메뉴는 "갈비탕" 입니다.')


# 동일한 결과를 얻는 코드지만 두 번째, 세 번째 예제가 가독성이 더 높아집니다. 

# 따옴표 세 개를 사용하는 트리플 따옴표(triple quote, ''')의 내부에서 인용을 하는 경우는 쌍따옴표를 사용하는 것이 좋습니다. 왜냐하면 docstring 컨벤션인 [PEP 257](https://www.python.org/dev/peps/pep-0257/)에서 이미 정의한 내용이기 때문입니다. 어떤 함수의 docstring에서 따옴표를 사용하는 예를 들면 다음과 같습니다.

# In[ ]:


def complex(real=0.0, imag=0.0):
    """Form a complex number.
    Keyword arguments:
    real -- the real part (default 0.0)
    "이 부분은 쌍따옴표를 썼습니다."
    imag -- the imaginary part (default 0.0)
    
    """
    if imag == 0.0 and real == 0.0:
        return complex_zero
    ...


# In[ ]:




