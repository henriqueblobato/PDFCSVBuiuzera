import json

from django.shortcuts import render, redirect
from .forms import PDFUploadForm
import tabula

from .models import UploadedPDF


def upload_pdf(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = form.save()
            print(f'Saved pdf_file: {pdf_file}')
            # csv_content = extract_csv_from_pdf(pdf_file.pdf_file.path)
            # request.session['csv_content'] = csv_content
            # return redirect('show_csv')
    else:
        form = PDFUploadForm()
    return render(request, 'upload.html', {'form': form})


def show_csv(request):
    # get content from all UploadedPDF objects
    csv_content = []
    for pdf in UploadedPDF.objects.all():
        pdf_file = pdf.pdf_file.path
        print(f'pdf_file: {pdf_file}')
        # file_data = extract_csv_from_pdf(pdf_file)
        file_data = {
            'File': pdf.pdf_file.name.split('/')[-1],
            **extract_csv_from_pdf(pdf_file)
        }
        csv_content.append(file_data)
        # csv_content.append(extract_csv_from_pdf(pdf_file))
    # csv_content = request.session.get('csv_content')
    # csv_content = json.dumps(csv_content)
    csv_content = json.dumps(csv_content)
    return render(request, 'show_csv.html', {'csv_content': csv_content})


def extract_csv_from_pdf(pdf_path):
    tables = tabula.read_pdf(pdf_path, pages='all')
    dict_ = {}
    for t in tables:
        columns = t.columns
        values = t.values.tolist()[0]
        for i in range(len(columns)):
            dict_[columns[i]] = values[i]
    return dict_
