from django.shortcuts import render
from django.http import HttpResponse
from .models import QueryLog
import pandas as pd
from django.db import connection
import csv

def execute_query(request):
    if request.method == 'POST':
        problem_statement = request.POST.get('problem_statement')
        sql_query = request.POST.get('sql_query')
        pandas_query = request.POST.get('pandas_query', None)
        pyspark_query = request.POST.get('pyspark_query', None)

        # SQL Execution
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                result = cursor.fetchall()
        except Exception as e:
            result = f"Error: {str(e)}"

        # Save Query to DB
        log = QueryLog.objects.create(
            problem_statement=problem_statement,
            sql_query=sql_query,
            pandas_query=pandas_query,
            pyspark_query=pyspark_query,
            result=str(result)
        )
        log.save()

        return render(request, 'queries/result.html', {'result': result})

    return render(request, 'queries/index.html')

def download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="queries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Problem Statement', 'SQL Query', 'Pandas Query', 'PySpark Query', 'Result'])

    for log in QueryLog.objects.all():
        writer.writerow([log.problem_statement, log.sql_query, log.pandas_query, log.pyspark_query, log.result])

    return response
    
