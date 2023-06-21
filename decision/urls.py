
from django.conf import settings
from django.shortcuts import redirect
from django.urls import path
from decision.views import change_done,account_view, decision_details, download_file, index, login_view, meeting, meeting_details, rec, recs,CustomLoginView
# from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', lambda request: redirect('app/')),
    path('app/', index, name='home'),
    # path('login/', login_view,name='login'),
    path('account/',  account_view,name='account'),
    path('recs/', recs ,name='recs'),
    path('meeting/', meeting,name='meeting'),
    path('meeting/<str:pk>', meeting_details,name='meetingdetail'),
    path('meeting/<str:slug>/<str:pk>', decision_details,name='decisiondetail'),
    path('changedone/<str:pk>', change_done,name='change-done'),
    path('recs/<str:pk>', rec ,name='recs-details'),
    # path('logout/', logout_view, name='logout'),
 
    path('logout/', LogoutView.as_view(), name='logout'),
    path('downloadfile/<str:pk>', download_file, name='download'),

    path('login/', login_view, name='login'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
