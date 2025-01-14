from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods
from django.db import transaction, connection
import json

"""
Return all rows from a cursor as a dict.
Assume the column names are unique.
"""
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

"""
Execute a query and return the cursor.
"""
def execute_query(query, params=None):
    with transaction.atomic():
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor

@require_http_methods(["GET", "POST"])
def react(request):
    if request.method == "POST":
        return HttpResponse("POST request received")
    else:
        if "postId" not in request.GET:
            return JsonResponse({"error": "Post ID not provided"}, safe=False)
        
        query = "SELECT * FROM Reactions WHERE postId = %s;"
        reactions = dictfetchall(execute_query(query, [request.GET["postId"]]))

        return JsonResponse(reactions, safe=False)

@require_http_methods(["GET"])
def post_by_id(request):
    if "postId" not in request.GET:
        return JsonResponse({"error": "Post ID not provided"}, safe=False)
    
    query = "SELECT * FROM Posts WHERE id = %s;"
    post = dictfetchall(execute_query(query, [request.GET["postId"]]))

    if len(post) == 0:
        return JsonResponse({"error": "Post not found"}, safe=False)
    return JsonResponse(post, safe=False)

@require_http_methods(["GET"])
def posts_by_user(request):
    if "userId" not in request.GET:
        return JsonResponse({"error": "User ID not provided"}, safe=False)
    
    query = "SELECT * FROM Posts WHERE userId = %s;"
    posts = dictfetchall(execute_query(query, [request.GET["userId"]]))

    return JsonResponse(posts, safe=False)

@require_http_methods(["GET"])
def user_by_id(request):
    if "userId" not in request.GET:
        return JsonResponse({"error": "User ID not provided"}, safe=False)
    
    query = "SELECT * FROM Users WHERE id = %s;"
    user = dictfetchall(execute_query(query, [request.GET["userId"]]))

    if len(user) == 0:
        return JsonResponse({"error": "User not found"}, safe=False)
    return JsonResponse(user, safe=False)