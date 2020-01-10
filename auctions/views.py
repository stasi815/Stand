from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse

from .models import Auction, Item, Organization
from auctions.forms import AuctionsForm, ItemForm


# def index(request):
#     return HttpResponse("Hello world.")

class AuctionsList(ListView):
    """ Renders a list of Auctions """
    model = Auction
    template_name = 'auctions/home.html'
    context_object_name = 'auctions'

    def get(self, request):
        """ GET a list of ceremonies. """
        auctions = self.get_queryset().all()
        return render(request, 'auctions/home.html', {
            'auctions': auctions
        })

class AuctionDetailView(DetailView):
    model = Auction
    
    def get(self, request, slug):
        """ Returns a specific auction page by slug. """
        auction = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'auctions/auction_details.html', {
            'auction': auction
        })

class AuctionCreateView(CreateView):
    """ Renders a form for creating a new auction. """
    def get(self, request, *args, **kwargs):
        context = {'form': AuctionsForm()}
        return render(request, 'auctions/new_auction.html', context)

    def post(self, request, *args, **kwargs):
        form = AuctionsForm(request.POST)
        if form.is_valid():
            auction = form.save()
            return HttpResponseRedirect(reverse_lazy('auction-details-page', args=[auction.slug]))
        return render(request, 'auctions/new_auction.html', {'form':form})

class AuctionEditView(UpdateView):
    """ Renders a form for editing an auction. """
    model = Auction
    template_name = 'auctions/auction_edit.html'
    form_class = AuctionsForm

    def get_success_url(self):
        return reverse('auction-details-page', kwargs={'slug':self.object.slug,})

class AuctionDeleteView(DeleteView):
    """ Renders deletion of an auction. """
    model = Auction
    success_url = reverse_lazy('auctions-list-page')

    def get(self, *args, **kwargs):
        return self.delete(*args, **kwargs)

class ItemDetailView(DetailView):
    model = Item
    
    def get(self, request, slug):
        """ Returns a specific item page by slug. """
        item = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'auctions/item_details.html', {
            'item': item
        })    
class ItemCreateView(CreateView):
    """ Renders a form for creating a new item. """
    def get(self, request, *args, **kwargs):
        context = {'form': ItemForm()}
        return render(request, 'auctions/new_item.html', context)

    def post(self, request, *args, **kwargs):
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save()
            return HttpResponseRedirect(reverse_lazy('item-details-page', args=[item.slug]))
        return render(request, 'auctions/new_item.html', {'form':form})