from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    create_date = models.DateField(auto_now=True)
    image = models.ImageField(upload_to="images/")
    short_description = models.CharField(max_length=300, blank=True)
    main_description = models.TextField()
    
    class Meta:
        db_table = 'Article'
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return f"{self.author} | {self.short_description[:20]}..."
    
    def save(self, *args, **kwargs):
        self.short_description = self.main_description[:300]
        return super(Article, self).save(*args, **kwargs)

