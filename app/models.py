from django.db import models
from user.models import User

# 호텔(Hotel) 모델
# 제목(hname-200), 설명(hcontent), 도(province), 시(city), 도로명주소(address_1), 상세주소(address_2)
class Hotel(models.Model):
    owner = models.ForeignKey(User,verbose_name="사업자", on_delete=models.CASCADE)
    hname = models.CharField(max_length=200,verbose_name="숙소명")
    hfeature = models.TextField(verbose_name="숙소 특징")
    hcontent = models.TextField(verbose_name="상세 안내")
    province = models.CharField(max_length=50,verbose_name="도")
    city = models.CharField(max_length=50,verbose_name="시")
    address_1 = models.TextField(verbose_name="도로명주소")
    address_2 = models.TextField(verbose_name="상세주소")
    himage = models.ImageField(blank=True, null=True)
    hphone = models.CharField(verbose_name ="전화번호",max_length=50)
    hmail = models.EmailField(verbose_name ="문의 이메일", null=True)
    hinfo = models.TextField(verbose_name="숙소 안내", null=True)
    hmap = models.TextField(verbose_name="숙소 지도", null=True)
    # 추천
    voter = models.ManyToManyField(User, related_name='voter_hotel')

    def __str__(self) -> str:
        return self.hname

class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE,verbose_name="숙소")
    roomnum = models.IntegerField(verbose_name="방번호")
    roomcap = models.SmallIntegerField(verbose_name="정원")
    rcontent = models.TextField(verbose_name="방 정보")
    roomprice = models.IntegerField(verbose_name="가격")

    def __str__(self) -> str:
        return self.hotel + self.roomnum


class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="작성자")
    content = models.TextField(verbose_name="댓글 내용")
    score = models.SmallIntegerField(verbose_name="리뷰 점수", null=True)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="작성날짜")  
    modified_at = models.DateTimeField(auto_now=True,verbose_name="수정날짜")
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE,null=True, blank=True, verbose_name="숙소")

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="예약자")
    ordered_at = models.DateTimeField(auto_now_add=True,verbose_name="결제날짜")
    visit_at = models.DateTimeField(verbose_name="입실날짜")
    leave_at = models.DateTimeField(verbose_name="퇴실날짜")
    room = models.ForeignKey(Room, on_delete=models.CASCADE,verbose_name="주문객실")


    def __str__(self) -> str:
        return self.customer + self.cumstomer.pk


    

class BaseModel(models.Model):
    """
    추상클래스
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 추상 클래스로 만드는 코드
