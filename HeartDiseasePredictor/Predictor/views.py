from django.shortcuts import render

from django.http import HttpResponse

import joblib
import pandas as pd

model = joblib.load("C:/Users/srich/Heart Disease Project/HeartDiseasePredictor.pkl")

def home(request):
        if request.method == "POST":

            '''age = int(request.POST.get("age"))
            sex = int(request.POST.get("gender"))
            cp = int(request.POST.get("chestPain"))
            trestbps = int(request.POST.get("restingBP"))
            chol = int(request.POST.get("cholesterol"))
            fbs = int(request.POST.get("fastingSugar"))
            restecg = int(request.POST.get("ecgResults"))
            thalach = int(request.POST.get("maxHeartRate"))
            exang = int(request.POST.get("exerciseAngina"))
            oldpeak = float(request.POST.get("stDepression"))
            slope = int(request.POST.get("slope"))
            ca = int(request.POST.get("vessels"))
            thal = int(request.POST.get("thallium"))

            model_input = [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]'''

            data_dict = {
                'age' : int(request.POST.get("age")),
                'sex' : int(request.POST.get("gender")),
                'cp' : int(request.POST.get("chestPain")),
                'trestbps' : int(request.POST.get("restingBP")),
                'chol' : int(request.POST.get("cholesterol")),
                'fbs' : int(request.POST.get("fastingSugar")),
                'restecg' : int(request.POST.get("ecgResults")),
                'thalach' : int(request.POST.get("maxHeartRate")),
                'exang' : int(request.POST.get("exerciseAngina")),
                'oldpeak' : float(request.POST.get("stDepression")),
                'slope' : int(request.POST.get("slope")),
                'ca' : int(request.POST.get("vessels")),
                'thal' : int(request.POST.get("thallium"))
            }

            model_input = pd.DataFrame(data_dict, index=[0])

            prediction = model.predict(model_input)

            if prediction == 1:
                pred = "Yes, you are prone to heart disease"
            else:
                pred = "No worries, you are healthy"
        
            context = {'output': pred}

            return render(request, 'home.html', context)

        return render(request, 'home.html')