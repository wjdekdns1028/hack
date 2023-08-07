from django.shortcuts import render
from .models import Item
from .forms import SearchForm

# Create your views here.

def main(request):
    return render(request, 'main.html')

# def search_items(request):
#     if request.method == 'GET': # http요청의 메서드가 get이라면
#         form = SearchForm(request.GET) # get요청에서 전달된 데이터를 사용해 searchform 생성
#         if form.is_valid(): # 폼의 데이터가 유효하다면
#             search_query = form.cleaned_data['search_query'] # 폼에 입력된 검색어를 cleaned_data속성을 통해 가져옴
#             items = Item.objects.filter(title__icontains=search_query) # 검색어를 이용해 item모델의 title필드를 대소문자 구분하지 않고 검색
#             return render(request, 'search_results.html', {'items':items, 'query':search_query}) # 검색결과를 화면에 보여주고 검색결과인 items와 검색어 quesry를 전달
#         else:
#             form = SearchForm() # get요청 아니면 빈폼 생성
#         return render(request, 'main.html', {'form':form}) # 빈 폼을 렌더링하여 보여줌