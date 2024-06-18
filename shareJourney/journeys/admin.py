from cloudinary.models import CloudinaryResource
from django.contrib import admin
from django.utils.html import mark_safe

from .models import User, Journey, Participation, Post, Comment, Report, Image, CommentJourney, ReportedUser


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'rate', 'is_active']
    readonly_fields = ['img']

    def img(self, obj):
        if obj.avatar:
            if type(obj.avatar) is CloudinaryResource:
                return mark_safe(
                    f'<img src="{obj.avatar.url}" height="200" alt="avatar" />'
                )
            return mark_safe(
                f'<img src="{obj.avatar.name}" height="200" alt="avatar" />'
            )


class ImageInlineAdmin(admin.StackedInline):
    model = Image
    extra = 0
    fk_name = 'post'


class CommentInlineAdmin(admin.StackedInline):
    model = Comment
    extra = 0
    fk_name = 'post'


class CommentJourneyInlineAdmin(admin.StackedInline):
    model = CommentJourney
    extra = 0
    fk_name = 'journey'


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'content', 'created_date', 'user']
    inlines = [CommentInlineAdmin, ImageInlineAdmin, ]


class ParticipationInlineAdmin(admin.StackedInline):
    model = Participation
    extra = 0
    fk_name = 'journey'


class ParticipationAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'journey','journey_id','is_approved']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'content', 'created_date']


class JourneyAdmin(admin.ModelAdmin):
    list_display = ['id', 'name_journey', 'created_date', 'start_location', 'end_location', 'active', 'user_create']
    search_fields = ['name_journey']
    inlines = [CommentJourneyInlineAdmin, ParticipationInlineAdmin, ]


class ReportInline(admin.StackedInline):
    model = Report
    extra = 0
    readonly_fields = ('reported_user', 'reported_by', 'reason')


class ReportedUserAdmin(admin.ModelAdmin):
    list_display = ('user', 'report_count', 'is_processed', 'activate_user')
    ordering = ('is_processed', '-report_count',)
    readonly_fields = ('user', 'report_count')
    inlines = [ReportInline, ]

    def activate_user(self, obj):
        return obj.user.is_active

    activate_user.boolean = True  # hiển thị tick or X
    activate_user.short_description = 'Is Active'


class JourneyAppAdminSite(admin.AdminSite):
    site_title = 'Trang quản trị của tôi'
    site_header = 'Hệ thống Quản lý hành trình trực tuyến'
    index_title = 'Trang chủ quản trị'

    def get_app_list(self, request, app_label=None):
        return super().get_app_list(request) + [
            {
                'name': 'STASTISTIC',
                'models': [
                    {
                        'name': 'Thống kê các hành trình',
                        'admin_url': '/admin/statistics',
                        "view_only": True,
                    },
                ]
            }
        ]


admin_site = JourneyAppAdminSite(name='myjourney')

admin_site.register(Journey, JourneyAdmin)
admin_site.register(User, UserAdmin)
admin_site.register(Participation, ParticipationAdmin)
admin_site.register(Post, PostAdmin)
admin_site.register(Comment, CommentAdmin)
admin_site.register(CommentJourney, CommentAdmin)
admin_site.register(ReportedUser, ReportedUserAdmin)
