from django.contrib import admin
from .models import BugReport, FeatureRequest

# Класс администратора для модели BugReport
@admin.register(BugReport)
class BugReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task')
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority')
        }),
    )
    
    list_editable = ('status', 'priority')
    
    def change_status_to_new(self, request, queryset):
        queryset.update(status='New')
    
    def change_status_to_in_progress(self, request, queryset):
        queryset.update(status='In_progress')
    
    def change_status_to_completed(self, request, queryset):
        queryset.update(status='Completed')
    
    change_status_to_new.short_description = "Изменить статус на 'Новая'"
    change_status_to_in_progress.short_description = "Изменить статус на 'В работе'"
    change_status_to_completed.short_description = "Изменить статус на 'Завершена'"
    
    actions = ['change_status_to_new', 'change_status_to_in_progress', 'change_status_to_completed']

# Класс администратора для модели FeatureRequest
@admin.register(FeatureRequest)
class FeatureRequestAdmin(admin.ModelAdmin):
    list_display = ('title', 'project', 'status', 'priority', 'created_at', 'updated_at')
    list_filter = ('status', 'priority', 'project')
    search_fields = ('title', 'description')
    
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'project', 'task')
        }),
        ('Status and Priority', {
            'fields': ('status', 'priority')
        }),
    )