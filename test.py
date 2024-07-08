'''3D 애니메이션 예제'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


# X축 및 Y축 좌표 생성
xs = np.linspace(-2, 2, 101) # -2부터 2까지 균일간격 101개 값 생성
ys = np.linspace(-2, 2, 101) # -2부터 2까지 균일간격 101개 값 생성

# XY 평면 좌표 생성
xx, yy = np.meshgrid(xs, ys)

# 모든 XY 평면상 값에 해당하는 Z값 생성
zz = xx * np.exp(-(xx)**2 - yy**2)

# 3D 플롯 생성
fig, axs = plt.subplots(
    nrows=1,
    ncols=2,
    figsize=(10, 7),
    # layout 방식 설정 - 아래 두가지 방법 모두 가능
    # constrained_layout=True,
    # layout='tight',
    layout='tight',
    subplot_kw={'projection': '3d'} # 각 sub-plot에 전달할 args
)

# 참고사항
# constrained_layout
# tight_layout과 비슷하게 sub-plot을 자동 배치해주는 옵션입니다.
# 하지만, tight_layout 보다 유연한 배치를 제공합니다.
#   - sub-plot에 할당된 color bar 자동 배치
#   - 동일한 행/열에 배치된 sub-plot의 크기를 자동 조정
#   - 가로축, 세로축 자동 맞춤
# 참고: https://matplotlib.org/stable/users/explain/axes/constrainedlayout_guide.html

# constrained_layout vs tight_layout
# 이것 저것 신경쓰지 않고 matplotlib에게 맡기고 싶다면 constrained_layout 사용
# 미세한 조정을 직접 하고 싶다면 tight_layout 사용

### 첫번째(왼쪽) plot 생성 ###
# 3차원 채워진 등고선, contourf 메서드 -> 연결된 등고선 생성
axs[0].contourf(
    xx, yy, zz,
    cmap="inferno", # 컬러맵 지정,
    # cmap 참고: https://matplotlib.org/stable/users/explain/colors/colormaps.html#grayscale-conversion
    levels=20, # 등고선 라인 개수
)

### 두번째(오른쪽) plot 생성 ###
# 2차원 바닥 등고선 생성
axs[1].plot_surface(
    xx, yy, zz,
    cmap="inferno",
    ec="k",         # edge color, k: black
    # edge color format: https://matplotlib.org/stable/users/explain/colors/colors.html#color-formats
    linestyle="dotted",  # line 스타일(선 종류)
    # lie syyles format: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    linewidths=0.5  # line width(선 굵기)
)
# 3차원 색이 채워진 등고선 생성
axs[1].contourf(xx, yy, zz, zdir="z", offset=-0.6)
# 3차원 선으로만 연결된 등고선 생성
axs[1].contour(xx, yy, zz, zdir="z", offset=-0.6, linewidths=2, colors=["w"])
# Sub-plot 제목 지정
titles = ["(A): contourf()", "(B): plot_surface() + 2D contours"]
for ax, title in zip(axs, titles):
    # 시작할 때 바라보는 각도 지정
    ax.view_init(elev=20, azim=225) # 높이각: 20도, 좌우각: 225도
    ax.set_zlim(-0.6, 0.5) # Z축 범위 지정
    ax.set_title(title, pad=0)

# animation frame마다 적용되는 변화
def update(frame_number):
    axs[0].view_init(azim=225 + frame_number*2) # 좌우각 업데이트
    axs[1].view_init(azim=225 + frame_number*2) # 좌우각 업데이트

# animation 객체 생성
anim = FuncAnimation(
    fig,
    update,
    frames=720, # 초당 프레임(이미지) 개수
    interval=5, # 프레임과 프레임 시간 간격(밀리초), 기본값: 200ms
)

# animation을 mp4 동영상으로 저장
anim.save("animation_result.mp4", fps=24)