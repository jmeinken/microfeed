import datetime

from pages import forms
from microfeed import models


def validate_form_with_inlines(form, children, post_data, model_instance=False):
    """Handles validation of form and all inline children.
    Returns updated form and children if validation passes, false if validation fails.
    """
    if model_instance:
        form = forms.PageForm(post_data, instance=model_instance)
    else:
        form = forms.PageForm(post_data)
    temp_children = []
    for child in children:
        if model_instance:
            temp_children.append( child(post_data, instance=model_instance) )
        else:
            temp_children.append( child(post_data) )
    children = temp_children
    children_valid = True
    for child in children:
        if not child.is_valid():
            children_valid = False
    if form.is_valid() and children_valid:
        is_valid = True
    else:
        is_valid = False
    return [form, children, is_valid]


def get_upcoming_events():
    now = datetime.datetime.now()
    upcoming_events = models.EventPostTime.objects.filter(start_date__gte=now).order_by('start_date', 'start_time')[:3]
    return upcoming_events










