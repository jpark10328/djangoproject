from django.shortcuts import redirect, render,get_object_or_404
from django.conf import settings

# from django.views.generic.base import TemplateView
# from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from django.http import JsonResponse

from .forms import CommentForm
from .models import Hotel, Room, Comment, Checkbox, Order


def home(request):
    return render(request, "home.html")

def hotel_list(request):
    """
    호텔 리스트 목록
    """
    hotels = Hotel.objects.order_by("id")


    return render(request, "hotel_list.html", {"hotels":hotels})

def hotel_detail(request,pk):

    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel=hotel)
    checkboxes = Checkbox.objects.filter(hotel=hotel)

    return render(request, "hotel_detail.html",{"hotel":hotel,"rooms":rooms,"checkboxes":checkboxes})

@login_required(login_url="login")
def order(request, pk):

    order = Order.objects.get(id=pk)

    return render(request, "order.html",{"order":order})

@login_required(login_url="login")
def hotel_order(request):

    order = Order.objects.filter(customer=request.user)

    # if request.method == "POST":
    #     form = OrderForm(request.POST, request.FILES)
        

    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.user = request.user
    #         order.save()

    #         return redirect("order")
    # else:
    #     form = OrderForm()

    return render(request, "order.html",{"order":order})

@require_POST
@login_required(redirect_field_name="next")
def comment_create(request):
    """
    댓글 등록
    """
    errors = []
    if request.method == "POST":
        # 폼에서 넘어오는 값 2개 가져오기
        hotel_id = request.POST.get("hotel_id")
        content = request.POST.get("content").strip()

        if content:
            # 댓글 생성
            # comment = Comment(user=request.user,post=post_id,content=content)
            # comment.save()

            Comment.objects.create(author=request.user,hotel_id=hotel_id,content=content)
            return redirect("hotel_detail", pk=hotel_id)
        else:
            # 화면 쪽에 에러 메세지 전송
            messages.error(request,"댓글을 입력해 주세요")
            return redirect("hotel_detail", pk=hotel_id)

@login_required(login_url='users:login')
def comment_delete(request,comment_id):
    
    comment = get_object_or_404(Comment,pk=comment_id)
    hotel_id = comment.hotel.id

    comment.delete()
    return redirect("hotel_detail", pk=hotel_id)

@login_required(login_url='users:login')
def comment_modify(request,comment_id):
    """
    질문 댓글 수정 => 템플릿은 comment_create 사용
    """
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.save()
            return JsonResponse({"message":"success"},status=200)       
    else:
        result = {
            "id": comment.id,
            "content":comment.content
        }


        return JsonResponse(result,status=200)

        # return render(request, "hotel_detail.html",{"form":form})
