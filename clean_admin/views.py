from django.contrib.admin.models import LogEntry
from django.core.exceptions import PermissionDenied
from django.views import generic


class AdminActionsHistory(generic.ListView):
    template_name = 'admin/actions_history.html'
    model = LogEntry
    context_object_name = "actions_history_list"
    paginate_by = 25

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied  # HTTP 403
        return super(AdminActionsHistory, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AdminActionsHistory, self).get_context_data(**kwargs)
        context["title"] = ""
        return context


