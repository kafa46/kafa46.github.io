import os

# __file__ 이름을 갖는 파일의 
# 디렉토리를 기본 디렉토리로 설정
# (프로젝트 루트 디렉토리와 동일)
BASE_DIR = os.path.dirname(__file__)

# SQLALCHEMY_DATABASE_URI -> DB 접속 주소
# 프로젝트 루트 디렉토리와 우리가 생성할 DB (hello_cju.db) 연결
# 'sqlite:///' -> 사용할 DB는 SQLite
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(
    os.path.join(BASE_DIR, 'hello_cju.db')
)

# 만약 True 설정된 경우 ORM 객체의 변경사항을
# 지속적으로 추적하고 변동 이벤트에 대한 메시지를 출력함
# True일 경우 추가 메모리를 사용하므로
# 불필요한 경우 False로 꺼놓는 것을 추천함
SQLALCHEMY_TRACK_MODIFICATIONS = False

# CSRF 토큰에 사용할 비밀키 등록
SECRET_KEY = '1234'

