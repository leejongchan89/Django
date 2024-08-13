"""
URL configuration for DjangoApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

# URL 경로를 정의하고, 각 URL 경로에 대한 뷰(view)를 설정하는 urlpatterns 목록을 설정
# kmdb라는 장고의 앱에서 views 모듈을 읽어 들입니다.
from kmdb import views # 오류가 나더라도 무시 바람

urlpatterns = [
    path('admin/', admin.site.urls),

    # 영화 목록을 표시해주는 url
    # path('요청할url패턴', '호출할View함수', name='url 패턴에 부여한 이름'),
    path('movies/', views.movie_list, name='movie_list'),

    path('movies/pagination', views.movie_pagination, name='movie_pagination'),
    path('bootstrap_exercise/', views.bootstrap_exercise, name='bootstrap_exercise'),

]
