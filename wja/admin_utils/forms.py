from django import forms


class UploadTreatmentsForm(forms.Form):
    file = forms.FileField()
