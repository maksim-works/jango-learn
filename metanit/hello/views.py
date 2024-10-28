from django.http import HttpResponse

def index(request):
    host = request.META["HTTP_HOST"]
    user_agent = request.META["HTTP_USER_AGENT"]
    path = request.path
    return HttpResponse(f"""
            <h2>Главная</h2>
            <p>REQ: {request.META}</p>
            <p>Host: {host}</p>
            <p>Path: {path}</p>
            <p>User agent: {user_agent}</p>
    """)

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О сайте</h2>
            <p>Имя: {name} </p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("<h2>Контакты</h2>")

def headers(request):
    return HttpResponse("Test text + header 'Secret_Code'", headers={"Secret-Code": "1234567890"})

def send_error(request):
    return HttpResponse("Произошла ошибка", status=400, reason="Incorrect data")

def send_text(request):
    return HttpResponse("<h1>Hello</h1>", content_type="text/plain", charset="utf-8")

def user(request, name):
    return HttpResponse()