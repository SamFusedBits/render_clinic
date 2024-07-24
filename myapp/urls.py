from django.urls import path
from .views import home
from .views import submit_survey, PredictView

urlpatterns = [
    path('', home, name='home'),
    path('submit/', submit_survey, name='submit_survey'),
    path('predict/', PredictView.as_view(), name='predict')
    # path('api/submit/', SubmitFormView.as_view(), name='submit-form'),
    # path('api/formdata/', FormDataListView.as_view(), name='form-data-list'),
]