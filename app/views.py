from django.shortcuts import redirect, render,get_object_or_404
from django.conf import settings

from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages

from django.http import JsonResponse

from .forms import CommentForm
from .models import Hotel, Room, Comment, Order, Checkbox

from django.db.models import Q,Count
from django.core.paginator import Paginator

from django.utils import timezone



def home(request):
    return render(request, "home.html")

def hotel_list(request):
    """
    호텔 리스트 목록
    """
    hotels = Hotel.objects.order_by("id")


    return render(request, "app/hotel_list.html", {"hotels":hotels})

def hotel_detail(request,pk):

    hotel = get_object_or_404(Hotel, pk=pk)
    rooms = Room.objects.filter(hotel=hotel)
    checkboxes = Checkbox.objects.filter(hotel=hotel)

    return render(request, "app/hotel_detail.html",{"hotel":hotel,"rooms":rooms,"checkboxes":checkboxes})

def order_delete(request, pk):
    
    order = Order.objects.get(id=pk)

    order.delete()

    return redirect("order_result")


@login_required(login_url="login")
def order(request, pk):

    room = Room.objects.get(id=pk)
    # room 예약 가능일자 확인

    checkin=timezone.localdate()
    checkout=timezone.localdate() + timezone.timedelta(days=30)
    # print(checkout)
    if checkin:
        orders = Order.objects.filter(room=room).filter(
                Q(visit_at__gte = checkin) &
                Q(leave_at__lte = checkout)
            )

        result_date=[
            {
                
            "visit_at": order.visit_at.strftime("%Y-%m-%d"),
            "leave_at":order.leave_at.strftime("%Y-%m-%d")           
            }for order in orders
        ]
        print("result_date",result_date)       
     

    # result = []           
    # for order in orders:
    #     print(order)
    #     check_date = []
    #     for date in order:                     
    #         check_date.append(date.strftime("%Y-%m-%d"))
    #         # check_date.append(date)
    #     result.append(check_date)
                
    # print(result)

    if request.method == "POST":

        visit_at = request.POST.get('checkin')
        leave_at = request.POST.get('checkout')
        room = room
        customer = request.user

        order = Order.objects.create(visit_at=visit_at,leave_at=leave_at,room=room,customer=customer)        
        
        return redirect("order_result")
    

    return render(request, "app/order.html",{"room":room,"orders":orders,"result_date":result_date})

@login_required(login_url="login")
def order_result(request):

    orders = Order.objects.filter(customer=request.user)

    # if request.method == "POST":
    #     form = OrderForm(request.POST, request.FILES)
        

    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         order.user = request.user
    #         order.save()

    #         return redirect("order")
    # else:
    #     form = OrderForm()


    return render(request, "app/order_result.html",{"orders":orders})

@require_POST
@login_required(redirect_field_name="next")
def comment_create(request):
    """
    댓글 등록
    """
    print('comment')
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


def hotel_search(request):
    """
    Hotel 목록 추출
    """

    # 사용자가 입력한 검색어 가져오기
    keyword = request.GET.get('keyword','')

    # 사용자가 입력한 입실/퇴실 날짜 가져오기
    checkin = request.GET.get('checkin',timezone.localdate())
    checkout = request.GET.get('checkout',timezone.localdate())
    roomcap = request.GET.get('roomcap','1')
    # print(checkin)
    # print(checkout)
    # print("&*&*&*")

    # 사용자가 요청한 페이지 값 가져오기
    page = request.GET.get("page", 1)

    # 사용자가 입력한 정렬기준 가져오기
    so = request.GET.get('so','recent')

    # print("-------------")
    # print(keyword,page, so)

    if so == "recommend":
        hotel_lists = Hotel.objects.annotate(num_voter = Count('voter')).order_by('-num_voter')
    elif so == "popular":
        hotel_lists = Hotel.objects.annotate(num_comment = Count('comment')).order_by('-num_comment')
    else:
        # 전체 목록 추출 - 최신순
        hotel_lists = Hotel.objects.order_by("-id")


    # hotel_lists 에서 id만 추출 => 리스트로 생성

    
        # print(room.roomtype)

    # filter(user__id__in = lookup_user_ids)

    # 검색결과 리스트 추출
    # subject, content, author 항목들이 검색어와 일치하는 경우를 추출
    # Q : or 조건으로 데이터 조회
    # icontains : 대소문자 구별 없이
    if keyword:
        hotel_lists = hotel_lists.filter(
            Q(hname__icontains = keyword) |
            Q(city__icontains = keyword) |
            Q(address_1__icontains = keyword) 
        ).distinct()

    # if searchdate:
    #     hotel_lists = hotel_lists.filter(
    #         Q(start)
    #     )


    # print("hotel_ids")
    # room 에서 hotel_lists id와 일치하는 room_id 추출
    hotel_ids=hotel_lists.values_list('id',flat=True)
    # print(hotel_ids)
    # roomcap 이 맞는 room_id 추출
    room_ids = Room.objects.filter(hotel__id__in=list(hotel_ids)).filter(roomcap__gte = roomcap).values_list('id',flat=True)
    # print("room_ids")
    # print(room_ids)

    # order 에서 room_id 가 일치하고 예약된 날짜가 없는 값을 추출

    if checkin:
        order_ids = Order.objects.filter(room__id__in=list(room_ids)).values_list('room',flat=True).filter(
            Q(visit_at__gte = checkin) &
            Q(leave_at__lte = checkout)
        )   
    # else:
    #     checkin = timezone.now()
    #     checkout = timezone.now()
    #     order_ids = Order.objects.filter(room__id__in=list(room_ids)).values_list('room',flat=True).filter(
    #         Q(visit_at__gte = checkin) &
    #         Q(leave_at__lte = checkout)
    #     )  

    # print("order_ids")
    # print(order_ids)

    rooms = Room.objects.filter(hotel__id__in=list(hotel_ids)).filter(roomcap__gte = roomcap).exclude(id__in=list(order_ids))

    # for room in rooms:
        # print(room)

    # for room in rooms:
    #     room_list =[
    #         {
    #             "room_id":room.id,
    #             "hotel_name":room.hotel.hname,
    #             "hotel_province":room.hotel.province,
    #             "hotel_city":room.hotel.city,
    #             "hotel_address_1":room.hotel.address_1,
    #             "hotel_address_2":room.hotel.address_2,
    #             "hotel_hinfo":room.hotel.hinfo       
    #         }
    #     ]
    #     print(room_list)  


    # 전체 목록 안에서 사용자가 요청한 페이지에 대한 목록만 전송
    paginator = Paginator(rooms, 5)
    rooms = paginator.get_page(page)

    return render(request, "app/hotel_search.html",{"rooms":rooms,'page':page,'keyword':keyword,'so':so,'checkin':checkin,'checkout':checkout,'roomcap':roomcap})
