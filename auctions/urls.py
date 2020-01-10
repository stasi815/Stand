from django.urls import path
from .views import AuctionsList, AuctionDetailView, AuctionCreateView, AuctionDeleteView, AuctionEditView, ItemDetailView, ItemCreateView

urlpatterns = [
    path('', AuctionsList.as_view(), name='auctions-list-page'),
    path('new-auction/', AuctionCreateView.as_view(), name='new-auction-page'),
    path('auctions/<str:slug>/', AuctionDetailView.as_view(), name='auction-details-page'),
    path('auctions/<str:slug>/update', AuctionEditView.as_view(), name='auction-update-page'),
    path('auctions/<str:slug>/delete', AuctionDeleteView.as_view(), name='auction-delete'),
    path('auctions/item/<str:slug>/', ItemDetailView.as_view(), name='item-details-page'),
    path('new-item/', ItemCreateView.as_view(), name='new-item-page'),
]