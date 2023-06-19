from django.core.paginator import Paginator

def paginate_results(request, queryset, items_per_page):
    
    paginator = Paginator(queryset, items_per_page)
    page_number = request.GET.get('page')
    paginated_results = paginator.get_page(page_number)

    return paginated_results
