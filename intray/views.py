from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Item


# def index(request):
def index():
    return HttpResponseRedirect("/add")


@login_required()
def add(request):
    # Add new item if POST request
    if request.method == "POST":
        Item.objects.create(item_text=request.POST["item_text"])
        return HttpResponseRedirect("/add")

    # Otherwise, render add page
    return render(request, "intray/add.html")


@login_required()
def process(request):
    # Archive item if POST request, then rerender page
    if request.method == "POST":
        item_uuid = request.POST["item_uuid"]
        item_to_archive = Item.objects.get(item_uuid=item_uuid)

        # Set is_archived to True
        item_to_archive.is_archived = True
        item_to_archive.save()
        return HttpResponseRedirect("/process")

    # Otherwise, render process page with oldest item (if any)
    items = Item.objects.all().filter(is_archived=False)
    oldest_item = items.order_by("timestamp")[:1]
    if oldest_item:
        oldest_item = oldest_item[0]
    context = {"oldest_item": oldest_item, "item_count": items.count()}
    return render(request, "intray/process.html", context)


class ArchiveView(LoginRequiredMixin, generic.ListView):
    template_name = "intray/archive.html"
    context_object_name = "archived_items"

    def get_queryset(self):
        return Item.objects.all().filter(is_archived=True).order_by("-timestamp")


class ArchivedItemView(LoginRequiredMixin, generic.DetailView):
    slug_field = "item_uuid"
    model = Item
    template_name = "intray/archived_item.html"
