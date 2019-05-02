from django.shortcuts import render
from django.shortcuts import HttpResponse
from movie_t1.models import MovieDetail

# Create your views here.
def index(request):

    featured_movies = MovieDetail.objects.filter(kind__name="GD")
    top_viewed_movies = MovieDetail.objects.filter(kind__name="RFS")
    top_rating_movies = MovieDetail.objects.filter(kind__name="MJG")
    recently_add_movies = MovieDetail.objects.filter(kind__name="gfd")

    data = MovieDetail.objects.all().order_by('-id')
    movie = data[0]
    return render(request, 'index.html', {"jpm": movie, "movies": data, 'GD': featured_movies, 'RFS':top_viewed_movies,
                                          'MJG': top_rating_movies, 'gfd': recently_add_movies})


def index1(request, movie_id):
    # pramary key
    try:
        movie = MovieDetail.objects.filter(pk=movie_id)[0]
    except Exception:
        return HttpResponse("not found")
    return render(request, 'single.html', {"movie": movie})