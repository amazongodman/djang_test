from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

#定義したクラスを読み込む
from .models import Question



def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    ques = Question.objects.order_by('-pub_date')

    return render(request, 'polls/index.html', {'poll':ques})




def poll_detail(request, poll_id):
    return render(request, 'polls/poll_detail.html',{'poll_id':poll_id})







