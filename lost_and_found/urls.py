from django.urls import path
from . import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    path('', views.LostAndFoundView.as_view(), name='lost_and_found'),
    path('report-missing', views.ReportMissingView.as_view(), name='report_missing'),
    path('missing-person-found', views.MissingPersonFound.as_view(), name='missing_person_found')
] 