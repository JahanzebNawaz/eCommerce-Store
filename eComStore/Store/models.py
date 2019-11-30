from django.db import models

# Create your models here.


class Product(models.Model):
        ''' 
                Products Model
        '''
        product_id = models.AutoField
        product_name = models.CharField(max_length=50, verbose_name='Product Name')
        product_category = models.CharField(max_length=50, default="")
        product_subcategory = models.CharField(max_length=50)
        product_price = models.IntegerField()
        product_desc = models.TextField(max_length = 500, verbose_name='Product Description')
        pub_date = models.DateTimeField(auto_now_add=True)
        product_image = models.ImageField(upload_to='products')

        class Meta:
                verbose_name_plural = 'Product'
        
        def __str__(self):
                return self.product_name
        
        def product_desc_sum(self):
                return self.product_desc[:40]
