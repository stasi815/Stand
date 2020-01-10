from django import forms
from auctions.models import Auction, Item

class AuctionsForm(forms.ModelForm):
    """ Render and process a form based on the Auction model. """

    class Meta:
        model = Auction
        fields = ['name', 'description', 'start_date', 'end_date', 'item']

class ItemForm(forms.ModelForm):
    """ Render and process a form based on the Item model. """

    class Meta:
        model = Item
        fields = ['name', 'description','starting_bid', 'min_bid_increment', 'value', 'current_bid', 'image']

