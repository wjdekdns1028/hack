from django.db import models

# Create your models here.
class Free_board(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title

class Free_Comment(models.Model):
    free_board_id = models.ForeignKey(Free_board, on_delete=models.CASCADE, related_name='comment')
    b_text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.b_text