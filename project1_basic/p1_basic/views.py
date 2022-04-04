from django.shortcuts import render
import random

# Create your views here.


def lotto(request):

    lotto_nums = [0,0,0,0,0,0]
    
    if request.GET.get('click') == "로또 번호 추출하기":
        for i in range(6):
            lotto_nums[i] = random.randint(1,45)
            

    
    return render(request, 'lotto.html', {'lotto_nums':lotto_nums})