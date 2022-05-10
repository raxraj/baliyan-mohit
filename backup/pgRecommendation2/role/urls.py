from django.urls import path
from .views import home, registerA,registerM, dashboardA , dashboardM , logout, addPropertyM , searchPropertyM , uploadA , uploadM ,  editProfileA , editProfileM 
urlpatterns = [
    path('', home, name='home'),
    path('registerA/', registerA, name='registerA'),
    path('registerM/', registerM, name='registerM'),
    path('dashboardA/',dashboardA, name='dashboardA'),
    path('dashboardM/',dashboardM, name='dashboardM'),
    path('logout/',logout, name='logout'),
    path('addPropertyM/',addPropertyM, name='addPropertyM'),
    path('searchPropertyM/',searchPropertyM, name='searchPropertyM'),
    path('editProfileA/?P<int:doctor_id>/',editProfileA, name='editProfileA'),
    path('editProfileM/?P<int:patient_id>/',editProfileM, name='editProfileM'),
    path('uploadA/?P<int:doctor_id>/',uploadA, name='uploadA'),
    path('uploadM/?P<int:patient_id>/',uploadM, name='uploadM'),
]
