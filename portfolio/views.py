from django.shortcuts import render, get_object_or_404
from .models import PostPortfolio

# Create your views here.



def portfolio_list(request):
    port_posts = PostPortfolio.published.all()

    return render(request, 'app/index.html',{
        'port_posts': port_posts,
        })