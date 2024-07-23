from django.db import models

class Assessment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

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
    assessment = models.ForeignKey(Assessment, related_name='questions', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    question_type = models.CharField(max_length=50, choices=QUESTION_TYPES)

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

class Response(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    text_response = models.TextField(null=True, blank=True)
    user_id = models.IntegerField()
    completed = models.BooleanField(default=False)
