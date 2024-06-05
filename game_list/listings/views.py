from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Game
from listings.models import Plateform
from listings.forms import GameForm
from listings.forms import PlateformForm
from django.shortcuts import redirect

def about(request):
    return render(request,'listings/about.html')

def games(request):
    games=Game.objects.all()
    gamel=[]
    for game in games:
        platelist = game.plateforme.all()
        p = []
        for plateform in platelist:
            p.append([plateform.name,plateform.id])
        p.sort(key=lambda x: x[0])
        gamel.append([game.title,p ,game.id])
    return render(request,'listings/games.html', {'gamel' : gamel})

def game_detail(request,game_id):
    game=Game.objects.get(id=game_id)
    plateformes=game.plateforme.all()
    return render(request, 'listings/game_detail.html', {'game' : game,'plateformes' : plateformes})

def game_create(request):
    if request.method == 'POST':
        form=GameForm(request.POST)
        if form.is_valid():
            game=form.save()
            return redirect('game_detail',game.id)
    else:
        form=GameForm()
    return render(request, 'listings/game_create.html', {'form' : form})

def game_edit(request,game_id):
    game=Game.objects.get(id=game_id)
    
    if request.method == 'POST':
        form=GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_detail', game.id)
    else:
        form=GameForm(instance=game)
    return render(request, 'listings/game_edit.html', {'form' : form})

def game_delete(request,game_id):
    game=Game.objects.get(id=game_id)
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'listings/game_delete.html', {'game' : game})

def plateformes(request):
    plateformes=Plateform.objects.all()
    return render(request,'listings/plateformes.html', {'plateformes': plateformes})

def plateforme_detail(request, plateforme_id):
    plateforme=Plateform.objects.get(id=plateforme_id)
    games=Game.objects.all()
    gamep=[]
    for game in games:
        plateformes=game.plateforme.all()
        for p in plateformes:
            if p.name == plateforme.name:
                gamep.append(game)
    return render(request, 'listings/plateforme_detail.html', {'plateforme' : plateforme, 'gamep' : gamep})

def plateforme_add(request):
    if request.method == 'POST':
        form = PlateformForm(request.POST)
        if form.is_valid():
            plateforme=form.save()
            return redirect('plateforme_detail', plateforme.id)
    else:
        form=PlateformForm()
    return render(request,'listings/plateforme_add.html',{'form' : form})

def plateforme_delete(request,plateforme_id):
    plateforme=Plateform.objects.get(id=plateforme_id)
    if request.method == 'POST':
        plateforme.delete()
        return redirect('plateformes')
    return render(request, 'listings/plateforme_delete.html', {'plateforme' : plateforme})

def plateforme_edit(request, plateforme_id):
    plateforme=Plateform.objects.get(id=plateforme_id)
    if request.method == 'POST':
        form=PlateformForm(request.POST, instance=plateforme)
        if form.is_valid():
            form.save()
            return redirect('plateforme_detail', plateforme.id)
    else:
        form=PlateformForm(instance=plateforme)
    return render(request, 'listings/plateforme_edit.html', {'form' : form})
