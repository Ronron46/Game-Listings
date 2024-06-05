from django import forms
from listings.models import Game
from listings.models import Plateform
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields= '__all__'
        labels={
            "plateforme" : _(mark_safe("Utilisez ctrl + clic pour selectionner plusieurs plateformes <br>"))
        }

class PlateformForm(forms.ModelForm):
    class Meta:
        model = Plateform
        fields='__all__'