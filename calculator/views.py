from django.shortcuts import render, HttpResponse

def calc_view(request):
    result = None
    if request.method == 'POST':
        num1 = int(request.POST['num1'])
        num2 = int(request.POST['num2'])
        operation = request.POST['operation']

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return HttpResponse("Cannot divide by zero!")
            result = num1 / num2

    return render(request, 'index.html', {'result':result})