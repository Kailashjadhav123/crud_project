from django.db import models
from django.contrib.auth.models import AbstractUser,User
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

# Create your models here.

class Student(models.Model):
    firstname = models.CharField(max_length=100,default=" ")
    lastname = models.CharField(max_length=100,default="")
    age = models.IntegerField()
    city = models.CharField(max_length=100)
    mobile = models.IntegerField()
    title = models.CharField(max_length=100,default="Title1")
    code = models.CharField(max_length=100,default="Code1")
    linenos = models.CharField(max_length=100,default="1")
    language = models.CharField(max_length=100,default="python")
    style = models.CharField(max_length=100,default="friendly")

    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    
    def save(self, *args, **kwargs):
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super().save(*args, **kwargs)