from django.contrib import admin
from movie_t1.models import MovieDetail,MovieKind
# Register your models here.

class MovieDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(MovieDetail,MovieDetailAdmin)


class MovieKindAdmin(admin.ModelAdmin):
    pass

admin.site.register(MovieKind,MovieDetailAdmin)