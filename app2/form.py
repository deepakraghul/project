from django import forms

some_choices=[
('dosa','dosa'),
('idly','idly')
]
gender=[
('MALE','male'),
('FEMALE','female'),
('other','other')
]

class supermarket(forms.Form):
    name=forms.CharField(max_length=100)
    text=forms.CharField(initial="DEEPAK",widget=forms.Textarea(attrs={'row':4,'coln':10}))
    quantity=forms.IntegerField()
    price=forms.IntegerField()
    roll=forms.IntegerField()
    present=forms.BooleanField()
    email=forms.EmailField(required=False)
    food_menu=forms.CharField(widget=forms.Select(choices=some_choices))
    gender=forms.CharField(label="GENDER",widget=forms.Select(choices=gender))
    
