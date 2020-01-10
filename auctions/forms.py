from django import forms
from auctions.models import Auction

class AuctionsForm(forms.ModelForm):
    """ Render and process a form based on the Auction model. """

    class Meta:
        model = Auction
        fields = ['name', 'description', 'start_date', 'end_date', 'items']
