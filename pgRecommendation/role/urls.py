from django.urls import path
from .views import home, registerA,registerM, dashboardA , dashboardM , logout, addPropertyM , searchPropertyM , addPropertyA , searchPropertyA , showProperty , otpM , uploadA , uploadM ,  editProfileA , editProfileM 
urlpatterns = [
    path('', home, name='home'),
    path('registerA/', registerA, name='registerA'),
    path('registerM/', registerM, name='registerM'),
    path('dashboardA/',dashboardA, name='dashboardA'),
    path('dashboardM/',dashboardM, name='dashboardM'),
    path('logout/',logout, name='logout'),
    path('otpM/',otpM, name='otpM'),
    path('addPropertyM/',addPropertyM, name='addPropertyM'),
    path('searchPropertyM/',searchPropertyM, name='searchPropertyM'),
    path('addPropertyA/',addPropertyA, name='addPropertyA'),
    path('searchPropertyA/',searchPropertyA, name='searchPropertyA'),
    path('showProperty/?P<int:prop_id>/',showProperty, name='showProperty'),
    path('editProfileA/?P<int:doctor_id>/',editProfileA, name='editProfileA'),
    path('editProfileM/?P<int:patient_id>/',editProfileM, name='editProfileM'),
    path('uploadA/?P<int:doctor_id>/',uploadA, name='uploadA'),
    path('uploadM/?P<int:patient_id>/',uploadM, name='uploadM'),
]
