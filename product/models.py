from django.db import models 
from django.utils.text import slugify
from django.core.exceptions import ValidationError

class Language(models.TextChoices):
    HINDI = "HI", "Hindi"
    ENGLISH = "EN", "English"
    URDU = "UR", "Urdu"

class Stock(models.TextChoices):
    IN_STOCK = "in_stock", "In Stock"
    OUT_OF_STOCK = "out_of_stock", "Out of Stock"
    PRE_ORDER = "pre_order", "Pre-order"
    COMING_SOON = "coming_soon", "Coming Soon"

    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cover_image= models.ImageField(upload_to='category_image/')
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "book_categories"
        verbose_name_plural = "Categories"
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    cover_image= models.ImageField(upload_to='author_profile/')
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        db_table = "book_authors"
    
class Publisher(models.Model):
    name = models.CharField(max_length=50)
    publication_date = models.DateField()
    def __str__(self):
        return self.name
    class Meta:
        db_table = "book_publishers"

class ISBNConfig(models.Model):
    prefix = models.CharField(max_length=3, default="978")
    digit_length = models.PositiveSmallIntegerField(default=10)
    current_sequence = models.PositiveBigIntegerField(default=0)
    class Meta:
        db_table = "isbn_config"
    def save(self, *args, **kwargs):
        if not self.pk and ISBNConfig.objects.exists():
            raise ValueError("Only one ISBNConfig instance allowed")
        super().save(*args, **kwargs)
    @classmethod
    def get_next_isbn(cls):
        config = cls.objects.first()
        if not config:
            config = cls.objects.create()
        config.current_sequence += 1
        config.save()
        sequence = str(config.current_sequence).zfill(config.digit_length)
        return f"{config.prefix}{sequence}"
  
class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.PositiveIntegerField(default=0) 
    stock= models.CharField(max_length=50, choices=Stock.choices, default=Stock.IN_STOCK)  # will add business logic so now manually select stock 
    cover_image= models.ImageField(upload_to='books_cover_image/')
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50, choices=Language.choices, default=Language.HINDI)
    description = models.TextField()
    publication_date = models.DateField(auto_now_add=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
   
    # for calculate discount price
    def calculate_discount(self):
        if self.discount_price > self.price:
            raise ValidationError(
                "Discount price cannot be greater than the original price."
            )

        if self.price > 0:
            self.discount_percentage = round(
                ((self.price - self.discount_price) / self.price) * 100
            )
        else:
            self.discount_percentage = 0

    # generarate auto slug as per title 
    def generate_slug(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

    # generate unique ISBN number
    def generate_isbn(self, *args, **kwargs):
        if not self.isbn:
            self.isbn = ISBNConfig.get_next_isbn()

    def save(self, *args, **kwargs):
        self.calculate_discount()
        self.generate_slug()
        self.generate_isbn()

        super().save(*args, **kwargs)
    


    def __str__(self):
        return self.title
    class Meta:
        db_table = "books"

class BookImages(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='book_gallery/')
    alt_text = models.CharField(max_length=200, blank=True, help_text="Text for SEO and screen readers ")
    created_at = models.DateTimeField(auto_now_add=True )
    def __str__(self):
        return f"Image for {self.book.title}"
   

