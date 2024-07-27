from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .models import MissingPerson
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse
from home.models import SosUser

# Create your views here.
class LostAndFoundView(View):
    def get(self, request):
        missing_person_list = MissingPerson.objects.all()
        user = SosUser.objects.get(user=request.user)
        context = {
            'missing_person_list': missing_person_list,
            'role': user.role
        }
        return render(request, 'lost_and_found/lost_and_found.html', context)

    def post(self, request):
        context = {}
        if len(request.POST['date_of_birth'])==0 and len(request.POST['name'])==0:
            return HttpResponseRedirect(reverse('lost_and_found'))
        elif len(request.POST['date_of_birth'])==0 and len(request.POST['name'])!=0:
            missing_person_list = MissingPerson.objects.filter(name__icontains=request.POST['name'].lower())
            context = {
                'missing_person_list': missing_person_list
            }
        elif len(request.POST['date_of_birth'])!=0 and len(request.POST['name'])==0:
            missing_person_list = MissingPerson.objects.filter(date_of_birth=request.POST['date_of_birth'])
            context = {
                'missing_person_list': missing_person_list
            }
        else:
            missing_person_list = MissingPerson.objects.filter(date_of_birth=request.POST['date_of_birth'] ,name__icontains=request.POST['name'].lower())
            context = {
                'missing_person_list': missing_person_list
            }
        return render(request, 'lost_and_found/lost_and_found.html', context)

class ReportMissingView(View):
    def get(self, request):
        return render(request, 'lost_and_found/report_missing.html')

    def post(self, request):
        missing_person = MissingPerson()
        missing_person.name = request.POST['name'].lower()
        missing_person.date_of_birth = request.POST['date_of_birth']
        missing_person.date_missing = request.POST['date_missing']
        missing_person.image = request.FILES['image']
        if len(request.POST['birth_mark'])==0:
            missing_person.birth_mark = "None"
        else:
            missing_person.birth_mark = request.POST['birth_mark']
        missing_person.place_seen_last_time = request.POST['place_seen_last_time']
        missing_person.save()
        return HttpResponseRedirect(reverse('lost_and_found'))

class MissingPersonFound(View):
    def post(self, request):
        person_found = MissingPerson.objects.get(id=request.POST['person_id'])
        person_found.delete()
        return HttpResponseRedirect(reverse('lost_and_found'))