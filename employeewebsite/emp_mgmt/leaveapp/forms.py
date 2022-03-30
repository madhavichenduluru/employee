from django import forms
from leaveapp.models import Leave


class MyLeaveUploadForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = '__all__'

    def clean(self):
        data = self.cleaned_data

        begindt = data['start_date']
        enddt = data['end_date']
        count = (enddt - begindt).days
        print(type(count))
        print(count)
        if count>4:
            print('hello')
            raise forms.ValidationError('maximum 4 leaves can apply')
        return self.cleaned_data
