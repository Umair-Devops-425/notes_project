from django.shortcuts import render, get_object_or_404
from .models import Note
from .forms import NoteForm


# Create your views here.
def note_list(request):
    notes = Note.objects.all()
    return render(request, "notes/note_list.html", {"notes": notes})

from django.shortcuts import render, redirect

# Creating a note_create view.
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("note_list")  # back to list after saving
    else:
        form = NoteForm()

    return render(request, "notes/note_form.html", {"form": form})\

# Creating a Note edit Function
def note_edit(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "notes/note_form.html", {"form": form, "note": note})

# Creating a Function to delete note
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        note.delete()
        return redirect("note_list")
    return render(request, "notes/note_detail.html", {"note": note})



