from django.db import models
from django.utils.text import slugify

class Language(models.TextChoices):
    HINDI = "hindi", "Hindi"
    ENGLISH = "english", "English"
    
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    cover_image= models.ImageField(upload_to='genre_cover_image/')
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
    cover_image= models.ImageField(upload_to='author_cover_image/')
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
  
class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=120, unique=True, blank=True)
    authors = models.ManyToManyField(Author, related_name='books')
    publisher = models.ForeignKey(Publisher, on_delete=models.PROTECT, related_name='books')
    categories = models.ManyToManyField(Category, related_name='books')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    cover_image= models.ImageField(upload_to='product_cover_image/')
    isbn = models.CharField("ISBN", max_length=13, unique=True, help_text="13-character ISBN number")
    page_count = models.PositiveIntegerField()
    language = models.CharField(max_length=50, choices=Language.choices, default=Language.HINDI)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        db_table = "books"

class BookImages(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='book_gallery/')
    alt_text = models.CharField(max_length=200, blank=True, help_text="Text for SEO and screen readers ")
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Image for {self.book.title}"
   
