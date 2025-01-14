from django.http import HttpResponse, JsonResponse
from django.db import transaction, connection

def get_department(departmentCode=None):
    if departmentCode == None:
        query = "SELECT * FROM Departments;"
        params = []
        return get_public_request(query, params)
    else:
        query = "SELECT * FROM Departments WHERE departmentCode = %s;"
        params = [departmentCode]
        empty_response = JsonResponse({"error": "Department not found"}, safe=False)
        return get_public_request(query, params, empty_response)

def get_courses(departmentCode):
    query = "SELECT * FROM Courses WHERE departmentCode = %s;"
    params = [departmentCode]
    return get_public_request(query, params)

def get_course(courseId):
    query = "SELECT * FROM Courses WHERE courseId = %s;"
    params = [courseId]
    empty_response = JsonResponse({"error": "Course not found"}, safe=False)
    return get_public_request(query, params, empty_response)

def get_categories(courseId):
    query = "SELECT * FROM Categories WHERE courseId = %s;"
    params = [courseId]
    return get_public_request(query, params)

def get_category_posts(courseId, titleId):
    query = "SELECT * FROM Posts WHERE courseId = %s AND titleId = %s;"
    params = [courseId, titleId]
    return get_public_request(query, params)

def get_user(userId):
    query = "SELECT * FROM Users WHERE id = %s;"
    params = [userId]
    empty_response = JsonResponse({"error": "User not found"}, safe=False)
    return get_public_request(query, params, empty_response)

def get_user_posts(userId):
    query = "SELECT * FROM Posts WHERE userId = %s;"
    params = [userId]
    return get_public_request(query, params)

def get_post(postId):
    query = "SELECT * FROM Posts WHERE id = %s;"
    params = [postId]
    empty_response = JsonResponse({"error": "Post not found"}, safe=False)
    return get_public_request(query, params, empty_response)

def get_post_reactions(postId, params):
    if "type" not in params or params["type"] not in ["0", "1"]:
        return JsonResponse({"error": "Invalid request"}, safe=False)
    type_name = "upvotes" if params["type"] == "1" else "downvotes" 
    is_count = "count" in params and params["count"].lower() == "true"

    if is_count:
        query = "SELECT COUNT(postId) as " + type_name + " FROM Reactions WHERE postId = %s AND upvote = %s;"
    else:
        query = "SELECT * FROM Reactions WHERE postId = %s AND upvote = %s;"
    params = [postId, params["type"]]
    return get_public_request(query, params)

def create_department():
    pass

def create_course():
    pass

def create_category():
    pass

def create_user():
    pass

def create_post():
    pass

def create_reaction():
    pass

def get_request(query, params, permission_query=None, permission_params=None, empty_response=None):
    if permission_query:
        has_permission = len(execute_query(permission_query, permission_params).fetchone() != 0)
        if not has_permission:
            return JsonResponse({"error": "No permission"}, safe=False)

    result = dictfetchall(execute_query(query, params))
    if empty_response is not None and len(result) == 0:
        return empty_response
    return JsonResponse(result, safe=False)

def get_public_request(query, params, empty_response=None):
    return get_request(query, params, None, None, empty_response)

def get_permission_request(query, params, permission_query, permission_params, empty_response=None):
    return get_request(query, params, permission_query, permission_params, empty_response)

def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]

def execute_query(query, params=None):
    with transaction.atomic():
        cursor = connection.cursor()
        cursor.execute(query, params)
        return cursor