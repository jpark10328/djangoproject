from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser,PermissionsMixin

# userid 를 장고가 사용하는 username 을 사용하지 않고 이메일로 변경
class UserManager(BaseUserManager):
    def _create_user(self, email, username, nickname, password, phone=None, rank=0, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        # username = self.model.normalize_username(username)
        user = self.model(email=email, nickname=nickname, username=username, rank=rank, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username='', nickname='', password=None, phone=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, username, nickname, password, phone, **extra_fields)

    def create_superuser(self, email, password, phone=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, "관리자", password, phone, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):

    RANK_CHOICES = [
        (0,'회원'),
        (1,'사업자'),
    ]

    email = models.EmailField(verbose_name="email",max_length=255,unique=True)
    username = models.CharField(max_length=50, verbose_name="이름")
    nickname = models.CharField(max_length=50, verbose_name="닉네임")
    rank = models.SmallIntegerField(choices = RANK_CHOICES, verbose_name="회원구분")
    phone = models.CharField(max_length=15, unique=True, null=True, verbose_name="전화번호")
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return "<%d %s>" % (self.pk, self.email)


    # def has_perm(self, perm, obj=None):
    #     return True


    # def has_module_perms(self, app_label):
    #     return True
    