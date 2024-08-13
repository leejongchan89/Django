from django.db import models

# Create your models here.
# 모델은 장고의 테이블을 정의해주는 클래스입니다.
# 자바 bean 클래스 만드는 느낌
class Movie(models.Model): # Movie가 Model을 상속 받는다.
    MovieCd = models.IntegerField(primary_key=True)
    MovieNm = models.TextField()
    MovieNmEn = models.TextField()
    prdtYear = models.TextField()
    openDt = models.FloatField()
    typeNm = models.FloatField()
    prdtStatNm = models.TextField()
    nationAlt = models.TextField()
    genreAlt = models.TextField()
    repNationNm = models.TextField()
    repGenreNm = models.TextField()

    # 메타 클래스 : 기본 컬럼 이외에 모델의 설정 정보를 담고 있는 내부 클래스
    # 예를 들어 테이블 이름이나, 정렬 방식 등을 설정할 수 있습니다.
    # Meta 클래스는 이너 클래스이고 Model을 상속 받은 클래스에는 항상 있다?
    class Meta:
        db_table = 'movies' # 이 모델은 'movies' 테이블과 연동됩니다.

    # __str__ 함수는 객체를 문자열로 표현하고자 할때 사용하는 함수입니다. (java에서 toString 같은 역할)
    # 메소드
    def __str__(self):
        return self.movieNm

# end class Movie(models.Model)

