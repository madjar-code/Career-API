from django.contrib import admin
from .models import Node, Growth


@admin.register(Node)
class NodeAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    ordering = (
        '-created_at',
    )
    list_display = (
        'middle_name',
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
    def career_move(self, object) -> str:
        return f'{object.start_node} -> {object.end_node}'

    ordering = (
        '-created_at',
    )
    list_display = (
        'career_move',
        'counter',
        'period',
        'is_active',
    )
    readonly_fields = (
        'created_at',
        'updated_at',
        'id',
    )