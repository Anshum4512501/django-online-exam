from django.shortcuts import render,reverse,get_object_or_404
from django.views.generic import View
from .models import Question,Choice,Answer
from django.http import HttpResponse,HttpResponseRedirect
from .forms import QuestionForm,ChoiceForm
from django.views.generic import ListView,DetailView,UpdateView,CreateView
# Create your views here.

class QuestionView(View):
    def get(self,request,*args,**kwargs):
        form = QuestionForm()
        return render(request,'onlinexam/question.html',{'form':form})

    def post(self,request,*args,**kwargs):
        print(request.POST)
        form =QuestionForm(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('question-list'))


class QuestionList(ListView):
    template_name = 'onlinexam/questionlist.html'
    queryset = Question.objects.all()
            
class QuestionDetailView(DetailView):
    template_name = 'onlinexam/questiondetailview.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Question,id=id_)            
            
class QuestionUpdateView(UpdateView):
    template_name = 'onlinexam/question.html'
    form_class = QuestionForm

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Question,id=id_)
        
    def form_valid(self, form):

        return super().form_valid(form)


class ChoiceViewCreate(CreateView):
    template_name = 'onlinexam/choice.html'
    form_class = ChoiceForm

    def form_valid(self, form):
        
        return super().form_valid(form)