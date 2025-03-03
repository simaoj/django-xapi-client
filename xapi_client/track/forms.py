from django.core.validators import EmailValidator
from django.utils.translation import gettext_lazy as _
from django import forms
from datetimewidget.widgets import DateTimeWidget
from django.conf import settings

from xapi_client.xapi_vocabularies import xapi_language_codes
from xapi_client.utils import get_recipe_choices, get_verb_choices, get_activity_choices, get_contextual_activity_choices

context_activity_relation_choices = [
    ('grouping', _('grouping (generic relation)')),
    ('parent', _('parent (containment relation)'))
]

dateTimeOptions = {
'minView': 0,
'maxView': 3,
'startView': 2,
'weekStart': 1,
'minuteStep': 1, # default 5
'format': 'dd/mm/yyyy hh:ii',
'startDate': '01/01/2000 00:00',
'endDate': '31/12/2020 23:59',
}

class SelfRecordForm(forms.Form):
    """
    actor_name = forms.CharField(required=False, label=_('actor full name'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('this is a computed value'),)
    actor_email = forms.EmailField(required=False, label=_('actor email'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('this is a computed value'),)
    """
    actor_name = forms.CharField(widget=forms.HiddenInput())
    actor_email = forms.CharField(widget=forms.HiddenInput())
    timestamp = forms.DateTimeField(required=True, label=_('timestamp'), input_formats=['%d/%m/%Y %H:%M'], widget=DateTimeWidget(bootstrap_version=3, options=dateTimeOptions, attrs={'id': 'timestamp', 'class':'form-control',}), help_text=_('when the experience occurred; format: dd/mm/yyyy hh:mm'))
    platform = forms.CharField(required=True, label=_('learning platform'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('can be the name of any activity provider'),)
    endpoint = forms.CharField(widget=forms.HiddenInput())
    recipe_ids = forms.MultipleChoiceField(required=True, label=_('xAPI recipes'), choices=get_recipe_choices, widget=forms.SelectMultiple(attrs={'class':'form-control', 'onchange': 'javascript: this.form.submit()',}), help_text=_('select one or more, then wait for the form to refresh'),)
    verb_id = forms.ChoiceField(required=False, label=_('verb'), choices=get_verb_choices, widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, choose after selecting the recipe(s); currently the match with the activity type is not checked'),)
    activity_type = forms.ChoiceField(required=False, label=_('activity type'), choices=get_activity_choices, widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, choose after selecting the recipe(s); currently the match with the verb is not checked'),)
    object_name = forms.CharField(required=True, label=_('activity name'), widget=forms.TextInput(attrs={'class':'form-control', }), help_text=_('the name of the specific activity, distinguishing it among other activities of the same type'),)
    object_id = forms.CharField(required=True, label=_('activity unique identifier'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('can be an URL, a URI, a DOI, an ISBN code or the like'),)
    object_description = forms.CharField(required=False, label=_('activity description'), widget=forms.Textarea(attrs={'class':'form-control', 'rows': 2,}), help_text=_('an optional description of the specific activity'),)
    object_language = forms.ChoiceField(required=True, label=_('Language of name and description'), choices=xapi_language_codes, widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, specify the language used for the name and the description of the activity object'),)
    context_activity_type = forms.ChoiceField(required=False, label=_('contextual activity type'), choices=get_contextual_activity_choices, widget=forms.Select(attrs={'class':'form-control',}), help_text=_('the type of a related activity, if any'),)
    context_object_name = forms.CharField(required=True, label=_('contextual activity name'), widget=forms.TextInput(attrs={'class':'form-control', }), help_text=_('the name of the related activity, distinguishing it among other activities of the same type'),)
    context_object_id = forms.CharField(required=True, label=_('contextual activity unique identifier'), widget=forms.TextInput(attrs={'class':'form-control',}), help_text=_('the unique id of the related activity; can be an URL, a URI, a DOI, an ISBN code or the like'),)
    context_activity_relationship = forms.ChoiceField(required=False, label=_('contextual activity relationship'), choices=context_activity_relation_choices, widget=forms.Select(attrs={'class':'form-control',}), help_text=_('please, specify how the contextual activity is related to the one being recorded'),)
    """
    authority_name = forms.CharField(required=False, label=_('authority name'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('name of person or agency certifying this activity; this is a fixed value'),)
    authority_email = forms.EmailField(required=False, label=_('authority email'), widget=forms.TextInput(attrs={'readonly':'readonly', 'class':'form-control',}), help_text=_('email of person or agency certifying this activity; this is a fixed value'),)
    """
