from django.db import models

class wedding_card(models.Model):
    CHOICES = { 'premium' : 'PREMIUM' , 
                'general'  : 'GENERAL' ,
                'medium'  : 'MEDIUM' }
    
    choice = models.CharField(
        choices=CHOICES,
        default='premium',
        max_length=11
    )
    created_at = models.DateTimeField(auto_now_add=True)
    model_id = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    front_image = models.ImageField(
        upload_to='wedding_cards/',
        help_text='Upload front JPG image for the wedding card',
        null=True,
        blank=True
    )
    back_image = models.ImageField(
        upload_to='wedding_cards/',
        help_text='Upload back JPG image for the wedding card',
        null=True,
        blank=True
    )
    gsm = models.IntegerField(null=True)
    layer = models.IntegerField(null=True)
    folding = models.IntegerField(null= True)
