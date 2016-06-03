from django.shortcuts import render

from search.forms import ReportSearchForm
from polls.models import Report
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.db.models import Q

# Create your views here.
def search_report(request):
	if request.method == 'POST':
        form = ReportSearchForm()
        if request.method == 'GET':
            return render_to_response('search/search.html', {'form': form}, RequestContext(request))
        elif request.method == 'POST':
            form = ReportSearchForm(request.POST)
            reports = Report.objects.all()
            if form.is_valid():
                books = book.filter(Q(title__contains=form.cleaned_data['title']) | Q(subtitle__contains=form.cleaned_data['title']))
        return render_to_response('search/search.html', {'form':form, 'reports':reports}, RequestContext(request))
    else:
        form = ReportSearchForm()
        return render_to_response('search/search.html', )

