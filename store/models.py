from django.db import models

class Banner(models.Model):
    POSITION_CHOICES = [
        ('left', 'Left'),
        ('right', 'Right'),
    ]
    image = models.ImageField(upload_to='banners/', null=True, blank=True)
    button_text = models.CharField(max_length=50, default='Shop Now')
    button_position = models.CharField(max_length=10, choices=POSITION_CHOICES, default='left')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Banner {self.order}"

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='ingredients/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    front_image = models.ImageField(upload_to='categories/')
    back_image = models.ImageField(upload_to='categories/')
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class Product(models.Model):
    BADGE_CHOICES = [
        ('', 'None'),
        ('bestseller', 'Best Seller'),
        ('new', 'New'),
        ('trending', 'Trending'),
        ('hotpick', 'Hot Pick'),
        ('skinloving', 'Skin Loving'),
    ]
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    reviews_count = models.IntegerField(default=0)
    badge = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WhyPoint(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Customer(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    review = models.TextField()
    avatar = models.ImageField(upload_to='customers/')
    stars = models.IntegerField(default=5)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FlashSaleItem(models.Model):
    product_name = models.CharField(max_length=200)
    discount = models.CharField(max_length=50)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product_name

class NavLink(models.Model):
    label = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.label
    

class Product(models.Model):
    BADGE_CHOICES = [
        ('', 'None'),
        ('bestseller', 'Best Seller'),
        ('new', 'New'),
        ('trending', 'Trending'),
        ('hotpick', 'Hot Pick'),
        ('skinloving', 'Skin Loving'),
    ]
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    how_to_use = models.TextField(blank=True)
    benefits = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=1, default=4.5)
    reviews_count = models.IntegerField(default=0)
    badge = models.CharField(max_length=20, choices=BADGE_CHOICES, blank=True)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProductShade(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='shades')
    color_code = models.CharField(max_length=20)
    shade_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.product.name} - {self.shade_name}"
    
class OfferBanner(models.Model):
    image = models.ImageField(upload_to='offer_banners/')
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f"Offer Banner {self.order}"


class BuyOneGetOne(models.Model):
    name = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    description = models.CharField(max_length=200, blank=True)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='bogo/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ExclusiveKit(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    offer_price = models.DecimalField(max_digits=10, decimal_places=2)
    save_percent = models.IntegerField(default=0)
    image = models.ImageField(upload_to='exclusive/', null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name