from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import QuoteHead, QuoteDetail


class QuoteHeadCreateForm(forms.ModelForm):
    class Meta:
        model = QuoteHead
        #fields = ["category", "zmms", "manage_memo" ]
        exclude = ('create_at','modify' , 'invalid',)
        widgets = {
            'customer': forms.TextInput(attrs={'size':20, 'title':'Customer Number', }) ,

        }

class QuoteLineCreateForm(forms.ModelForm):
    class Meta:
        model = QuoteDetail
        fields = ["quotehead", "line_no", "product","unit_price","line_memo"   ]
        #exclude = ('create_at','modify' )
