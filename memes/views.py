from django.shortcuts import render, redirect
from .models import Meme, UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MemeForm


def memes(request):
    memes = Meme.objects.all()
    context = {"memes": memes}
    return render(request, "memes/memes.html", context)


def meme(request, pk):
    memeObj = Meme.objects.get(id=pk)
    tags = memeObj.tags.all()
    context = {"meme": memeObj, "tags": tags}
    return render(request, "memes/single-meme.html", context)


def home_page(request):
    memes = Meme.objects.all()
    context = {"memes": memes}
    return render(request, "index.html", context)


@login_required(login_url='/accounts/login/')
def uploadMeme(request):
    profile = request.user.userprofile
    form = MemeForm()

    if request.method == "POST":
        form = MemeForm(request.POST, request.FILES)
        if form.is_valid():
            meme = form.save(commit=False)
            meme.uploader = profile
            meme.save()
            messages.success(request, 'Meme uploaded successfully!')
            return redirect("memes")

    context = {'form': form}
    return render(request, "memes/meme_form.html", context)


@login_required(login_url='/accounts/login/')
def updateMeme(request, pk):
    profile = request.user.userprofile
    meme = profile.meme_set.get(id=pk)
    form = MemeForm(instance=meme)

    if request.method == 'POST':
        form = MemeForm(request.POST, request.FILES, instance=meme)
        if form.is_valid():
            meme = form.save()

            messages.success(request, 'Meme updated successfully!')
            return redirect('single-meme', pk=meme.id)

    context = {'form': form, 'meme': meme}
    return render(request, "memes/meme_form.html", context)


@login_required(login_url='/accounts/login/')
def deleteMeme(request, pk):
    profile = UserProfile.objects.get(user=request.user)
    meme = profile.meme_set.get(id=pk)
    if request.method == 'POST':
        meme.delete()
        messages.warning(request, 'Meme was deleted!')
        return redirect('memes')

    context = {'meme': meme}
    return render(request, "memes/delete_meme.html", context)
