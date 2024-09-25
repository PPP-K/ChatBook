from django.db import models
from PIL import Image
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    
    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        if self.image:
            img = Image.open(self.image.path)

            if img.height > 30 or img.width > 30:
                output_size = (30, 30)
                img.thumbnail(output_size)
                img.save(self.image.path)
                
    


# Create your models here.
