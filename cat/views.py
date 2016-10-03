from django.shortcuts import render


subjects_list = [
    'USO',
    'SD',
    'PC'
]

def subjects(request):
    return render(request, 'cat/subjects.html',
                  {'subjects_list': subjects_list})
