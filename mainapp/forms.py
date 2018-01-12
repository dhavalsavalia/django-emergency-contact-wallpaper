from django import forms
from .models import Wallpaper

class WallpaperForm(forms.ModelForm):
	class Meta:
		model = Wallpaper
		fields = [
					'name',
					'age',
					'blood_group',
					'emergency_contact_1_name',
					'emergency_contact_1_rel',
					'emergency_contact_1_contact_1',
					'emergency_contact_1_contact_2',
					'emergency_contact_2_name',
					'emergency_contact_2_rel',
					'emergency_contact_2_contact_1',
					'emergency_contact_2_contact_2',
				]
		widgets = {
			'file_name': forms.HiddenInput()
		}