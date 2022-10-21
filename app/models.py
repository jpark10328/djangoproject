from django.db import models

class BaseModel(models.Model):
    """
    추상클래스
    """
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True # 추상 클래스로 만드는 코드

class Hotel(models.Model):
    hotel = models.CharField(max_length=200, verbose_name="숙박이름")
    content = models.TextField(verbose_name="숙박내용 및 주소")
    
    def __str__(self) -> str:
        return self.subject
