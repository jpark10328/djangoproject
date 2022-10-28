# Generated by Django 4.1.2 on 2022-10-28 08:07

import app.models
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
                ("province", models.CharField(max_length=50, verbose_name="도")),
                ("city", models.CharField(max_length=50, verbose_name="시")),
                ("address_1", models.TextField(verbose_name="도로명주소")),
                ("address_2", models.TextField(verbose_name="상세주소")),
                (
                    "himage",
                    models.ImageField(
                        blank=True, null=True, upload_to=app.models.image_upload_to
                    ),
                ),
                ("hphone", models.CharField(max_length=50, verbose_name="전화번호")),
                (
                    "hmail",
                    models.EmailField(max_length=254, null=True, verbose_name="문의 이메일"),
                ),
                ("hinfo", models.TextField(null=True, verbose_name="숙소 안내")),
                ("hmap", models.TextField(null=True, verbose_name="숙소 지도")),
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
                (
                    "rimage",
                    models.ImageField(
                        blank=True, null=True, upload_to=app.models.image_upload_to
                    ),
                ),
                (
                    "roomtype",
                    models.CharField(max_length=200, null=True, verbose_name="방종류"),
                ),
                ("roomcap", models.SmallIntegerField(verbose_name="정원")),
                ("rcontent", models.TextField(verbose_name="방 정보")),
                ("roomprice", models.IntegerField(verbose_name="가격")),
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
                ("visit_at", models.DateField(verbose_name="입실날짜")),
                ("leave_at", models.DateField(verbose_name="퇴실날짜")),
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
            name="Image",
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
                ("image", models.ImageField(upload_to=app.models.image_upload_to)),
                ("order", models.SmallIntegerField()),
                (
                    "hotel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.hotel"
                    ),
                ),
            ],
            options={"ordering": ["order"],},
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
                ("score", models.SmallIntegerField(null=True, verbose_name="리뷰 점수")),
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
        migrations.CreateModel(
            name="Checkbox",
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
                ("family", models.BooleanField(default=False, verbose_name="가족객실")),
                ("wifi", models.BooleanField(default=False, verbose_name="전구역 WIFI")),
                ("parking", models.BooleanField(default=False, verbose_name="무료주차")),
                ("fitness", models.BooleanField(default=False, verbose_name="피트니스 센터")),
                ("nosmoking", models.BooleanField(default=False, verbose_name="금연 객실")),
                ("breakfast", models.BooleanField(default=False, verbose_name="조식")),
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
        migrations.AddConstraint(
            model_name="image",
            constraint=models.UniqueConstraint(
                fields=("hotel", "order"), name="unique_together"
            ),
        ),
    ]
