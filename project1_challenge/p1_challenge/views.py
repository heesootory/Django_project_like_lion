from django.shortcuts import render
import random

# Create your views here.

#입력창
def lotto2(request):

    num = request.GET.get('num')

    return render(request, 'lotto.html')


#결과창
def lotto2_result(request):

    num = int(request.GET.get('num'))
    list = [[0]*6 for _ in range(num)]
    
    for i in range(num):
        for j in range(6):
            list[i][j] = random.randint(1,45)
    
    return render(request, 'result.html', {'num':num, 'list':list}) 
