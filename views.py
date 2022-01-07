import datetime

from django.shortcuts import render, redirect
from django.views import View
from Warsztatapp.models import Sala, Reserve


class Index(View):
    def get(self, request):
        return render(request, 'Warsztatapp/index.html')


class AddRoom(View):
    def get(self, request):
        return render(request, 'Warsztatapp/Add_room.html')

    def post(self, request):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        availability = bool(request.POST.get('availability'))

        if not name:
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Nie podano nazwy sali'})

        if Sala.objects.filter(name=name).first():
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Sala o podanej nazwie istnieje już w bazie '
                                                                          'danych'})
        if int(capacity) <= 0:
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Pojemność sali musi być liczbą dodatnią'})

        new_room = Sala()
        new_room.name = name
        new_room.capacity = capacity
        new_room.availability = availability
        new_room.save()
        return redirect('room-list')


class RoomList(View):
    def get(self, request):
        sala = Sala.objects.all()
        for sale in sala:
            reservation_dates = [reservation.date for reservation in sale.reserve_set.all()]
            sale.reserved = datetime.date.today() in reservation_dates
        return render(request, 'Warsztatapp/Lista_Sal.html', {'sala': sala})


class DeleteRoom(View):
    def get(self, request, id):
        sala = Sala.objects.get(id=id)
        sala.delete()
        return redirect('room-list')

class ModifyRoom(View):
    def get(self, request, id):
        Sala.objects.get(id=id)
        return render(request, 'Warsztatapp/Modify_room.html')
    def post(self, request, id):
        name = request.POST.get('name')
        capacity = request.POST.get('capacity')
        availability = bool(request.POST.get('availability'))
        if not name:
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Nie podano nazwy sali'})

        if Sala.objects.filter(name=name).first():
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Sala o podanej nazwie istnieje już w bazie '
                                                                          'danych'})
        if int(capacity) <= 0:
            return render(request, 'Warsztatapp/Add_room.html', {'error': 'Pojemność sali musi być liczbą dodatnią'})

        sala = Sala.objects.get(id=id)
        sala.name = name
        sala.capacity = capacity
        sala.availability = availability
        sala.save()
        return redirect('room-list')

class ReserveViev(View):
    def get(self, request, id):
        sala = Sala.objects.get(id=id)
        reservations = sala.reserve_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, 'Warsztatapp/Reserve.html', {'sala': sala, 'reservations': reservations})

    def post(self, request, id):
        room = Sala.objects.get(id=id)
        comment = request.POST.get('comment')
        date = request.POST.get('date')

        if Reserve.objects.filter(id_room=room, date=date):
            return render(request, 'Warsztatapp/Reserve.html', {'error': 'Sala jest już zarezerwowana'})

        if date < str(datetime.date.today()):
            return render(request, 'Warsztatapp/Reserve.html', {'error': 'Podana data jest z przeszłości'})

        reserve = Reserve()
        reserve.id_room = room
        reserve.comment = comment
        reserve.date = date
        reserve.save()
        return redirect('room-list')

class DetailsRoom(View):
    def get(self, request, id):
        sala = Sala.objects.get(id=id)
        reservations = sala.reserve_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, 'Warsztatapp/Details.html', {'sala': sala, 'reservations': reservations})

# Create your views here.
