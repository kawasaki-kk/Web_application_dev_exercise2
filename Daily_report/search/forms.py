from django import forms

class ReportSearchForm(forms.Form):
   keyword = forms.CharField(min_length=2, max_length=100, label='keyword')
   # date = forms.DateField(required=False)