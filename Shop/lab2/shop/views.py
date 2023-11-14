from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import *
from .forms import ClientForm, ProductForm


class ClientList(TemplateView):

    def get(self, request):
        clients = Client.objects.all()
        context = {
            'clients': clients,
        }
        return render(request, "clients.html", context)

    def post(self, request):
        if 'search' in request.POST:
            query = request.POST['search']
            result_list = Client.objects.filter(name=query)
            print('------------------------', result_list)
            if result_list.count() != 0:
                lb = result_list[0].credit_limit - result_list[0].current_doubt
                lb = abs(lb)
                context = {
                    'lb': lb,
                    'result_list': result_list,
                    'query': query,
                }
            else:
                context = {
                    'empty': "Nothing founded. 404!",
                    'query': query,
                }

        return render(request, "clients.html", context)


class ProductList(TemplateView):
    def get(self, request):
        form = ProductForm()
        products = Product.objects.all()
        context = {
            'products': products,
            'form': form,
        }
        return render(request, "productCreate.html", context)

    def post(self, request):
        if request.method == 'POST':
            form = ProductForm(request.POST)
            if form.is_valid():
                form.save()
        context = {
            'form': form
        }
        return render(request, 'productCreate.html', context)


class Orderget(TemplateView):

    def get(self, request):
        clients = Client.objects.all()
        context = {
            'clients': clients,
        }
        return render(request, "orders.html", context)

    def post(self, request):
        if 'searchclient' in request.POST:
            query = request.POST['searchclient']
            result_list = Client.objects.filter(name=query)
            print('------------------------', result_list)
            if result_list.count() != 0:
                lb = result_list[0].credit_limit - result_list[0].current_doubt
                lb = abs(lb)
                context = {
                    'lb': lb,
                    'result_list': result_list,
                    'query': query,
                }
            else:
                context = {
                    'empty': "Nothing founded. 404!",
                    'query': query,
                }
            # render(request, "orders.html", context)

        if 'searchproduct' in request.POST:
            pr_query = request.POST['searchproduct']
            pr_result_list = Product.objects.filter(name=pr_query)
            if pr_result_list.count() != 0:
                context['product_result_list'] = pr_result_list
                context['product_query'] = pr_query
                # context += {
                # 'product_result_list': pr_result_list,
                # 'product_query': pr_query,
                # }
            else:
                context['product_empty'] = "Nothing founded. 404!"
                context['product_query'] = pr_query
                # context = {
                #     'product_empty': "Nothing founded. 404!",
                #     'product_query': pr_query,
                # }
        # if 'goodsnumber' in request.POST:
        pay_method = str(request.POST.get('paymethod', "None"))
        count = request.POST.get('goodsnumber')
        # if count == '':
        #     count = 0
        # else:
        #     count = int(count)
        # if 'paymethod' in request.POST:

        # print(request.POST['paymethod'], '---------------------------------')

        if len(result_list) != 0 and len(pr_result_list) != 0 and pay_method != "None" and count != '':
            if int(count) > 0:
                t = createOrder(
                    result_list[0], pr_result_list[0], int(count), pay_method)
                if t[0] == False:
                    context = {
                        'error': t[1]
                    }
                else:
                    context = {
                        'success': "Successful purchase. Thank you for nice deal!",
                        'result_list': result_list,
                        'product_result_list': pr_result_list,
                        'lb': lb,
                    }
            else:
                context = {
                    'error': "Count field is not correct! Input positive number."
                }
        else:
            context = {
                'error': "Some fields was filled not correct!"
            }
        return render(request, "orders.html", context)


def createOrder(client, product, count, pay_method):
    total = product.price * count
    gift = Product.objects.get(name="Gift Card")
    if pay_method == 'cash':
        if count > product.stock_balance:
            result = [False, 'Wanted count is more than stock balance']
        else:
            client.shopping_bag += total
            product.stock_balance -= count
            result = [True]

    elif pay_method == 'cashless':
        if count > product.stock_balance:
            result = [False, 'Wanted count is more than stock balance']
        elif total > client.current_account:
            result = [False, 'There are not enough funds in account']
        else:
            client.shopping_bag += total
            client.current_account -= total
            product.stock_balance -= count
            result = [True]
    elif pay_method == 'credit':
        if count > product.stock_balance:
            result = [False, 'Wanted count is more than stock balance']
        elif total > (client.credit_limit - client.current_doubt + client.current_account):
            result = [False, 'Credit limit exceeded']
        elif client.current_account >= total:
            result = [False, 'There are enough funds in the main account']
        else:
            client.shopping_bag += total
            total -= client.current_account
            client.current_account = 0
            client.current_doubt += total
            product.stock_balance -= count
            result = [True]

    elif pay_method == 'exchange':
        if count > product.stock_balance:
            result = [False, 'Wanted count is more than stock balance']
        product.stock_balance -= count
        gift.stock_balance += total
        result = [True]

    elif pay_method == 'mutoffset':  # mutual offset = взаимозачёт
        if total < client.current_doubt:
            product.stock_balance += count
            client.current_doubt -= total
            result = [True]
        else:
            product.stock_balance += count
            total -= client.current_doubt
            client.current_doubt = 0
            client.current_account += total
            result = [True]

    if result[0] == True:
        client.save()
        product.save()
        gift.save()

    return result
