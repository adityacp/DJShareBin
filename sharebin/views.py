# Django Imports
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
from django.utils import timezone
from django.contrib import messages

# Local Imports
from .forms import PasteForm
from .models import Share


def add_or_edit_paste(request, paste_uuid=None):
    context = {}
    try:
        share = Share.objects.get(uid=paste_uuid)
        if not _is_valid_share(share):
            text = "The shareable link is expired"
            return HttpResponse(text, content_type='text/plain')
    except Share.DoesNotExist:
        share = None
    if request.method == 'POST':
        form = PasteForm(request.POST, instance=share)
        if form.is_valid():
            data = form.save(commit=False)
            data.set_expiry_time()
            data.save()
            if paste_uuid:
                messages.success(
                    request, "Updated your snippet successfully"
                )
            else:
                messages.success(
                    request, "Created your snippet successfully"
                )

            return redirect(
                reverse("sharebin:add_or_edit_paste", args=[data.uid])
            )
        else:
            context['form'] = form
    else:
        form = PasteForm(instance=share)
        context['form'] = form
    context['paste_uuid'] = paste_uuid
    return render(request, 'create_paste.html', context)


def _is_valid_share(share):
    status = True
    if share.expiry_time and share.expiry_time < timezone.now():
        status = False
    return status


def view_paste(request, paste_uuid):
    context = {}
    try:
        share = Share.objects.get(uid=paste_uuid)
        context["status"] = True
        if not _is_valid_share(share):
            context["status"] = False
            messages.warning(
                request, "The shareable link is expired"
            )
        context["share"] = share
    except Share.DoesNotExist:
        share = None
        context["status"] = False
        messages.warning(request, "No shareable information found for the link")
    return render(request, 'view_paste.html', context)


def view_raw_paste(request, paste_uuid):
    try:
        share = Share.objects.get(uid=paste_uuid)
        if not _is_valid_share(share):
            text = "The shareable link is expired"
        else:
            text = share.text
    except Share.DoesNotExist:
        share = None
        text = "No shareable information found for the link"
    return HttpResponse(text, content_type='text/plain')


def download_paste(request, paste_uuid):
    try:
        share = Share.objects.get(uid=paste_uuid)
        if not _is_valid_share(share):
            text = "The shareable link is expired"
            response = HttpResponse(text)
        else:
            response = HttpResponse(share.text, content_type='text/plain')
            response['Content-Disposition'] = 'attachment; filename={0}.txt'.format(
                                            share.name.replace(" ", "_")
                                            )
            response.write(share.text)
    except Share.DoesNotExist:
        share = None
        text = "No shareable information found for the link"
        response = HttpResponse(text)
    return response
