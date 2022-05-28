from django.http import HttpResponse
from django.views.generic import ListView
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect


from .forms import ContactForm
from .models import Post, Category, PostPortfolio


# Create your views here.

class AppListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    # paginate_by = 9
    template_name = 'app/index.html'


def post_list(request):
    posts = Post.published.all()
    categories = Category.objects.all()
    port_posts = PostPortfolio.published.all()

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry" 
            body = {
            'full_name': form.cleaned_data['full_name'], 
            'email': form.cleaned_data['email_address'], 
            'message':form.cleaned_data['message'], 
            }
            message = "\n".join(body.values())

            send_mail(subject, message, 'satipovakbar@gmail.com', ['satipovakbar@gmail.com']) 

            
    form = ContactForm()
    

    return render(request, 'app/index.html',{
        'posts': posts,
        'port_posts': port_posts,
        'categories': categories,
        'form': form, 
        })

