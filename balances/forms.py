from django import forms
from .models import Balance, Comment

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ('title', 'select1_content', 'select2_content', 'image_1', 'image_2',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        # self.fields['title'].widget.attrs['placeholder'] = '제목'
        self.fields['select1_content'].widget.attrs['class'] = 'form-control'
        # self.fields['select1_content'].widget.attrs['placeholder'] = '첫 번째 주제'

        self.fields['select2_content'].widget.attrs['class'] = 'form-control'
        # self.fields['select2_content'].widget.attrs['placeholder'] = '두 번째 주제'

        self.fields['image_1'].widget.attrs['class'] = 'form-control'
        self.fields['image_2'].widget.attrs['class'] = 'form-control'


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
        