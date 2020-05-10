import os
from django.shortcuts import render
from django.conf import settings
from commands import Commands


def home(request):
    context = dict()
    context['menus'] = settings.APP_MENUS
    return render(request, 'home.html', context)


def exec_command(request, menu, command):
    context = dict()
    context['menu'] = menu
    context['command'] = command
    context['tree'] = list()
    context['return'] = Commands.execute(command)
    for (dirpath, dirnames, filenames) in os.walk(os.path.join(settings.BASE_DIR, 'templates', 'menu')):
        context['tree'] += [os.path.join(dirpath, file) for file in filenames]
    target = 'menu/' + menu + '/' + command + '.html'
    if os.path.exists(os.path.join(settings.BASE_DIR, 'templates', target)):
        return render(request, target, context)
    else:
        return render(request, 'generic/404.html', context)
