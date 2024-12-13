from django import forms

CURSOS_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddCourseForm(forms.Form):
    quantity = forms.TypedChoiceField(
        choices=CURSOS_QUANTITY_CHOICES,
        coerce=int,
    )
    override = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput,
    )
