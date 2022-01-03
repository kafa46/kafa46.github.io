#!/usr/bin/env python
# coding: utf-8

# # When to Use Trailing Commans (콤마를 마지막에 사용하는 경우)

# 파이썬 코딩에서 어떤 문(statement)에서 콤마를 사용하는 것은 선택사항입니다.
# 
# 다만, 튜플을 만들때 콤마를 사용하는 것은 선택이 아니라 필수 입니다.
# 
# 일반적으로 명료함을 추구하기 위해 괄호로 묶어서 사용하는 것을 추천합니다.

# - 좋은 예

# In[1]:


FILES = ('setup.cfg',)


# - 나쁜 예

# In[2]:


FILES = 'setup.cfg',


# 값을 여러개 나열하거나, 여러개의 인자를 선언하는 등 마지막 콤마가 여러개 이어질 경우, 유지보수 단계에서 값을 추가하거나 삭제하고 디폴트 값을 변경해야 하는 경우가 발생합니다. 이 경우 한줄로 코딩해 놓으면 유지보수가 힘들고 가독성이 떨어지게 됩니다. 
# 
# 이 경우에는 괄호를 분할하여 여러줄에 걸쳐 사용하는게 좋습니다.

# - 좋은 예

# In[3]:


FILES = [
    'setup.cfg',
    'tox.ini',
    ]

initialize(FILES,
           error=True,
           )


# - 나쁜 예

# In[ ]:


FILES = ['setup.cfg', 'tox.ini',]
initialize(FILES, error=True,)


# ---
