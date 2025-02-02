from crispy_forms.bootstrap import (
    AppendedText,
    FormActions,
    PrependedAppendedText,
    PrependedText,
)
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Column, Field, Layout, Row, Submit
from django import forms
from django.utils import timezone


class MessageForm(forms.Form):
    text_input = forms.CharField()
    text_input2 = forms.CharField()
    text_input_a = forms.CharField()
    text_input_b = forms.CharField()
    text_input_c = forms.CharField()

    textarea = forms.CharField(
        widget=forms.Textarea(),
    )

    radio_buttons = forms.ChoiceField(
        choices=(
            (
                "option_one",
                "Option one is this and that be sure to include why it's great",
            ),
            (
                "option_two",
                "Option two can is something else and selecting it will deselect option one",
            ),
        ),
        widget=forms.RadioSelect,
        initial="option_two",
    )

    checkboxes = forms.MultipleChoiceField(
        choices=(
            (
                "option_one",
                "Option one is this and that be sure to include why it's great",
            ),
            (
                "option_two",
                "Option two can also be checked and included in form results",
            ),
            (
                "option_three",
                "Option three can yes, you guessed it also be checked and included in form results",
            ),
        ),
        initial="option_one",
        widget=forms.CheckboxSelectMultiple,
        help_text="<strong>Note:</strong> Labels surround all the options for much larger click areas and a more usable form.",  # noqa
    )

    grouped_checkboxes = forms.MultipleChoiceField(
        choices=(
            ("Group 1", ((1, "Option one"), (2, "Option two"), (3, "Option three"))),
            ("Group 2", ((4, "Option four"), (5, "Option five"), (6, "Option six"))),
        ),
        initial=(1,),
        widget=forms.CheckboxSelectMultiple,
    )

    appended_text = forms.CharField(help_text="Here's more help text")

    appended_text2 = forms.CharField(help_text="And a bigger appended text field")

    appended_select = forms.ChoiceField(
        label="Select field with appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text",
    )

    prepended_appended_select = forms.ChoiceField(
        label="Select field with both preprended and appended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text",
    )

    prepended_select = forms.ChoiceField(
        label="Select field with prepended text",
        choices=[(1, "Choice 1"), (2, "Choice 2")],
        help_text="Some help text",
    )

    prepended_text = forms.CharField()

    prepended_text_two = forms.CharField()

    select = forms.ChoiceField(
        choices=(("1", "North"), ("2", "South"), ("3", "East"), ("4", "West")),
        help_text="Direction to go",
    )

    multicolon_select = forms.MultipleChoiceField(
        choices=(("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")),
    )
    datetime_field = forms.SplitDateTimeField(initial=timezone.now())
    boolean_field = forms.BooleanField()

    # Bootstrap4
    helper = FormHelper()
    helper.layout = Layout(
        Field("text_input"),
        Field("text_input2", css_class="input-lg"),
        Field("textarea", rows="3"),
        "radio_buttons",
        Field("checkboxes", style="background: #FAFAFA"),
        AppendedText("appended_text", ".00"),
        AppendedText("appended_text2", ".00", css_class="input-lg"),
        AppendedText("appended_select", ".00"),
        PrependedAppendedText("prepended_appended_select", "$", ".00"),
        PrependedText("prepended_select", "$"),
        PrependedText(
            "prepended_text",
            '<input type="checkbox" checked="checked" value="" id="" name="">',
            active=True,
        ),
        PrependedText("prepended_text_two", "@"),
        "select",
        "multicolon_select",
        "boolean_field",
        "grouped_checkboxes",
        "datetime_field",
        Row(
            Column("text_input_a", "text_input_b", css_class="col-xs-6"),
            Column("text_input_c", css_class="col-xs-6"),
        ),
        FormActions(
            Submit("save_changes", "Save changes", css_class="btn-primary"),
            Submit("cancel", "Cancel"),
        ),
    )

    helper.label_class = "col-lg-4"
    helper.field_class = "col-lg-8"
