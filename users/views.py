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



def detail(request, m_id):
    form = BookForm(request.POST)
    member = get_object_or_404(Member, pk=m_id)
    if form.is_valid():
        book = form.save(commit=False)
        book.member = member
        book.save()
        return render(request, 'users/member_detail.html', {'form': form, 'member': member})
    context = {
        'member': member,
        'form': form,
    }
    return render(request, 'users/member_detail.html', context)

    

    

