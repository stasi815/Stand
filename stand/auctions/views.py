from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Auction, Item, Organization


# def index(request):
#     return HttpResponse("Hello world.")

class AuctionsList(ListView):
    """ Renders a list of Auctions """
    model = Auction
    template_name = 'auctions/home.html'
    context_object_name = 'auctions'

class AuctionDetailView(DetailView):
    model = Auction
    template_name = 'auctions/auction_details.html'
    context_object_name = 'auction'
