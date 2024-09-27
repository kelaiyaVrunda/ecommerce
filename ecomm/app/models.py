from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('TX','TEXTILE'),
    ('PT','PAINTING'),
    ('PC','POTTERY & CERAMICS'),
    ('SC','SCULPTURES & CARVINGS'),
    ('HL','HANDLOOMS'),
    ('MC','METALCRAFTS'),
    ('WV','WEAVING'),
)
class Product(models.Model):
    title=models.CharField(max_length=100)
    selling_price=models.FloatField()
    description=models.TextField()
    composition=models.TimeField(default='')
    prodapp=models.TextField(default='')
    category=models.CharField(choices=CATEGORY_CHOICES,max_length=2)
    product_image=models.ImageField(upload_to='product')
    def __str__(self):
      return self.title
