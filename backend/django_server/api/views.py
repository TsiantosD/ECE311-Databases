from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import transaction, connection

@require_http_methods(["GET", "POST"])
def post(request):
    if request.method == "POST":
        return HttpResponse("POST request received")
    else:
        query = "SELECT * FROM Posts;"
        with transaction.atomic():
            with connection.cursor() as cursor:
                cursor.execute(query)
                posts = cursor.fetchall()
        return JsonResponse(posts, safe=False)