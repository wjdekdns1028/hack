from django import forms
from .models import Review_board, Review_Comment

class Review_board_Form(forms.ModelForm):
    class Meta:
        model = Review_board
        fields = ['title', 'body']
        
class Review_board_CommentForm(forms.ModelForm):
    class Meta:
        model = Review_Comment
        fields = ['b_text']