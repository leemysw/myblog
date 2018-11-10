from django.forms import ModelForm, Textarea
from ckeditor.widgets import CKEditorWidget

from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': Textarea(attrs={'id': 'comment-content'}, )
        }
