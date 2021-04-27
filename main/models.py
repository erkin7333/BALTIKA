from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    post_added = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True, verbose_name='Saytga qoshilgan')
    image = models.ImageField(default='default1.jpg', upload_to='main/post_pics', blank=True,
                             null=True,
                             width_field='img_w',
                             height_field='img_h',
)
    img_w = models.IntegerField(default=0)
    img_h = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Yangilik'
    verbose_name = 'Yangiliklar'

    def save(self, *args, **kwargs):
        # print(self.photo.closed)
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')
            # tmp.seek(0)

            self.image = File(tmp, 'image.png')
        return super().save(*args, **kwargs)
