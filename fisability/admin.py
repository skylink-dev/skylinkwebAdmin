from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse, path, include
from .models import CoverageArea
from . import admin_urls


@admin.register(CoverageArea)
class CoverageAreaAdmin(admin.ModelAdmin):
    list_display = ("city", "area_name", "radius_km", "view_on_map", "all_areas_map")

    readonly_fields = ("map_preview",)

    fieldsets = (
        ("Location Details", {
            "fields": ("city", "area_name", "center_lat", "center_lng", "radius_km")
        }),
        ("Map Preview", {
            "fields": ("map_preview",),
        }),
    )

    # ------------------------------------------------------------------
    # 🔥 The MOST IMPORTANT PART → Load custom admin URLs
    # ------------------------------------------------------------------
   

    # ------------------------------------------------------------------

    def view_on_map(self, obj):
        return format_html(
            '<a href="/admin/coverage/map/?id={}" target="_blank">View Map</a>',
            obj.id
        )
    view_on_map.short_description = "Map"

    def map_preview(self, obj):
        if not obj.id:
            return "Save the record to view map."

        return format_html(
            '<iframe src="/admin/coverage/map/?id={}" '
            'style="width:100%; height:400px; border:1px solid #ccc;"></iframe>',
            obj.id
        )

    def all_areas_map(self, obj=None):
        url = reverse("coverage-map-all")
        return format_html(f'<a href="{url}" target="_blank">View All Areas Map</a>')
    all_areas_map.short_description = "All Areas Map"
