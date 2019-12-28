from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from django.views import View
from project_app.form import NameForm, CatagoryiesForm
from project_app.models import Person, Catagoryies
from django.http import HttpResponseRedirect


class URLListiews(View):


	def get(self, request, *args, **kwargs): 
		return render(request, 'index.html')

	def post(self, request, *args, **kwargs): 
		form = NameForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			Person.objects.create(**data)
		return HttpResponseRedirect('nextfilenex') 


class NextListiews(View):
	def get(self, request, *args, **kwargs):
		context ={'data':Person.objects.all()} 
		return render(request, 'stdform.html',context)


	def post(self, request, *args, **kwargs):
		person_id = request.POST.get('person_id')
		person = Person.objects.get(id=person_id)

		form = CatagoryiesForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			data['person'] = person

			Catagoryies.objects.create(**data)


		return HttpResponseRedirect('/')
 