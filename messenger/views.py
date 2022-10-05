import imp
from pkgutil import ImpImporter
from django.shortcuts import render
from messenger.forms import ReviewForm
from django.views.generic.edit import FormView
from django.http import HttpResponse



class ReviewEmailView(FormView):
    template_name="review.html"
    form_class=ReviewForm
    def form_valid(self, form):
        form.send_email()
        msg= "Thanks for your Feedback"
        return HttpResponse(msg)
