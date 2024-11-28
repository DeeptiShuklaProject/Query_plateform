from django.db import models

class QueryLog(models.Model):
    problem_statement = models.TextField()
    sql_query = models.TextField()
    pandas_query = models.TextField(blank=True, null=True)
    pyspark_query = models.TextField(blank=True, null=True)
    result = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
