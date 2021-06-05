from django.shortcuts import render
from django.http import HttpResponse

calculo =  [
            {
                'Monto':'12000',
                'Tasa':'4',
                'Plazo':'12',
                'Cuota':'555555',
                'Total':'555555',
            },

]

def index(request):
    if request.method == 'POST':

        monto = int(request.POST.get('monto'))
        tasa = int(request.POST.get('tasa'))
        plazo = int(request.POST.get('plazo'))

        #formula cuota prest
        r = tasa / 100 / 12
        n = plazo * 12

        cuota = (monto*r)/(1-(1+r)** -n)
        total = cuota * n

        calculo.append({
            'monto':monto,
            'tasa':tasa,
            'plazo':plazo,
            'cuota':cuota,
            'total':total,
        })

        ctx = {
            'calculo': calculo
        }

        return render(request, "cuota/index.html", ctx)
    else:
        ctx = {
            'calculo': calculo
        }
        return render(request, "cuota/index.html", ctx)

# Create your views here.
