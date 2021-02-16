from django.shortcuts import render
from .models import questions, answers
# Create your views here.
def Home(request):
    ques = questions.objects.all().order_by('uploaded_at')
    if request.method == "POST":
        question = request.POST['question']
        que_obj = questions(question_name=question,asked_by=request.user)
        que_obj.save()
    return render(request,"qa/homepage.html",{"questions":ques})


def DetailView(request,id):
    context = {}
    if request.method == "POST":
        answer = request.POST['answer']
        ans_obj = answers(answer=answer)
        ans_obj.save()
        print(ans_obj)
        try:
            question = questions.objects.get(pk=id)
            question.answer_ques.add(ans_obj)
        except:
            print("no such questions")
    try:
        question = questions.objects.get(pk=id)
        context['question'] = question
    except:
        context['question'] = None
    return render(request,'qa/details.html',context)
