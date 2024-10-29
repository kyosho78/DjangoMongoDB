# members/forms.py
from django import forms
from .models import Member
import datetime

class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'address', 'postal_code', 'phone', 'email', 'membership_start_date']

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['membership_start_date'].initial = datetime.date.today()
