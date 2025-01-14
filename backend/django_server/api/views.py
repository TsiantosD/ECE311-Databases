from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from . import database_service as db_service
from django.http import JsonResponse

not_authenticated = JsonResponse({"error": "Not authenticated"}, safe=False)
    
@require_http_methods(["GET"])
def department(request, departmentCode=None):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_department(departmentCode)

@require_http_methods(["GET"])
def department_courses(request, departmentCode):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_courses(departmentCode)

@require_http_methods(["GET"])
def course(request, courseId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_course(courseId)

@require_http_methods(["GET"])
def course_categories(request, courseId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_categories(courseId)

@require_http_methods(["GET"])
def category_posts(request, courseId, titleId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_category_posts(courseId, titleId)

@require_http_methods(["GET"])
def user(request, userId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_user(userId)

@require_http_methods(["GET"])
def user_posts(request, userId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_user_posts(userId)

@require_http_methods(["GET", "POST"])
def post(request, postId=None):
    if request.method == "POST":
        return JsonResponse()
    elif check_authenticated() is None:
        return not_authenticated:
    return db_service.get_post(postId)

@require_http_methods(["GET"])
def post_reactions(request, postId):
    if check_authenticated() is None:
        return not_authenticated
    return db_service.get_post_reactions(postId, request.GET)

"""
Checks if the user is authenticated.

This is a placeholder function and should be replaced with an actual authentication check 
for your application (e.g., by checking session data, token, etc.).

Returns:
    str: The userId of the authenticated user or None if authentication failed
"""
def check_authenticated(cookie):
    return "1"

