from django import forms

class CourseForm(forms.Form):
    CREDITS_CHOICES = [
        (1, '1'), (1, '1.5'), (2, '2'), 
        (3, '3'), (4, '4'), (5, '5'), (14, '14')
    ]
    GRADE_CHOICES = [
        (10, 'S'), (9, 'A'), (8, 'B'),
        (7, 'C'), (6, 'D'), (5, 'E'), (0, 'F')
    ]

    credits = forms.ChoiceField(choices=CREDITS_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    grade = forms.ChoiceField(choices=GRADE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))