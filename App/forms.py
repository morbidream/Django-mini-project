from django import forms
from .models import Projet

class AddProjectForm(forms.ModelForm):
    class Meta:
        model=Projet
        fields=('nom_projet','createur','superviseur','duree_projet','temps_alloue_par_projet',
                'besoins','description','est_valide')