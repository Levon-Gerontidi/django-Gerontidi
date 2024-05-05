from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html_main = f"<h1>Система контроля качества</h1><p><a href='{bug_list_url}'>Список всех багов</a></p><p><a href='{feature_list_url}'>Запросы на улучшение</a></p>"
    return HttpResponse(html_main)

def bug_list(request):
    html_bug = f"<h1>Список отчётов об ошибках</h1><p>"
    return HttpResponse(html_bug)

def feature_list(request):
    html_feature = f"<h1>Список запросов на улучшение</h1><p>"
    return HttpResponse(html_feature)

def bug_id_detail(request, bug_id):
    return HttpResponse(f"Детали бага {bug_id}")

def feature_id_detail(request, feature_id):
    return HttpResponse(f"Детали улучшения {feature_id}")