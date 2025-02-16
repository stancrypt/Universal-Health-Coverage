from django import forms



class NameForm(forms.Form):
    user_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your subject'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Drop a message'}))
    sender = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    c_myself = forms.BooleanField(required=False)





class NameForm1(forms.Form):
    empanelled = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'placeholder': 'Enter Number Empanelled'}))
    access = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Access to Care'}))
    referred = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Total Referred'}))
    CHOICES = [('YES', 'YES'),('NO', 'NO')]
    selection = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect(), required=True)