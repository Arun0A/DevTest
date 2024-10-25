from django.shortcuts import render, HttpResponse, redirect
import pandas as pd
from .forms import UploadFileForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def display(request):
    return render(request, "display.html")

def upload_file(request):
    if request.method == 'POST':
        if request.FILES.get('file', None):
            file = request.FILES['file']
            
            if file.name.endswith('.csv'):
                data = pd.read_csv(file)
            elif file.name.endswith('.xls') or file.name.endswith('.xlsx'):
                data = pd.read_excel(file)
            else:
                return render(request, 'upload.html', {
                    'error': 'Unsupported file type. Please upload a CSV or Excel file.'
                })
            
            try:
                data = data[['Cust State','Cust Pin','DPD']]
            except:
                pass
            
            table_html = data.to_html(classes='table table-striped', index=False)
            
            return render(request, 'display.html', {'table': table_html})

        else:
            return render(request, 'upload.html', {
                'error': 'No file uploaded. Please upload a file.'
            })
    
    return render(request, 'upload.html')