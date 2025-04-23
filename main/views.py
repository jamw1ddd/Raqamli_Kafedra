from django.shortcuts import render,redirect
from .models import StaffMember, Post
from .forms import ContactForm
from django.contrib import messages


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Post, StaffMember
from .forms import ContactForm

def index(request):
    posts = Post.objects.order_by('-date_posted')[:4]
    members = StaffMember.objects.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Xabaringiz muvaffaqiyatli yuborildi!")
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'posts': posts,
        'members': members,
        'form': form
    }
    return render(request, 'index.html', context)


# def staff(request):
#     members = StaffMember.objects.all()
#     return render(request, 'index.html', {'members': members})

def posts(request):
    posts = Post.objects.order_by('-date_posted')
    return render(request, 'meetings.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'meeting-details.html', {'post': post})

def members(request):
    members = StaffMember.objects.all()
    return render(request, 'members.html', {'members': members})

def about(request):
    return render(request, 'about.html')