from django import forms
from django.http import HttpResponse
from django.views import View, generic
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from django.contrib import messages
from shared.utils import get_instance_or_404, perform_update
from ..models import Author
from ..forms import AuthorForm


class AuthorsListCreateView(generic.ListView, generic.CreateView):
    template_name = "library/authors/authors-list-create.html"
    form_class = AuthorForm

    def get(self, request, **kwargs):
        return render(
            request,
            self.template_name,
            {"authors": self.get_queryset(), "form": self.form_class()},
        )

    def get_queryset(self):
        return Author.objects.all()

    @method_decorator(permission_required("library.add_author"))
    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f"Author: {form.instance.full_name} added successfully"
            )
            return redirect(self.get_success_url())
        else:
            self.form_class = form
            messages.error(request, "Please fill correctly.")
            return redirect("library:authors_list_create")

    def get_success_url(self) -> str:
        return "/library/authors"


@method_decorator(permission_required("library.change_author"), name="post")
class AuthorDetailUpdateView(generic.DetailView, generic.UpdateView):
    template_name = "library/authors/author-detail.html"
    form_class = AuthorForm

    def get_object(self):
        return get_instance_or_404(view=self, model=Author)

    def get(self, request, **kwargs):
        return render(
            request,
            self.template_name,
            {
                "author": self.get_object(),
                "form": self.form_class(data=vars(self.get_object())),
            },
        )

    def post(self, request, **kwargs) -> HttpResponse:
        form = self.form_class(
            Author.objects.get(pk__exact=self.get_object().pk), request.POST
        )
        if form.is_valid():
            return self.form_valid(form)
        else:
            self.form_class = form
            messages.error(request, "Update contains invalid information")
            return redirect(self.get_success_url())

    def form_valid(self, form: AuthorForm):
        form.update(self.get_object(), form.cleaned_data)
        messages.success(self.request, "Author updated successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return f"/library/authors/{self.get_object().pk}/detail/"


@method_decorator(permission_required("library.delete_author"), name="dispatch")
class AuthorDeleteView(generic.DeleteView):
    template_name = "library/authors/delete-author.html"
    model = Author

    def post(self, request, *args, **kwargs):
        self.delete(request, *args, **kwargs)
        messages.success(request, "Author deleted successfully")
        return redirect(self.get_success_url())

    def get_success_url(self) -> str:
        return "/library/authors"
