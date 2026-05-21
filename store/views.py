from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import (Banner, Ingredient, Category, Product,
                     WhyPoint, Customer, FlashSaleItem, NavLink,
                     OfferBanner, BuyOneGetOne, ExclusiveKit)


def get_common_context():
    return {
        'nav_links': NavLink.objects.filter(is_active=True).order_by('order'),
        'categories': Category.objects.all().order_by('order'),
    }


def home(request):
    context = get_common_context()
    context.update({
        'banners': Banner.objects.filter(is_active=True).order_by('order'),
        'ingredients': Ingredient.objects.all().order_by('order'),
        'products': Product.objects.filter(is_active=True)[:6],  
        'why_points': WhyPoint.objects.all().order_by('order'),
        'customers': Customer.objects.filter(is_active=True),
        'flash_items': FlashSaleItem.objects.filter(is_active=True),
    })
    return render(request, 'store/home.html', context)

def shop(request):
    context = get_common_context()
    products = Product.objects.filter(is_active=True)

    # Filter by category
    category_id = request.GET.get('category')
    selected_category = None
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)

    # Filter by brand
    brand = request.GET.get('brand')
    if brand:
        products = products.filter(brand__icontains=brand)

    # Filter by price
    price_range = request.GET.get('price')
    if price_range == '0-499':
        products = products.filter(price__lte=499)
    elif price_range == '500-799':
        products = products.filter(price__gte=500, price__lte=799)
    elif price_range == '800-1099':
        products = products.filter(price__gte=800, price__lte=1099)
    elif price_range == '1100+':
        products = products.filter(price__gte=1100)

    # Sort
    sort = request.GET.get('sort', 'recommended')
    if sort == 'top_rated':
        products = products.order_by('-rating')
    elif sort == 'price_low':
        products = products.order_by('price')
    elif sort == 'price_high':
        products = products.order_by('-price')
    elif sort == 'offers':
        products = products.filter(badge__in=['bestseller', 'hotpick'])

    # Get all brands for filter
    all_brands = Product.objects.filter(
        is_active=True
    ).values_list('brand', flat=True).distinct()

    context.update({
        'products': products,
        'selected_category': selected_category,
        'all_brands': all_brands,
        'current_sort': sort,
        'current_category': category_id,
        'current_brand': brand,
        'current_price': price_range,
    })
    return render(request, 'store/shop.html', context)


def product_detail(request, pk):
    context = get_common_context()
    product = get_object_or_404(Product, pk=pk)
    related_products = Product.objects.filter(
        category=product.category,
        is_active=True
    ).exclude(pk=pk)[:4]
    shades = product.shades.all()

    context.update({
        'product': product,
        'related_products': related_products,
        'shades': shades,
    })
    return render(request, 'store/product_detail.html', context)


def search(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        is_active=True,
        name__icontains=query
    ).values('id', 'name', 'price', 'image')[:8]

    results = []
    for p in products:
        results.append({
            'id': p['id'],
            'name': p['name'],
            'price': str(p['price']),
            'image': '/media/' + p['image'] if p['image'] else '',
        })
    return JsonResponse({'results': results})

def offers(request):
    context = get_common_context()
    context.update({
        'offer_banners': OfferBanner.objects.filter(is_active=True).order_by('order'),
        'bogo_items': BuyOneGetOne.objects.filter(is_active=True),
        'exclusive_kits': ExclusiveKit.objects.filter(is_active=True),
    })
    return render(request, 'store/offers.html', context)

def cart(request):
    context = get_common_context()
    return render(request, 'store/cart.html', context)
def checkout(request):
    context = get_common_context()
    return render(request, 'store/checkout.html', context)

def order_success(request):
    context = get_common_context()
    return render(request, 'store/order_success.html', context)

def track_order(request):
    context = get_common_context()
    return render(request, 'store/track_order.html', context)
def about(request):
    context = get_common_context()
    return render(request, 'store/about.html', context)
def contact(request):
    context = get_common_context()
    return render(request, 'store/contact.html', context)