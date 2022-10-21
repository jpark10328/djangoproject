# Generated by Django 4.1.1 on 2022-10-21 08:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hotel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("hname", models.CharField(max_length=200, verbose_name="숙소명")),
                ("hfeature", models.TextField(verbose_name="숙소 특징")),
                ("hcontent", models.TextField(verbose_name="상세 안내")),
                ("province", models.CharField(max_length=50, verbose_name="도")),
                ("city", models.CharField(max_length=50, verbose_name="시")),
                ("address_1", models.TextField(verbose_name="도로명주소")),
                ("address_2", models.TextField(verbose_name="상세주소")),
                (
                    "owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="사업자",
                    ),
                ),
                (
                    "voter",
                    models.ManyToManyField(
                        related_name="voter_hotel", to=settings.AUTH_USER_MODEL
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("roomnum", models.IntegerField(verbose_name="방번호")),
                ("roomcap", models.SmallIntegerField(verbose_name="정원")),
                ("rcontent", models.TextField(verbose_name="방 정보")),
                ("roomprice", models.IntegerField(verbose_name="가격")),
                ("hphone", models.CharField(max_length=50, verbose_name="전화번호")),
                ("hmail", models.EmailField(max_length=254, verbose_name="문의 이메일")),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.hotel",
                        verbose_name="숙소",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "ordered_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="결제날짜"),
                ),
                ("visit_at", models.DateTimeField(verbose_name="입실날짜")),
                ("leave_at", models.DateTimeField(verbose_name="퇴실날짜")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="예약자",
                    ),
                ),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.room",
                        verbose_name="주문객실",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="댓글 내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성날짜"),
                ),
                (
                    "modified_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정날짜"),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
                (
                    "hotel",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.hotel",
                        verbose_name="숙소",
                    ),
                ),
            ],
        ),
    ]
