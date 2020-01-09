from django.urls import path
from .views import AuctionsList, AuctionDetailView

urlpatterns = [
    path('', AuctionsList.as_view(), name='auctions-list-page'),
    path('<slug>/', AuctionDetailView.as_view(), name='auction-details-page')
]