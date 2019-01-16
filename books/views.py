from django.shortcuts import render
from .models import Book

# Create your views here.
def detail(request, member_id):
    form = BookForm(request.POST or None, request.FILES or None)
    member = get_object_or_404(Member, pk=member_id)
    if form.is_valid():
        book = form.save(commit=False)
        book.member = member.member_id
        book.save()
    form = BookForm()
    return render(request, 'users/member-detail.html', {'form': form, 'member': member})