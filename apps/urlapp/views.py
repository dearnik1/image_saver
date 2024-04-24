from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import URLForm

@login_required
def url_form_view(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            # Process the URL (e.g., save it to the database)
            # Redirect to another page if necessary
            return redirect('success')  # Redirect to a success page
    else:
        form = URLForm()

    return render(request, 'url_form.html', {'form': form})

