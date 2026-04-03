from django.db import models

class Conversation(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Message in {self.conversation.title} on {self.created_at}'
        # Models for storing conversations and messages
# Conversation -> stores chat title and creation time
# Message -> stores each message linked to a conversation
# Fixed __str__ method to properly display message info
