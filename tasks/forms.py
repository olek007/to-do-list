from django import forms

from tasks.models import Tag, Task


class TaskForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea)

    deadline = forms.DateTimeField(
        required=False,
        input_formats=["%d/%m/%Y %H:%M"],
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
    )

    is_complete = forms.BooleanField(widget=forms.CheckboxInput, required=False)
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    class Meta:
        model = Task
        fields = "__all__"


class TagForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Tag
        fields = "__all__"
