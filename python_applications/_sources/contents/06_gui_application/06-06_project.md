(06-06)=
# Challenge Project

메모장 앱 기능을 확장해 봅니다.

참고 코드 없이 프로젝트에 도전해 보세요 ^^.

아래에 제시된 **힌트**를 적절히 활용한다면 쉽게 해결할 수 있습니다.

직접 고민하고 검색하는 과정에서 많은 것을 배울 수 있습니다!

너무 어렵다면 참고 코드 [여기](../solutions/ch06_solution.md)를 클릭해 주세요.

## 편집 $\to$ 찾기 메뉴 등록

메모장에서 `편집` 메뉴를 만들고, 편집 하부 메뉴로 `찾기` 명령을 등록합니다.

**힌트**

```python
edit_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="편집", menu=edit_menu)
edit_menu.add_command(label="찾기", command=find_text)
```

## `찾기` 메뉴가 클릭되었을 경우 처리

해당 메뉴가 클릭되었을 경우 수행할 `find_text()` 함수를  만듭니다.

**힌트**

`find_text()` 함수는 다음과 같이 구현 가능합니다.
1. 찾을 단어가 있다면 시작위치 `start_pos`을 0번째 글자부터 동일한 문자열이 있는지 찾는다.
2. 찾을 수 없다면 멈춘다.
3. 만약 찾은 문자열이 있다면 `end_pos`을 `end_pos = f"{start_pos}+{len(find_word)}c"`으로 설정한다.
4. 찾은 위치에 `tag_add()` 메서드를 이용하여 `found`라고 마킹한다.
5. 시작 위치를 `end_pos`으로 바꾼다.
6. 1번으로 이동하여 다시 시작한다.
7. 반복이 종료되면 `found`라고 마킹된 부분의 배경색을 변경

```python
def find():
    text_area.tag_remove('found', '1.0', tk.END)
    find_word = find_entry.get()
    if find_word:
        start_pos = '1.0'
        while True:
            # 시작 위치부터 문서의 마지막까지 스캔
            # find_word와 동일한 문자열을 찾았다면 찾은 문자열의 첫글자 인덱스를 리턴
            # 찾지 못했다면 빈 문자열 리턴
            start_pos = text_area.search(find_word, start_pos, stopindex=tk.END)
            if not start_pos:
                break
            # 종료 인덱스 업데이트: 출발 인덱스 + 찾은 문자열의 글자수
            end_pos = f"{start_pos}+{len(find_word)}c"
            # 찾은 문자열의 시작 인덱스와 끝 인덱스에 'found'라고 태그 붙여주기
            text_area.tag_add('found', start_pos, end_pos)
            # 찾은 문자열의 마지막 인덱스를 시작점으로 삼아 다시 탐색 시작
            start_pos = end_pos
        # 'found'라고 태그된 영역의 배경색을 'yellow'로 변경
        text_area.tag_config('found', background='yellow')

tk.Button(find_window, text="찾기", command=find).grid(row=1, column=0, columnspan=2, pady=5)
```

위에서 제시한 힌트를 이용하여 메모장 앱을 업그레이드 해 보세요.

