import datetime
 
# from haystack import site
from haystack.indexes import *
 
from polls.models import *
 
class ReportIndex(SearchIndex, Indexable):
    text = CharField(document=True, use_template=True)
    title = CharField(model_attr='title')
    publisher = CharField(model_attr='publisher')
    date = DateTimeField(model_attr='date')

    def get_model(self):
        return Report

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(date__lte=datetime.datetime.now())
 
# site.register(Entry, EntryIndex)