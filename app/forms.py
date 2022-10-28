from django import forms

from .models import Hotel


class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['hname', 'hfeature', 'hcontent', 'province', 'city', 'address_1', 'address_2', 'hphone', 'hmail']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['roomnum', 'roomcap', 'rcontent', 'roomprice']


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['visit_at', 'leave_at', 'room']


# CommentForm - fields : content
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']