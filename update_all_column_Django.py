from .models import Answer
# Import your model first

Answer.objects.all().order_by('text').update(text='updated')

#Update the whole column in Django model