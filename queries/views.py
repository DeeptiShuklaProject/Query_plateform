

   
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import QueryLog
from django.db import connection
import csv


def execute_query(request):
    if request.method == 'POST':
        # Get form data
        problem_statement = request.POST.get('problem_statement')
        sql_query = request.POST.get('sql_query')
        pandas_query = request.POST.get('pandas_query', None)
        pyspark_query = request.POST.get('pyspark_query', None)

        # Execute SQL query
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_query)
                result = cursor.fetchall()
        except Exception as e:
            result = f"SQL Error: {str(e)}"

        # Save the query and result to the database
        log = QueryLog.objects.create(
            problem_statement=problem_statement,
            sql_query=sql_query,
            pandas_query=pandas_query,
            pyspark_query=pyspark_query,
            result=str(result) if result else "No result"
        )
        log.save()

        return render(request, 'queries/result.html', {'result': result})

    return render(request, 'queries/index.html')


def auto_search(request):
    # Auto-search logic
    term = request.GET.get('term', '')  # Get the search term
    if term:
        results = QueryLog.objects.filter(problem_statement__icontains=term)[:10]  # Limit to 10 results
        data = [
            {
                'id': query.id,
                'problem_statement': query.problem_statement,
            }
            for query in results
        ]
        return JsonResponse(data, safe=False)  # Return JSON response
    return JsonResponse([], safe=False)  # Empty response


def download_csv(request):
    # Create CSV download
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="queries.csv"'

    writer = csv.writer(response)
    writer.writerow(['Problem Statement', 'SQL Query', 'Pandas Query', 'PySpark Query', 'Result'])

    for log in QueryLog.objects.all():
        writer.writerow([log.problem_statement, log.sql_query, log.pandas_query, log.pyspark_query, log.result])

    return response
