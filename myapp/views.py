from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from .models import SurveyResponse
from .serializers import SurveyResponseSerializer
import logging
from django.conf import settings
import joblib
import numpy as np
import pandas as pd

def home(request):
    return HttpResponse("Hello, world!")

@api_view(['POST'])
def submit_survey(request):
    if request.method == 'POST':
        serializer = SurveyResponseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

model = joblib.load('modelfiles\\model1')

class PredictView(APIView):
    def get(self, request, *args, **kwargs):
        # Retrieve the latest survey response
        survey_response = SurveyResponse.objects.latest('id')

        # age = int(survey_response.age)

        # Prepare the input data for the model
        input_data = np.array([
            survey_response.age,
            survey_response.gender,
            survey_response.weight,
            # survey_response.working,
            # survey_response.work_shift,
            # survey_response.job_nature,
            # survey_response.lift_heavy_weights,
            # survey_response.use_devices_often,
            survey_response.sitting_hours,
            # survey_response.fast_food_frequency,
            survey_response.consume_oily_spicy_food,
            # survey_response.dinner_time,
            survey_response.digestion_problems,
            # survey_response.stool_frequency,
            survey_response.buttock_pain,
            survey_response.cutting_pain,
            survey_response.burning_sensation,
            survey_response.itching,
            survey_response.pile_mass_coming_out,
            # survey_response.pile_mass_condition,
            # survey_response.bleeding_amount,
            survey_response.pus_discharge,
            # survey_response.anus_swelling,
            # survey_response.first_time_swelling,
            # survey_response.body_hair_type,
            survey_response.diabetes,
            survey_response.bleeding_issue,
            survey_response.bleeding_type,
            survey_response.blood_color,
            survey_response.boils_around_anus,
            # survey_response.redness_swelling,
            # survey_response.treatment_type,
            # survey_response.treatment_kind,
            # survey_response.blood_color_during_treatment,
            # survey_response.recurrence,
            # survey_response.relapse_frequency,
            # survey_response.pain_while_sitting,
            # survey_response.pain_while_defecation,
            # survey_response.weight_loss,
            # survey_response.just_delivered_baby,
            # survey_response.family_anal_cancer,
            # survey_response.first_time_doctor_visit
        ]).reshape(1, -1)

        # Make predictions using the model
        # prediction = model.predict(input_data)
        # prediction = input_data

        label_encoders = joblib.load('modelfiles\\label_encoders.pkl')
        model = joblib.load('modelfiles\\model1')

        columns = [
            'Age', 'Gender', 'Weight', 'sitting_hours', 'oily_spicy', 'Constipation', 'endure_pain',
            'cutting_pain', 'Burning_pain', 'Itching', 'Mass_coming_out', 'pus_discharge', 'Diabetic',
            'Bleeding', 'Bleeding_type', 'Blood_color', 'boils'
        ]

        # Function to preprocess incoming data
        def preprocess_data(new_data, label_encoders, columns):
            # Create a DataFrame from the list
            df = pd.DataFrame(new_data, columns=columns)
            
            # Apply LabelEncoders to the relevant columns, excluding 'Age'
            for column in columns:
                if column != 'Age' and column in label_encoders:
                    le = label_encoders[column]
                    df[column] = le.transform(df[column].apply(lambda x: x.lower()))
            
            return df

        # Function to handle new data and make predictions
        def handle_new_data(new_data):
            # Preprocess the data
            processed_data = preprocess_data(new_data, label_encoders, columns)
            
            # Predict using the model
            predictions = model.predict(processed_data)
            return predictions

        # new_data = [["30", "male", "60 - 70 kg", "6 - 8 hrs", "Yes", "No", "None", "No", "No", "No", "No", "No", "No", "No", "Sticking with stool", "Red", "No"]]
        prediction = handle_new_data(input_data)

        # Return the prediction as a JSON response
        return JsonResponse({"prediction": prediction.tolist()})