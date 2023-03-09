from django.contrib import admin
from .models import Node, Growth


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = (
        '-created_at',
    )
    list_display = (
        'name',
        'node_type',
        'counter',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )


@admin.register(Growth)
class GrowthAdmin(admin.ModelAdmin):
    ordering = (
        '-created_at',
    )
    list_display = (
        'start_node',
        'end_node',
        'counter',
        'period',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )