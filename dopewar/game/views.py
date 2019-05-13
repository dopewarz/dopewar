import json

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import player, drug, country, house
from django.db.models import Sum


def index(request):
    return HttpResponse('Game on here is the link --> <a href="/game/game2/">Click</a>')

# Create your views here.
def game2(request):
    active_player = player.objects.get(id=2)
    coke = int(drug.objects.get(country=active_player.country, name='COKE').price)
    all_drugs = drug.objects.all()
    reigon_drugs = drug.objects.filter(country=active_player.country)
    inventory_space = str(house.objects.filter(owned="True").aggregate(Sum('inventory'))).replace("{'inventory__sum':","").replace("}","")
    realestate = house.objects.filter(country=active_player.country)
    action = request.POST.get('action')
    if not action:
        return render(request, 'game/game2.html', {'coke': coke, 'active_player': active_player} )
    elif action == "newgame":
        state = {"name": request.POST['name'], "balance": active_player.cash,
                 "inventory": {}, "house": active_player.house, "health":active_player.health,
                 "country": str(active_player.country), "inventory_space": inventory_space}
        return render(request, 'game/game2.html', {'action': 'home', 'coke': coke,'all_drugs': all_drugs,'reigon_drugs': reigon_drugs, 'state': state, 'state_str': json.dumps(state), 'active_player':active_player, "realestate":realestate} )
    elif action == "change_unit":
        state = json.loads(request.POST['state'])
        units = int(request.POST['amount'])
        total_price = units * coke
        if request.POST['submit'] == 'Add unit':
            if total_price > state['balance']:
                raise RuntimeError("Insufficient balance.")
            state['inventory']['coke'] = state['inventory'].get('coke', 0) + units
        elif request.POST['submit'] == 'Subtract unit':
            units_in_inventory = state['inventory'].get('coke', 0)
            if units > units_in_inventory:
                raise RuntimeError("Insufficient units in inventory.")
            state['inventory']['coke'] -= units
            total_price *= -1
        state['balance'] -= total_price
        return render(request, 'game/game2.html', {'action': 'home', 'coke': coke, 'state': state, 'state_str': json.dumps(state), 'active_player':active_player})
    elif action == "change_balance":
        sign = 1
        if request.POST['submit'] == 'Subtract money':
            sign = -1
        state = json.loads(request.POST['state'])
        state['balance'] += sign * int(request.POST['amount'])
        return render(request, 'game/game2.html', {'action': 'home', 'coke': coke, 'state': state, 'state_str': json.dumps(state), 'active_player':active_player})
    else:
        raise RuntimeError("Weird state.")


