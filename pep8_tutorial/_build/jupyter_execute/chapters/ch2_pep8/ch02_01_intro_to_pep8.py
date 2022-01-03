#!/usr/bin/env python
# coding: utf-8

# # PEP 8 소개 (Introduction to PEP 8)

# 
# ```{figure} ../../imgs/pep8_overview_table.jpg
# ---
# width: 550px
# align: center
# name: pep8Table
# ---
# PEP 8 정리한 표
# ```

# ```{note}
# PEP 8은 아래 링크를 참고하세요.
# 
# **PEP 1**: https://www.python.org/dev/peps/pep-0008
# ```

# - PEP 8은 main 파이썬 배포판에서 표준 라이브러리를 준수하는 파이썬 코드에 대한 컨벤션(convention)을 제공합니다.
# - 파이썬은 C 언어로 만들어졌기 때문에 파이썬을 만든 C 언어로 코딩하는 스타일은 PEP 7을 참고할 수 있습니다.
#     - C 언어는 파이썬과 친구 관계지만, 이번 튜토리얼에서는 C 언어 관련 사항은 생략합니다.
#     - 관심있는 사람은 아래 링크를 참고하기 바랍니다.
#     - PEP 7: https://www.python.org/dev/peps/pep-0007
# 
# ```{admonition} 컨벤션(convention)
# 많은 개발자들이 관용적으로 사용하여, 하나의 스타일로 정형화된 코딩 방식
# ```

# - PEP 8은 귀도 반 로섬에 의해 최초로 제안된 Docstring Convention ([PEP 257](https://www.python.org/dev/peps/pep-0257/))과 [Barry's GNU Mailman style guide](http://barry.warsaw.us/software/STYLEGUIDE.txt)의 일부가 반영되어 작성된 코딩 스타일 가이드입니다.

# - 파이썬 코딩 스타일은 추가적인 컨벤션(convention)이 식별될 때마다 지속적으로 진화하고 있습니다.
# - 파이썬 과거 버전은 언어 자체의 변화가 있는 경우 더 이상 반영하지 않습니다.
#     - 종결처리(obsolete) 예시
#         - Python 2 에 있고, Python 3에 반영되지 않는 경우
#         - Pyton 3가 진화하면서 없어지는 문법들

# - 대부분의 프로그래밍 언어는 그 자신만의 코딩 스타일을 가지고 있습니다.
# - 다른 언어와 파이썬 사이에서 코딩 스타일의 충돌(conflicts)가 존재하는 경우는 해당 프로젝트에서 정한 규칙을 우선적으로 사용하는 것이 좋습니다.
