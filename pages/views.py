from django.shortcuts import render

from .models import SiteContent, TeamMember


def about(request):
    """
    Trang Giới thiệu — render templates/pages/about.html.
    Field template cần (xem {% comment %} đầu file about.html):
      hero/vision/mission: 1 bản ghi SiteContent mỗi section (có thể None
        nếu chưa nhập qua admin — template tự có fallback |default).
      core_values: nhiều bản ghi SiteContent, section='about_value'.
      team_members: TeamMember đang active, sắp theo order.
    """
    context = {
        "hero": SiteContent.objects.filter(section=SiteContent.Section.ABOUT_HERO).first(),
        "vision": SiteContent.objects.filter(section=SiteContent.Section.ABOUT_VISION).first(),
        "mission": SiteContent.objects.filter(section=SiteContent.Section.ABOUT_MISSION).first(),
        "core_values": SiteContent.objects.filter(
            section=SiteContent.Section.ABOUT_VALUE
        ).order_by("order"),
        "team_members": TeamMember.objects.filter(is_active=True).order_by("order"),
    }
    return render(request, "pages/about.html", context)


def contact(request):
    """
    Trang Liên hệ — render templates/pages/contact.html.
    Field template cần: contact_info (nhiều bản ghi SiteContent,
    section='contact_info'; nếu rỗng, template tự hiện 3 mục mặc định qua
    nhánh {% empty %}).
    """
    context = {
        "contact_info": SiteContent.objects.filter(
            section=SiteContent.Section.CONTACT_INFO
        ).order_by("order"),
    }
    return render(request, "pages/contact.html", context)
