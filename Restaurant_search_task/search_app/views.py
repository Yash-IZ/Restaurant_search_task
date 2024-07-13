from django.shortcuts import render
from .models import Restaurant
from django.db.models import Q

def home_view(request):
    return render(request, 'search_app/home.html')

def search_view(request):
    query = request.GET.get('q', '')  # Get search query from request.GET with default empty string
    results = []

    if query:
        # Define Q objects for each field you want to search
        queries = [Q(**{f'{field}__icontains': query}) for field in ['name', 'location', 'items', 'lat_long', 'full_details']]
        
        # Combine all Q objects with OR operator using functools.reduce
        import functools
        combined_query = functools.reduce(lambda a, b: a | b, queries)
        
        # Fetch results and count them
        results = Restaurant.objects.filter(combined_query)
        number_of_results = results.count()
    else:
        number_of_results = 0
    
    context = {
        'query': query,
        'results': results,
        'number_of_results': number_of_results,  # Pass number of results to template
    }
    return render(request, 'search_app/search_result.html', context)
