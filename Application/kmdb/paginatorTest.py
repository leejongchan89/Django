data = ['item' + str(idx).zfill(2) for idx in range(1,11)]
print('데이터 리스트 : ' + str(data))

from django.core.paginator import Paginator

pageSize = 3
paginator = Paginator(data, pageSize)
print(type(paginator))

per_page = paginator.per_page # pageSize 확인용
print('한페이지에 표시할 객체의 수 : ' + str(per_page))

currPage = 2
page = paginator.page(currPage) # <Page 2 of 4> 이렇게 출력 됨
print(str(currPage) + '페이지 정보 : ' + str(page))

object_list = page.object_list
print('현재 페이지 목록들 : ' + str(object_list))

total_pages = paginator.num_pages
print('전체 페이지 수 : ' + str(total_pages))

number = page.number # 현재 페이지 번호 확인용
print('현재 페이지 번호 : ' + str(number))

start_index = page.start_index() # 1 base 이다. 1부터 시작
print('현재 페이지의 첫 번째 인덱스 : ' + str(start_index))

end_index = page.end_index()
print('현재 페이지의 마지막 번째 인덱스 : ' + str(end_index))

has_next = page.has_next()
print('다음 페이지가 있나요? : ' + str(has_next))

if has_next:
    next_page = page.next_page_number()
    print('다음 페이지 번호 ' + str(next_page))

has_previous = page.has_previous()
print('이전 페이지가 있나요? : ' + str(has_previous))

if has_previous:
    previous_page = page.previous_page_number()
    print('이전 페이지 번호 ' + str(previous_page))

