from django import forms
from django.forms import ModelForm, Textarea, CharField
from .models import QuoteHead


class QuoteHeadCreateForm(forms.ModelForm):
    class Meta:
        model = QuoteHead
        #fields = ["category", "zmms", "manage_memo" ]
        exclude = ('create_at','modify' , 'invalid',)
        widgets = {
            'customer': forms.TextInput(attrs={'size':20, 'title':'Customer Number', }) ,

        }

class QuoteHeadDetailForm(forms.ModelForm):
    class Meta:
        model = QuoteHead
        #fields = ["category", "zmms", "manage_memo" ]
        exclude = ('create_at','modify' )
        widgets = {
            'customer': forms.TextInput(attrs={'size':20, 'title':'Customer Number', }) ,
            #'product': forms.TextInput(attrs={'size':20, 'title':'Product Number', }) ,

        }
