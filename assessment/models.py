from django.db import models

class Assessment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Question(models.Model):
    QUESTION_TYPES = [
        ('MCQ', 'Multiple Choice'),
        ('LIKERT', 'Likert Scale'),
        ('RATING', 'Rating Scale'),
        ('TRUE_FALSE', 'True/False'),
        ('RANKING', 'Ranking'),
        ('OPEN_ENDED', 'Open-Ended'),
        ('SEMANTIC', 'Semantic Differential'),
        ('CHECKLIST', 'Checklist'),
        ('BINARY', 'Binary'),
    ]
    assessment = models.ForeignKey(Assessment, on_delete=models.CASCADE, related_name='questions')
    name = models.CharField(max_length=200)
    description = models.TextField()
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='options')
    text = models.CharField(max_length=200)

class Response(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    text_response = models.TextField(null=True, blank=True)
    rating_response = models.IntegerField(null=True, blank=True)
