from django.shortcuts import render, get_object_or_404
from .models import Member
from books.models import Book
from books.forms import BookForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView


class MemberListView(LoginRequiredMixin,ListView):
	model = Member
	context_object_name = 'members'


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    fields = '__all__'
    
    def form_valid(self, form):
        return super().form_valid(form)


class MemberUpdateView(LoginRequiredMixin, UpdateView):
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


class MemberBooksView(ListView):
    model = Book
    context_object_name = 'books'

def user_returned(request, m_id):
    member = get_object_or_404(Member, pk=m_id)
    pending = Book.objects.get(returned=False, member=member)
    return render(request, 'users/member_detail.html', {'pending': pending})


    

