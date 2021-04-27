from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
from django.core.files import File

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='defaulti.jpg', upload_to='profile_pics', blank=True,
                             null=True,
                             width_field='img_w',
                             height_field='img_h',
)
    
    img_w = models.IntegerField(default=0)
    img_h = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} Profile'



    def save(self, *args, **kwargs):
            # print(self.photo.closed)
        if not self.image.closed:
            img = Image.open(self.image)
            img.thumbnail((500, 500), Image.ANTIALIAS)

            tmp = BytesIO()
            img.save(tmp, 'PNG')
            print(self.image)
                # tmp.seek(0)

            self.image = File(tmp, 'image.png')
        return super().save(*args, **kwargs)
