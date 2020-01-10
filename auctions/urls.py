from django.urls import path
from .views import AuctionsList, AuctionDetailView, AuctionCreateView

urlpatterns = [
    path('', AuctionsList.as_view(), name='auctions-list-page'),
    path('new-auction/', AuctionCreateView.as_view(), name='new-auction-page'),
    path('auctions/<str:slug>/', AuctionDetailView.as_view(), name='auction-details-page'),
]