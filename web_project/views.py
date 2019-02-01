from django.shortcuts import render, redirect


def welcome(request):
    if request.user.is_authenticated:
        return redirect( 'player-home')
    else:
        return render(request, 'tictactoe/welcome.html')