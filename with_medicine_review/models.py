from django.db import models

# Create your models here.
class Review_board(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
class Review_Comment(models.Model):
    review_board_id = models.ForeignKey(Review_board, on_delete=models.CASCADE, related_name='comment')
    b_text = models.CharField(max_length=30)
    
    def __str__(self):
        return self.b_text