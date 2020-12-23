from django.views.generic import DetailView
from organization.models import Organization

class OrganizationDetailView (DetailView):
    model = Organization
    template_name = 'organization/org_detail.html'