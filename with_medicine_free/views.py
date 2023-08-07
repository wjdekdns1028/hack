from django.shortcuts import render, redirect, get_object_or_404
from .forms import Free_board_Form, Free_board_CommentForm
from django.utils import timezone
from .models import Free_board, Free_Comment
from django.views.generic import ListView
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def free_read(request):
    free_board = Free_board.objects.all()
    return render(request, 'free_read.html', {'free_board':free_board})

def free_create(request):
    if request.method == 'POST':
        form = Free_board_Form(request.POST)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('free_read')
    else:
        form = Free_board_Form
        return render(request, 'free_create.html', {'form': form})
    
def free_detail(request, id):  
    free_board = get_object_or_404(Free_board, id = id)  
    if request.method == 'POST':
        form = Free_board_CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.free_board_id = free_board
            comment.save()
            return redirect('free_detail', id)
    else:
        form = Free_board_CommentForm
        return render(request, 'free_detail.html', {'form' : form, 'free_board' : free_board})  

def free_update(request, id):
    free_board = get_object_or_404(Free_board, id = id)
    if request.method == 'POST':
        form = Free_board_Form(request.POST, instance=free_board)
        if form.is_valid():
            form = form.save(commit = False)
            form.pub_date = timezone.now()
            form.save()
            return redirect('free_read')
    else:
        form = Free_board_Form(instance=free_board)
        return render(request, 'free_update.html', {'form' : form})
    
def free_delete(request, id):
    free_update = get_object_or_404(Free_board, id = id)
    free_update.delete()
    return redirect('free_read')

def free_comment_delete(request, id, c_id):
    comment = get_object_or_404(Free_Comment, id=c_id)
    comment.delete()
    return redirect('free_detail',id)

def free_comment_update(request, id, com_id):
    comment = Free_Comment.objects.get(id = com_id)
    form = Free_board_CommentForm(instance=comment)
    if request.method == "POST":
        form = Free_board_CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('free_detail', id)
    return render(request, 'free_comment_update.html', {'form':form})


def free_search(request):
    free_board = Free_board.objects.all().order_by('-id')
    
    q = request.POST.get('q', "")
    
    if q:
        free_board = free_board.filter(Q (title__icontains=q) | Q (body__icontains=q))
        return render(request, 'free_search.html', {'free_board':free_board, 'q':q})
    
    else:
        return render(request, 'free_search.html', {'free_board':free_board})




# class NoticeListView(ListView): # ListView를 상속받은 뷰 클래스
#     model = Free_board
#     paginate_by = 10 # 한 페이지에 보여줄 객체의 개수를 10으로 설정
#     template_name = 'free_read.html' # 뷰에서 사용할 템플릿 파일의 이름 설정
#     context_object_name = 'free_board' # 템플릿에서 사용할 객체 리스트의 이름 설정
    

    
#     def get_body_data(self, **kwargs): # 기본 컨텍스트 데이터를 가져옴
#         body = super().get_body_data(**kwargs) # super를 사용해 부모 클래스의 get_body_data메소드를 호출하여 기본 컨텍스트 데이터를 가져옴
#         paginator = body['paginator'] # 페이지네이션의 객체를 가져와 변수 저장
#         page_numbers_range = 5 # 한번에 보여줄 페이지 버튼의 개수를 5로 설정
#         max_index = len(paginator.page_range) # 페이지 범위의 최대 인덱스 저장
            
#         page = self.request.GET.get('page') # get파라미터에서 page라는 키로 현재 페이지 번호를 가져옴
#         current_page = int(page) if page else 1 # 현재 페이지 번호를 get파라미터로 전달하면 해당 페이지 번호를 가져오고 전달되지 않으면 1로 설정
            
#         start_index = int((current_page - 1) / page_numbers_range) * page_numbers_range # 현재 페이지를 기준으로 보여줄 페이지 범위 계산
#         end_index = start_index + page_numbers_range # 페이지 범위의 끝 인덱스를 계산
#         if end_index >= max_index: # 끝 인덱스가 최대 인덱스를 초과하지 않도록
#             end_index = max_index
                
#         page_range = paginator.page_range[start_index:end_index] # 계산된 페이지 범위 저장
#         body["page_range"] = page_range # body page_range정보를 추가해 템플릿에서 사용하도록 
            
#         search_keyword = self.request.GET.get('q', '') # get파라미터에서 q라는 키로 검색 키워드를 가져옴, 검색어가 없으면 빈 문자열로 설정
#         search_type = self.request.GET.get('type', '') # get파라미터에서 type이라는 키로 검색 유형을 가져옴, 검색유형이 없으면 빈 문자열로 설정

#         if len(search_keyword) > 1 : # 검색어의 길이가 2보다 큰 경우라면
#             body['q'] = search_keyword # 검색어 컨텍스트에 추가
#         body['type'] = search_type # 검색 유형 컨텍스트에 추가

#         return body
