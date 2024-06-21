from django.shortcuts import render
from django.http import JsonResponse
from django.forms import formset_factory
from .forms import CourseForm

# Create your views here.
def home(request):
    return render(request, 'calc1/home.html')

def about(request):
    return render(request, 'calc1/about.html')

def calculate(request):
    CourseFormSet = formset_factory(CourseForm,extra=1)
    if request.method == 'POST':
        formset = CourseFormSet(request.POST,request.FILES)
        data ={ "form-TOTAL_FORMS": 5,
                }
        print(formset)
        if formset.is_valid():
            total_credits = 0
            weighted_sum = 0
            count=0
            #print(formset)
            for form in formset:
                print(form.cleaned_data)
                credits = float(form.cleaned_data['credits'])
                grade = float(form.cleaned_data['grade'])
                count+=1
                total_credits += credits
                weighted_sum += credits * grade
                #print(total_credits,weighted_sum,count)
            if total_credits > 0:
                cgpa = weighted_sum / total_credits
                cgpa_formatted = "{:.2f}".format(cgpa)
                #print(cgpa_formatted)
            #cgpa = weighted_sum / total_credits if total_credits > 0 else 0
            #cgpa_formatted = '{:.2f}'.format(cgpa)
            #cgpa_formatted = round(cgpa, 2)
            #cgpa_formatted = f"{cgpa:.2f}"
            return JsonResponse({'cgpa': cgpa_formatted})
    else:
        formset = CourseFormSet()
    return render(request, 'calc1/calculate.html', {'formset': formset})
