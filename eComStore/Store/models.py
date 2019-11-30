from django.db import models

# Create your models here.


class Product(models.Model):
        product_id = models.AutoField
        product_name = models.CharField(max_length=50, verbose_name='Product Name')
        product_desc = models.CharField(max_length = 500, verbose_name='Product Description')
        pub_date = models.DateTimeField(auto_now_add=True)

        class Meta:
                verbose_name_plural = 'Product'
        
        def __str__(self):
                return self.product_name