from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from django.views.generic.list import ListView

from django.contrib.auth.decorators import login_required

from polls.models import Report, Comment
from polls.forms import ReportForm, CommentForm

# Create your views here.
# @login_required
def report_list(request):
    """日報の一覧"""
    reports = Report.objects.all().order_by('id')
    return render(request,
                  'polls/report_list.html',     # 使用するテンプレート
                  {'reports': reports})         # テンプレートに渡すデータ


@login_required
def report_edit(request, report_id=None):
    """日報の編集"""
    if report_id:   # report_id が指定されている (修正時)
        report = get_object_or_404(Report, pk=report_id)
    else:         # report_id が指定されていない (追加時)
        report = Report(user=request.user)

    if request.method == 'POST':
        form = ReportForm(request.POST, instance=report)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            report = form.save(commit=False)
            report.save()
            return redirect('polls:report_list')
    else:    # GET の時
        form = ReportForm(instance=report)  # report インスタンスからフォームを作成

    return render(request, 'polls/report_edit.html', dict(form=form, report_id=report_id))


@login_required
def report_del(request, report_id):
    """書籍の削除"""
    report = get_object_or_404(Report, pk=report_id)
    report.delete()
    return redirect('polls:report_list')

# @login_required
class CommentList(ListView):
    """感想の一覧"""
    context_object_name='comments'
    template_name='polls/comment_list.html'
    paginate_by = 20  # １ページは最大2件ずつでページングする

    def get(self, request, *args, **kwargs):
        report = get_object_or_404(Report, pk=kwargs['report_id'])  # 親の書籍を読む
        comments = report.comment.all().order_by('id')   # 書籍の子供の、感想を読む
        self.object_list = comments
        # report_content = report.content
		# {'report_content':report.content}]

        context = self.get_context_data(object_list=self.object_list, report=report)    
        return self.render_to_response( context )

@login_required
def comment_edit(request, report_id, comment_id=None):
    """感想の編集"""
    report = get_object_or_404(Report, pk=report_id)  # 親の書籍を読む
    if comment_id:   # comment_id が指定されている (修正時)
        comment = get_object_or_404(Comment, pk=comment_id)
    else:               # comment_id が指定されていない (追加時)
        comment = Comment()

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)  # POST された request データからフォームを作成
        if form.is_valid():    # フォームのバリデーション
            comment = form.save(commit=False)
            comment.report = report  # この感想の、親の書籍をセット
            comment.save()
            return redirect('polls:comment_list', report_id=report_id)
    else:    # GET の時
        form = CommentForm(instance=comment)  # comment インスタンスからフォームを作成

    return render(request,
                  'polls/comment_edit.html',
                  dict(form=form, report_id=report_id, comment_id=comment_id))

@login_required
def comment_del(request, report_id, comment_id):
    """感想の削除"""
    comment = get_object_or_404(Comment, pk=comment_id)
    comment.delete()
    return redirect('polls:comment_list', report_id=book_id)