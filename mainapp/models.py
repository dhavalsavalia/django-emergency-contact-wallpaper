from django.db import models
from django.utils.translation import ugettext_lazy as _


class Wallpaper(models.Model):
	name = models.CharField(max_length=120, verbose_name=_("Name"))
	age = models.IntegerField(verbose_name=_("Age"))
	blood_group = models.CharField(max_length=10, verbose_name=_("Blood Group"))
	emergency_contact_1_name = models.CharField(max_length=120, verbose_name=_("Emergency Contact Name"))
	emergency_contact_1_rel = models.CharField(max_length=120, verbose_name=_("Relation"))
	emergency_contact_1_contact_1 = models.CharField(max_length=15, verbose_name=_("Emergency Contact Phone Number 1"))
	emergency_contact_1_contact_2 = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Emergency Contact Phone Number 2"))
	emergency_contact_2_name = models.CharField(max_length=120, verbose_name=_("Emergency Contact Name"))
	emergency_contact_2_rel = models.CharField(max_length=120, verbose_name=_("Relation"))
	emergency_contact_2_contact_1 = models.CharField(max_length=15, verbose_name=_("Emergency Contact Phone Number 1"))
	emergency_contact_2_contact_2 = models.CharField(max_length=15, blank=True, null=True, verbose_name=_("Emergency Contact Phone Number 2"))

	class Meta:
		app_label = 'mainapp'
		verbose_name = _('data')

	def __str__(self):
		return self.name
