from django import forms
from .models import Free
from all_info.models import Info
from django_summernote.fields import SummernoteTextField
from django_summernote.widgets import SummernoteWidget

class BoardWriteForm(forms.ModelForm):
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={
                'placeholder':'게시글 제목'
            }
        )
    )
    contents = SummernoteTextField


    #여기 아래에 select로 게시판 종류 추가하기
    options = (
        ('Free','자유게시판'),
        ('Free2','자유게시판2'),
        ('Free3','자유게시판3')

    )

    board_name = forms.ChoiceField(
        label='게시판 선택',
        widget=forms.Select(),
        choices=options
    )

    field_order  = [
        'title',
        'text',
        'info'
    ]

    class Meta:
        model = Free
        fields = [
            'title',
            'text',
            'info'
        ]
        widgets = {
            'contents' : SummernoteWidget()
        }
    def clean(self):
        cleaned_data = super().clean()

        title = cleaned_data.get('title','')
        text = cleaned_data.get('text','')
        info = cleaned_data.get('info','Free')

        if title == '':
            self.add_error('title','글 제목을 입력하세요.')
        elif text =='':
            self.add_error('text','글 내용을 입력하세요')
        else:
            self.title = title
            self.text = text
            self.info = info