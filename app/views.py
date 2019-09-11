from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .serializers import TextsSerializers
from .models import Texts
from .forms import TextForm, TitlesForm, TitleForm
from .predict import make_prediction


def get_all_titles(request):
    try:
        keys = Texts.objects.all()
        serializer = TextsSerializers(keys, many=True)
        return render(
            request, "get_all_titles.html",
            context={"titles": serializer.to_internal_value()}
        )
    except BaseException as e:
        return HttpResponse(status=404)


def add_text(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text_value = request.POST.get("text_value")
        tags = request.POST.get("tags")
        text = Texts.objects.create(
            title=title, text_value=text_value, tags=tags
        )
        return render(request, "index.html")
    else:
        textform = TextForm()
        return render(request, "add_text.html", {"titles": textform})


def get_prediction(request):
    if request.method == "POST":
        titles_liked = dict(request.POST).get("titles_liked", "")
        titles_dislike = dict(request.POST).get("titles_dislike", "")
        title = make_prediction(titles_liked, titles_dislike)
        return render(request, "prediction.html", {"title": title})
    else:
        titles = TitlesForm()
        return render(
            request, "get_prediction.html",
            {"titles": titles}
        )


def prediction(request):
    return render(request, "index.html")


def index(request):
    return render(request, "index.html")
