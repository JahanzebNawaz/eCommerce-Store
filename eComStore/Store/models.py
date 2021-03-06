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
    product_desc = models.TextField(
        max_length=500, verbose_name='Product Description')
    pub_date = models.DateTimeField(auto_now_add=True)
    product_image = models.ImageField(upload_to='products')

    class Meta:
        verbose_name_plural = 'Product'

    def __str__(self):
        return self.product_name

    def product_desc_sum(self):
        return self.product_desc[:40]


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, default="")

    class Meta:
        verbose_name = 'Orders'

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
