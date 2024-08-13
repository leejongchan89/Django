# render 함수는 클라이언트의 요청을 처리하여 최종 결과인 HTML 문서를 클라이언트에게 되돌려 주는 역할을 합니다.
from django.shortcuts import render
from .models import Movie # models.py에서 만든 클래스 / 상대 경로 임포트
# from kmdb.models import Movie # 절대 경로 임포트

# Create your views here.
# 데이터베이스에서 정보를 가져와서 HTML 템플릿에 전달하는 movie_list라는 뷰 함수를 정의하고 있습니다.
def movie_list(request): # HTTP 요청을 처리하는 뷰 함수
    # QuerySet는 데이터 베이스 쿼리의 결과 집합을 의미하는 객체입니다.
    # 장고에서 QuerySet의 기본 이름은 objects입니다.
    movies = Movie.objects.all() # Movie 테이블에 모든 데이터를 가져 오시오

    # 'kmdb/movie_list.html'는 렌더링할 템플릿의 경로
    # 딕셔너리를 사용하여 템플릿에 movieList라는 이름으로 movies 데이터를 전달
    return render(request, 'kmdb/movie_list.html', {'movieList':movies})
# end def movie_List(request):


# 페이징 처리를 위하여 임포트 합니다.
from django.core.paginator import Paginator

def movie_pagination(request): # request는 http 요청 객체입니다.
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)

    # GET 방식으로 요청한 파라미터 page를 page_number 변수에 저장합니다.
    page_number = request.GET.get('page') # html 작성할 때 파라미터로 page 사용 / html 문서내에서 클릭시 호출됨
    movieList = paginator.get_page(page_number)

    return render(request, 'kmdb/movie_pagination.html', {'movieList':movieList})
# end def movie_pagination(request)

def bootstrap_exercise(request):
    return render(request, 'kmdb/bootstrap_exercise.html')
# end def

