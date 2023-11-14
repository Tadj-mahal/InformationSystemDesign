from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.http import HttpResponse

from statistics import mean
import json

data = []
temp = 0


def right_point(temp, y_curr):
    if ((y_curr > 0.6 * temp) and (y_curr < 1.4 * temp)):
        result = [True, y_curr]
    else:
        result = [False, "Current y is more or less previous value more than 40%"]
    return result


class PointAdd(TemplateView):

    def __init__(self, *args, **kwargs):
        super(PointAdd, self).__init__(*args, **kwargs)

    def get(self, request):
        modified_data = json.dumps(data)
        context = {
            'lendata': len(data),
            'data': data,
            'values': modified_data,
        }
        return render(request, "charts.html", context)

    def post(self, request):
        global temp
        y = request.POST.get('add_point')
        try:
            y = float(y)

            if len(data) < 10:
                if len(data) < 1:
                    temp = y
                    data.append([len(data) + 1, y])
                    print(data)
                    modified_data = json.dumps(data)
                    context = {
                        'lendata': len(data),
                        'data': data,
                        'values': modified_data,
                        'success': "Successful! Value was added.",
                    }
                else:
                    res = right_point(temp, y)
                    if res[0]:
                        data.append([len(data) + 1, y])
                        temp = y
                        print(data)
                        modified_data = json.dumps(data)
                        context = {
                            'lendata': len(data),
                            'data': data,
                            'values': modified_data,
                            'success': "Successful! Value was added.",
                        }
                    else:
                        context = {'error': res[1]}
            else:
                context = {
                    'error': "More values than need!",
                }
        except ValueError:
            context = {'error': "value is not number!"}

        return render(request, "charts.html", context)


def cleardata(request):
    if request.method == "POST":
        data.clear()
        return redirect('/')
    context = {
        'success': "Graphic was reset successful!",
        'values': json.dumps(data),
    }
    return render(request, "reset.html", context)


def gistogram(request):
    if request.method == "POST":
        lower_bound = request.POST.get('lower_b')
        higher_bound = request.POST.get('higher_b')
        divval = request.POST.get('divval')
        inter = interval(lower_bound, higher_bound, divval)
        if(inter[0]):
            print(inter[1])
            interjson = json.dumps(inter[1])
            print(interjson)
            context = {
                'values1': interjson,
                'avgval': inter[2],
            }
        else:
            context = {'error': inter[1]}
        return render(request, "gisto.html", context)
    return render(request, "gisto.html")


def interval(a, b, c):
    try:
        a = float(a)
        b = float(b)
        с = float(c)
        if ((a > b) or (a < 0) or (b < 0) or (float(c) <= 0)):
            result = [False, "Input correct interval"]
        else:
            intrvldata = [["", '']]
            k = 0
            sumfavg = 0  # sum for avg
            for i in range(len(data)):
                if (data[i][1] % int(c) == 0 and data[i][1] >= a and data[i][1] <= b):
                    intrvldata.append(data[i])
                    k += 1
                    sumfavg += data[i][1]
            if k != 0:
                intravg = sumfavg / k
            else:
                intravg = 0
            result = [True, intrvldata, intravg]
    except ValueError:
        result = [False, "Input correct values"]
    return result

# доработать очистку и вид в гистограмму
