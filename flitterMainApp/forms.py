from django import forms

class AuthenticationForm(forms.Form):
    usernameBox = forms.CharField(label="Username", max_length=90)
    passwordBox = forms.CharField(label="Password", max_length=85, widget=forms.PasswordInput)

class SearchForm(forms.Form):
    searchBox = forms.CharField(label="", max_length=90)

class StatusUpdateForm(forms.Form):
    statusUpdateBox = forms.CharField(label='', widget=forms.Textarea(attrs={'cols':155, 'rows':7}))

class SignUpForm(forms.Form):
    firstNameBox = forms.CharField(label="First Name", max_length=90, widget=forms.TextInput(attrs={'class':"form-control"}))
    lastNameBox = forms.CharField(label="Last Name", max_length=90, widget=forms.TextInput(attrs={'class':"form-control"}))
    usernameBox = forms.CharField(label="Username", max_length=90, widget=forms.TextInput(attrs={'class':"form-control"}))
    passwordBox = forms.CharField(label="Password", max_length=85, widget=forms.PasswordInput(attrs={'class':"form-control"}))
    confirmPasswordBox = forms.CharField(label="Confirm Password", max_length=85, widget=forms.PasswordInput(attrs={'class':"form-control"}))
