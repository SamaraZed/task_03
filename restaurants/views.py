from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list" : [{"restaurant_name":"Burgerizz", "food_type":"Burgers and Wings"}
    ,{"restaurant_name":"Hamada", "food_type":"Falafel"}
    ,{"restaurant_name":"Shawermati", "food_type":"Shawarma"}]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    "my_object":{"restaurant_name":"Falafelrest","food_type":"Mansaf"}
    }
    return render(request, 'detail.html', context)
