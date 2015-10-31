from django.forms import ModelForm
from students.models import Book, Link, Question_Paper
from django.forms.forms import NON_FIELD_ERRORS



class QuestionPaperForm(ModelForm):
    class Meta:
        model = Question_Paper
        exclude = ['pub_date']
        #fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        
    # def get_absolute_url(self):
    #     return reverse('events:team-detail', kwargs={'pk': self.pk})


class LinkForm(ModelForm):
    class Meta:
        model = Link
        exclude = ['pub_date']
        #fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        
    # def get_absolute_url(self):
    #     return reverse('events:team-detail', kwargs={'pk': self.pk})


class BookForm(ModelForm):
    class Meta:
        model = Book
        exclude = ['pub_date']
        # fields = '__all__'
        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }
        
    # def get_absolute_url(self):
    #     return reverse('events:team-detail', kwargs={'pk': self.pk})

