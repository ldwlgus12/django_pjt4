from django import forms
from .models import Balance, Comment

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ('title', 'select1_content', 'select2_content', 'image_1', 'image_2',)



class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label='',
        widget = forms.TextInput(
            attrs={
                'class' : 'form-control input-group',
                'placeholder' : '댓글을 입력해주세요'
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)
        