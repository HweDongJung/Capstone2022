from django.db import connection,transaction
from django.shortcuts import render, redirect
from .models import Board,BoardContents
from django.core.paginator import Paginator
# Create your views here.

def list(request):
    boards = Board.objects
    boardList = Board.objects.filter(Category='Category1')
    paginator = Paginator(boardList,'5')
    page = request.GET.get('page',1)
    posts = paginator.page(page)
    return render(request, 'list.html',{"boards":boards,"posts":posts})

def write(request):
    return render(request, 'write.html')

def view(request,p):
    boardContents = BoardContents.objects.get(TeaserID = p)
    contents = str(boardContents).split(',')
    clickedUp(contents,p)
    return render(request, 'view.html', {"boardContents":contents})

def clickedUp(contents,p):
    with connection.cursor() as cursor:
        clicked = int(contents[4])+1
        cursor.execute("update brainTeaser set Clicked = %d where teaserID = %d"%(clicked,p))

def edit(request,p):
    print(p)
    board_Contents = BoardContents.objects.get(TeaserID = p)

    if request.method == "POST":
        board_Contents.Title = request.POST['title']
        board_Contents.Teaser = request.POST['text']
        board_Contents.save()
        return redirect('/questions/list/post=' + str(p))

    else:
        return render(request, 'edit.html', {'bdc':board_Contents})