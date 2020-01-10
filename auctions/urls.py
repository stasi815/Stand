from django.urls import path
from .views import AuctionsList, AuctionDetailView, AuctionCreateView, AuctionDeleteView, AuctionEditView

urlpatterns = [
    path('', AuctionsList.as_view(), name='auctions-list-page'),
    path('new-auction/', AuctionCreateView.as_view(), name='new-auction-page'),
    path('auctions/<str:slug>/', AuctionDetailView.as_view(), name='auction-details-page'),
    path('auctions/<str:slug>/update', AuctionEditView.as_view(), name='auction-update-page'),
    path('auctions/<str:slug>/delete', AuctionDeleteView.as_view(), name='auction-delete'),
]