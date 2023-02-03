from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from .models import Project, WorkOrder

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['python', 'r_language', 'excel', 'machine_learning', 'hourly_contract', 'django', 'react', 'project_name', 'description']

form = ProjectForm()


ProjectFormSet = inlineformset_factory(
    WorkOrder,
    Project, 
    form= ProjectForm,
    extra=1
)