from django.shortcuts import render, get_object_or_404
from .models import Member
from books.forms import BookForm
from django.views.generic import ListView, CreateView, UpdateView


class MemberListView(ListView):
	model = Member
	context_object_name = 'members'


class MemberCreateView(CreateView):
    model = Member
    fields = '__all__'
    
    def form_valid(self, form):
        return super().form_valid(form)


class MemberUpdateView(UpdateView):
    model = Member

    fields = ['fname', 'sname', 'dob', 'school', 'level', 'zone', 'contact']

    def form_valid(self, form):
        return super().form_valid(form)



def detail(request, member_id):
    form = BookForm(request.POST or None, request.FILES or None)
    member = get_object_or_404(Member, pk=member_id)
    if form.is_valid():
        book = form.save(commit=False)
        book.member = member
        book.save()
    form = BookForm()
    return render(request, 'users/member_detail.html', {'form': form, 'member': member})

    

    

