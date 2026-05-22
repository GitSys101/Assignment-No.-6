from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.contrib import messages
from .models import RecipePhoto
from .forms import RecipePhotoForm
import cloudinary.uploader

class GalleryListView(ListView):
    model = RecipePhoto
    template_name = 'gallery/home.html'
    context_object_name = 'photos'
    paginate_by = 2

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        if query:
            return RecipePhoto.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            ).order_by('-uploaded_at')
        return RecipePhoto.objects.all().order_by('-uploaded_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q', '')
        return context

class RecipePhotoCreateView(PermissionRequiredMixin, CreateView):
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/create.html'
    success_url = reverse_lazy('gallery_home')
    permission_required = 'gallery.add_recipephoto'

    def form_valid(self, form):
        messages.success(self.request, "Photo uploaded successfully!")
        return super().form_valid(form)

class RecipePhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = RecipePhoto
    form_class = RecipePhotoForm
    template_name = 'gallery/edit.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('gallery_home')
    permission_required = 'gallery.change_recipephoto'

    def form_valid(self, form):
        messages.success(self.request, f"'{form.instance.title}' updated successfully!")
        return super().form_valid(form)

class RecipePhotoDeleteView(PermissionRequiredMixin, DeleteView):
    model = RecipePhoto
    template_name = 'gallery/delete.html'
    context_object_name = 'photo'
    success_url = reverse_lazy('gallery_home')
    permission_required = 'gallery.delete_recipephoto'

    def form_valid(self, form):
        try:
            photo = self.get_object()
            title = photo.title
            
            # Delete from Cloudinary if image exists
            if photo.image:
                try:
                    # CloudinaryField value has public_id if it's a valid resource
                    public_id = getattr(photo.image, 'public_id', None)
                    if public_id:
                        cloudinary.uploader.destroy(public_id)
                except Exception as e:
                    print(f"Cloudinary deletion failed: {e}")
            
            messages.success(self.request, f"'{title}' was completely deleted.")
            return super().form_valid(form)
        except Exception as e:
            messages.error(self.request, f"Delete failed: {str(e)}")
            return redirect('gallery_home')