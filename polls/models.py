from django.db import models


class Question(models.Model):
    '''A Question has question and the publication date.
    '''
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    '''Choice has two fields.
       The text of the choice.
       A vote tally.
       Both are associated with Question.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
