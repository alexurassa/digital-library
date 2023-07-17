from django import forms
from ..models import ResourceBorrow


class BorrowForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BorrowForm, self).__init__(*args, **kwargs)
        self.fields["due_timestamp"].widget = forms.DateTimeInput(
            attrs={"type": "datetime-local"}
        )

    class Meta:
        model = ResourceBorrow
        exclude = ["id", "issue_timestamp", "user"]
