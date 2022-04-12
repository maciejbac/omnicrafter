from django.shortcuts import render
from .forms import CustomerForm
from . import functions as func
from django.http import HttpResponse


def index(request):
	form = CustomerForm()
	if request.method == 'POST':
		form = CustomerForm(request.POST)
		if form.is_valid():

			text = request.POST.get('item_id')

			if int(text) > 36700:
				return HttpResponse('Item ID out of range.')

			text = str(text)
			price = func.getPrice(text)
			name = func.getName(text)
			response = 'The cheapest ' + name + ' costs: ' + str(price)
			return HttpResponse(response)

	context = {'form':form}
	return render(request, 'app/index.html', context)