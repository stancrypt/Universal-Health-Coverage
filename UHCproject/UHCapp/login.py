from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your Name")
    new_name= forms.CharField(label_suffix= 'Nnamdi')
    subject = forms.CharField(label="Your subject",max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
   
