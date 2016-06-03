from django.forms import ModelForm
from polls.models import Report, Comment


class ReportForm(ModelForm):
    """日報のフォーム"""
    class Meta:
        model = Report
        fields = ('title', 'publisher', 'content' )


class CommentForm(ModelForm):
    """コメントのフォーム"""
    class Meta:
        model = Comment
        fields = ('comment', 'commenter' )