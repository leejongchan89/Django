# kmdb를 위한 App Url
from django.urls import path

# kmdb라는 장고의 앱에서 views 모듈을 읽어 들입니다.
from . import views # 오류가 나더라도 무시 바람

urlpatterns = [
    path('main', views.main_page, name='main'), # 메인 페이지

    # 영화 목록을 표시해주는 url
    # path('요청할url패턴', '호출할View함수', name='url 패턴에 부여한 이름'),
    path('list', views.movie_list, name='movie_list'),

    path('pagination', views.movie_pagination, name='movie_pagination'),
    path('bootstrap_exercise/', views.bootstrap_exercise, name='bootstrap_exercise'),
    path('bootstrap', views.movie_bootstrap, name='movie_bootstrap'),
    path('field_search', views.movie_field_search, name='movie_field_search'),
]