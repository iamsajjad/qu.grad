
from django import forms

from bio.models import Bio


class BioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = (
        'full_name', 'surname', 'image', 'birthday', 'nationality', 'gender', 'degree', 'college',
        'department', 'mother_lang', 'other_langs', 'phone', 'email', 'grad_date',

        'ar_full_name', 'ar_nationality', 'ar_college', 'ar_department', 'ar_degree', 'ar_state',
        'ar_district', 'ar_job_type', 'ar_job_place', 'ar_mother_lang', 'ar_other_langs',)


class DeleteBioForm(forms.ModelForm):
    class Meta:
        model = Bio
        fields = ()

