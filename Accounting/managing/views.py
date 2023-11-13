from django.shortcuts import render
from django.views.generic import TemplateView
from .models import *
from .forms import ClientCodesForm

class CreatingForms(TemplateView):
	def get(self, request):
		codes = ClientCodes.objects.all()
		context = {
			'codes': codes,
		}
		return render(request, "index.html", context)

	def post(self, request):
		if request.method == 'POST':
			form = ClientCodesForm(request.POST)
			codes = ClientCodes.objects.all()
			iac = request.POST.get('IAC')
			os = request.POST.get('OS')
			print(os)
			if form.is_valid():
				form.save()
				dc = ClientCodes.objects.filter(IAC=iac)
				dcode = dc[0]
				if os == 'windows':
					dcode.DepCode = '100' + str(iac)
				elif os == 'linux':
					dcode.DepCode = '200' + str(iac)
				elif os == 'macos':
					dcode.DepCode = '300' + str(iac)
				elif os == 'debian':
					dcode.DepCode = '400' + str(iac)
				else:
					dcode.DepCode = '500' + str(iac)

				dcode.save()
		context = {
			'codes': codes,
		}
		return render(request, 'index.html', context)
