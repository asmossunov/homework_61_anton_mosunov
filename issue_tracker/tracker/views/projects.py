from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from tracker.models import Project, Task
# from tracker.forms import SearchForm, ProjectForm


class ProjectView(DetailView):
    template_name = 'project_detail.html'
    model = Project

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        project = self.object
        tasks = project.tasks.order_by('-created_at')
        context['tasks'] = tasks
        return context


#
#
# class ArticleUpdateView(UpdateView):
#     template_name = 'project_update.html'
#     form_class = ProjectForm
#     model = Project
#     context_object_name = 'project'
