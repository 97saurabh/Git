from django.shortcuts import render
from .forms import *
# Create your views here.

from formtools.wizard.views import SessionWizardView

class ContactWizard(SessionWizardView):
    def done(self, form_list, **kwargs):
        return render(self.request, 'index.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })


def live(request):
    form=FormName()
    data={}
    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():
            print("VALIDATION A")
            print("NAME:",form.cleaned_data['name'])
            data={"Name":form.cleaned_data['name']}



    return render(request,"index.html",{"forms":form,"data":data})
