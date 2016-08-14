from django import forms

class CareerForm(forms.Form)
    major_group = forms.ModelChoiceField(queryset=major_groups, empty_label="(Major Group)")
    minor_group = forms.ModelChoiceField(queryset=minor_groups, empty_label="(Minor Group)")
    broad_group = forms.ModelChoiceField(queryset=broad_groups, empty_label="(Broad Group)")
    detailed_occupation = forms.ModelChoiceField(queryset=detailed_occupations, empty_label="(Occupation)")
