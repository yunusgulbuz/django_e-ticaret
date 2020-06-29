from django.db import models
from django.utils.safestring import mark_safe
STATUS = (
    ('True', 'Evet'),
    ('False', 'Hayır'),
)


class Category(models.Model):
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField()
    amount = models.IntegerField()
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        imageList = dict()
        imageList['images'] = ""
        for image in Images.objects.filter(product=self.pk):
            if imageList['images'] != "":
                imageList['images'] = mark_safe(f"{imageList['images']}<img src='{image.image.url}' height='40'/>"
                                                f"&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;")
            else:
                imageList['images'] = mark_safe(f"<img src='{image.image.url}' height='40'/>"
                                                f"&nbsp; &nbsp; &nbsp; &nbsp; &nbsp;")
        return imageList['images']


class Images(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=150, blank=True)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" height="50"/>')
        else:
            return ""
