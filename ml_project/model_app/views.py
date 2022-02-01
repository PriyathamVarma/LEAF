from django.shortcuts import render
from joblib import load
from django.http import HttpResponse, HttpResponseRedirect
from model_app.models import Leaf
# forms imports
from . import forms
#model = load('../savedModels/RandomForestClassifier.joblib')

# Create your views here.
def predictor(request):
    data = Leaf.objects.order_by('sepal_length')

    if request.method == "POST":
        
        form = forms.FormNamedata(request.POST)
        
        if form.is_valid():
            print("Validation Success")

            form.save()
            """Sepal_length = request.POST.get('sepal_length')
            Sepal_Width  = request.POST.get('sepal_width')
            Petal_length = request.POST.get('petal_length')
            Petal_width  = request.POST.get('petal_width')"""

            """my_dict = {

            Sepal_length : Sepal_length,
            Sepal_Width  : Sepal_Width,
            Petal_length : Petal_length,
            Petal_width  : Petal_width
                        }"""   
    form = forms.FormName()                      
    my_dict = {'data':data,'form':form}
    return render(request,'index.html',my_dict)    


    