from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def home(request):
    cursor = connection.cursor()
    cursor.execute("select * from posts where softdelete = 0")

    columns = [col[0] for col in cursor.description]
    posts =  [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]
    print(posts)
    context = {
        'keyposts': posts

    }
    return render(request,'blogapp/hello.html',context)

def about(request):
    return HttpResponse("hello")

def create(request):
     return render(request,'blogapp/form.html')


def insert(request):
    # print(request)
    title = request.POST['blogTitle']
    content = request.POST['content']
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (`title`,`content`) VALUES ( %s, %s );", (title, content))
    cursor = connection.cursor()
    cursor.execute("SELECT * from posts where softdelete = 0 and  id=<pk}")
    print(post)
    return redirect('/blog/home')



def edit(request, pk):
    print(pk)
    return render(request,'blogapp/formedit.html')



def update(request):
    title = request.POST['blogTitle']
    content = request.POST['content']
    id=request.POST['id']
    cursor = connection.cursor()
    cursor.execute("UPDATE posts set title = %s,content=%s where id=%s",(title,content,id))
    print(post)
    return redirect('/blog/home')

    context={
        'keyposts':posts[0],
    }
    print(context)
    return render(request,'blogapp/editform.html',context)
