from django import forms
from .models import Ticket, Comment


class TicketForm(forms.ModelForm):

    class Meta:
        model = Ticket

        fields = [
            'title',
            'description',
            'priority'
        ]


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = [
            'text'
        ]

        widgets = {
            'text': forms.Textarea(
                attrs={
                    'rows': 4,
                    'placeholder': 'Write a comment...'
                }
            )
        }