import subprocess
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    ls = subprocess.run(
            ['ls', '-alt'],
            stdout=subprocess.PIPE,
            text=True
    )
    content = ls.stdout.replace("\n", "</br>")
    gitdag = subprocess.run(
            ['git', 'dag'],
            stdout=subprocess.PIPE,
            text=True
    )
    gdcontent = gitdag.stdout.replace("\n", "</br>")
    return HttpResponse(f"<pre>{content}</br></br></br>{gdcontent}</pre>")

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
