from django.contrib import admin
from Articles.models import Publication, Article, Magazine
from writer.models import Reporter, Editor, Publisher


class publications_name(admin.ModelAdmin):
    list_display = ['headline', 'text', 'publications_name',
                    'pub_date','reporter']
    list_filter = ['headline']
    search_fields = ['headline']


admin.site.register(Publisher)
admin.site.register(Magazine)
admin.site.register(Publication)
admin.site.register(Article,publications_name)
admin.site.register(Reporter)
admin.site.register(Editor)
