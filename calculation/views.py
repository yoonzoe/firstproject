from django.shortcuts import render


def calculate (request):
    return render(request, "calculate.html",{'calculate' : calculate})

def result (request):
    first = request.GET['first']
    second = request.GET['second']
    first = int(first)
    second = int(second)
    cal = request.GET['calculate']
    
    if cal == 'plus':
        result = first + second
    elif cal == 'minus':
        result = first - second
    elif cal == 'multiple':
        result = first * second
    elif cal == 'divide':
        if second != 0:
            result = first / second
        else:
            result = 'division by zero'

    return render(request, "result.html", {'result' : result})
