# render 함수는 클라이언트의 요청을 처리하여 최종 결과인 HTML 문서를 클라이언트에게 되돌려 주는 역할을 합니다.
from django.shortcuts import render
from .models import Movie # models.py에서 만든 클래스 / 상대 경로 임포트
# from kmdb.models import Movie # 절대 경로 임포트

# Create your views here.
def main_page(request): # 메인 페이지 호출하기
    return render(request, 'kmdb/main.html')
# end def

# 데이터베이스에서 정보를 가져와서 HTML 템플릿에 전달하는 movie_list라는 뷰 함수를 정의하고 있습니다.
def movie_list(request): # HTTP 요청을 처리하는 뷰 함수
    # QuerySet는 데이터 베이스 쿼리의 결과 집합을 의미하는 객체입니다.
    # https://docs.djangoproject.com/en/5.1/ref/models/querysets/ 쿼리셋 정보
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
    pageSize = 10
    paginator = Paginator(movies, pageSize)

    # GET 방식으로 요청한 파라미터 page를 pageNumber 변수에 저장합니다.
    pageNumber = request.GET.get('page') # html 작성할 때 파라미터로 page 사용 / html 문서내에서 클릭시 호출됨
    movieList = paginator.get_page(pageNumber)

    return render(request, 'kmdb/movie_pagination.html', {'movieList':movieList})
# end def movie_pagination(request)

def bootstrap_exercise(request):
    return render(request, 'kmdb/bootstrap_exercise.html')
# end def

def movie_bootstrap(request):
    movies = Movie.objects.all()
    pageSize = 10
    paginator = Paginator(movies, pageSize)

    pageNumber = request.GET.get('page') # 사용자가 요청한 페이지 번호 (파라미터는 무조건 문자로 넘어온다.)
    movieList = paginator.get_page(pageNumber)
    totalPage = paginator.num_pages
    pageCount = 10

    if pageNumber == None: # 처음 시작 되었을 때
        pageNumber = 1
        beginPage = 1
        endPage = 10

    else: # 사용자가 Pagination의 숫자를 눌럿을 때
        print('pageNumber=' + pageNumber) # 파라미터들은 문자열로 넘어 옵니다.
        pageNumber = int(pageNumber) # 해당 파라미터를 정수형 숫자로 변경합니다.
        beginPage = (pageNumber-1) // pageSize * pageSize + 1

        endPage = beginPage + pageCount - 1

        # 끝 페이지가 전체 페이지 번호 보다 큰 경우, 끝페이지를 전체 페이지로 대체합니다.
        if endPage > totalPage:
            endPage = totalPage

    # end if

    has_previous = pageNumber > pageCount
    print('has_previous=' + str(has_previous))

    # 주의) 몫 연산을 위하여 //로 나누어야 합니다.
    has_next = pageNumber < (totalPage // pageCount * pageCount + 1)
    print('has_next=' + str(has_next))


    print('beginPage=' + str(beginPage))
    print('endPage=' + str(endPage))

    # Template(html 문서) 파일에서는 range()를 사용할 수 없습니다.
    # 연산이 이루어 지는 과정에서 실수로 바뀌기 때문에 다시 정수로 변환해줍니다.
    page_range = range(int(beginPage), int(endPage) + 1)  # 10개 씩을 의미

    context = {'movieList':movieList, 'beginPage':beginPage, 'endPage':endPage, 'page_range':page_range, 'has_previous':has_previous, 'has_next':has_next}

    return render(request, 'kmdb/movie_bootstrap.html', context)
# end def

def movie_field_search(request):
    movies = Movie.objects.all() # 전체 영화 목록

    # 요청한 mode, keyword 파라미터를 챙깁니다.
    mode = request.GET.get('mode')
    keyword = request.GET.get('keyword')
    print('mode=[%s], keyword=[%s]' % (mode, keyword)) # 디버깅 []는 빈칸 방지

    if mode and keyword:  # mode, keyword 둘다 의미 있는 데이터가 들어오면
        if mode == 'MovieNm':  # 영화명(국문)
            movies = movies.filter(MovieNm__icontains=keyword)  # 영화 이름안에 키워드를 포함하고 있는 필터 * icontains = 대소문자 무시, 다 포함
        elif mode == 'typeNm':  # 영화 유형
            movies = movies.filter(typeNm__icontains=keyword)
        elif mode == 'repGenreNm':  # 대표 장르
            movies = movies.filter(repGenreNm__icontains=keyword)
        # end if

    pageSize = 10
    paginator = Paginator(movies, pageSize)

    pageNumber = request.GET.get('page')  # 사용자가 요청한 페이지 번호 (파라미터는 무조건 문자로 넘어온다.)
    movieList = paginator.get_page(pageNumber)
    pageCount = 10
    totalPage = paginator.num_pages

    if pageNumber == None:  # 처음 시작 되었을 때
        pageNumber = 1
        beginPage = 1
        endPage = 10

    else:  # 사용자가 Pagination의 숫자를 눌럿을 때
        print('pageNumber=' + pageNumber)  # 파라미터들은 문자열로 넘어 옵니다.
        pageNumber = int(pageNumber)  # 해당 파라미터를 정수형 숫자로 변경합니다.
        beginPage = (pageNumber - 1) // pageSize * pageSize + 1

        endPage = beginPage + pageCount - 1

        # 끝 페이지가 전체 페이지 번호 보다 큰 경우, 끝페이지를 전체 페이지로 대체합니다.

        if endPage > totalPage:
            endPage = totalPage

    # end if

    has_previous = pageNumber > pageCount
    print('has_previous=' + str(has_previous))

    # 주의) 몫 연산을 위하여 //로 나누어야 합니다.
    has_next = pageNumber < (totalPage // pageCount * pageCount + 1)
    print('has_next=' + str(has_next))

    print('beginPage=' + str(beginPage))
    print('endPage=' + str(endPage))

    # Template(html 문서) 파일에서는 range()를 사용할 수 없습니다.
    # 연산이 이루어 지는 과정에서 실수로 바뀌기 때문에 다시 정수로 변환해줍니다.
    page_range = range(int(beginPage), int(endPage) + 1)  # 10개 씩을 의미

    # 페이지로 넘어 오는 파라미터 정보
    query_params = request.GET.copy() # 파라미터 목록의 복사본 만들기

    # page 파라미터를 제거한 다음 쿼리 문자열을 전송하도록 합니다.
    delete_param = 'page'
    if delete_param in query_params:
        del query_params[delete_param]
    # end if

    # 넘겨진 쿼리 목록의 문자열 집할을 QueryString이라고 부릅니다.
    query_params = query_params.urlencode() # 복사본을 인코딩 문자열로 변환
    print('query_params =[' + str(query_params) + ']')

    context = {'movieList': movieList, 'beginPage': beginPage, 'endPage': endPage, 'page_range': page_range,
               'has_previous': has_previous, 'has_next': has_next, 'query_params': query_params}

    return render(request, 'kmdb/movie_field_search.html', context)

# end def
