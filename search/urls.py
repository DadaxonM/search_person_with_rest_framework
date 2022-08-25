from django.urls import path
from search.views import CountryListView,CountryCreateView,CountryDetailView,CountryDetailUpdateDeleteView,\
    RegionListView,RegionCreateView,RegionDetailView,RegionDetailUpdateDeleteView,\
    PersonListView,PersonCreateView,PersonDetailView,PersonDetailUpdateDeleteView,UnknownPersonDetail,AllPersonEncode


urlpatterns = [
    path('country/list', CountryListView.as_view()),
    path('country/detail/<int:pk>', CountryDetailView.as_view()),
    path('country/create', CountryCreateView.as_view()),
    path('country/updatedelete/<int:pk>', CountryDetailUpdateDeleteView.as_view()),
    path('region/list', RegionListView.as_view()),
    path('region/detail/<int:pk>', RegionDetailView.as_view()),
    path('region/create', RegionCreateView.as_view()),
    path('region/updatedelete/<int:pk>', RegionDetailUpdateDeleteView.as_view()),
    path('person/list', PersonListView.as_view()),
    path('person/detail/<int:pk>', PersonDetailView.as_view()),
    path('person/create', PersonCreateView.as_view()),
    path('person/updatedelete/<int:pk>', PersonDetailUpdateDeleteView.as_view()),
    path('unkperson/detail', UnknownPersonDetail.as_view()),
    path('encode_person/all', AllPersonEncode),
]