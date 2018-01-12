from django.conf import settings as djangoSettings
from django.shortcuts import render
from django.http import HttpResponse
from .forms import WallpaperForm

from PIL import Image, ImageDraw, ImageFont
import requests
import random

url = "https://i.imgur.com/p2HuGid.png"

image1 = Image.open(requests.get(url, stream=True).raw)

font_type = ImageFont.truetype("Arial.ttf", 30)
draw = ImageDraw.Draw(image1)


def index(request):
	form = WallpaperForm()
	if request.method == 'POST':
		form = WallpaperForm(request.POST)

		if form.is_valid():

			name = request.POST.get('name')
			age = request.POST.get('age')
			blood_group = request.POST.get('blood_group')
			emergency_contact_1_name = request.POST.get('emergency_contact_1_name')
			emergency_contact_1_rel = request.POST.get('emergency_contact_1_rel')
			emergency_contact_1_contact_1 = request.POST.get('emergency_contact_1_contact_1')
			emergency_contact_1_contact_2 = request.POST.get('emergency_contact_1_contact_2')
			emergency_contact_2_name = request.POST.get('emergency_contact_2_name')
			emergency_contact_2_rel = request.POST.get('emergency_contact_2_rel')
			emergency_contact_2_contact_1 = request.POST.get('emergency_contact_2_contact_1')
			emergency_contact_2_contact_2 = request.POST.get('emergency_contact_2_contact_2')

			print(name)

			text_name = "Name: {}".format(name)
			text_age = "Age: {}".format(age)
			text_blood_group = "Blood Group: {}".format(blood_group)

			emergency_contact_1_name_render = "Name: {} ({})".format(emergency_contact_1_name, emergency_contact_1_rel)
			emergency_contact_1_contact_render = "Contact: {} / {}".format(emergency_contact_1_contact_1, emergency_contact_1_contact_2)

			emergency_contact_2_name_render = "Name: {} ({})".format(emergency_contact_2_name, emergency_contact_2_rel)
			emergency_contact_2_contact_render = "Contact: {} / {}".format(emergency_contact_2_contact_1, emergency_contact_2_contact_2)

			(x, y) = (49, 600)

			draw.text(xy=(x,y), text=text_name, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 40), text=text_age, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 80), text=text_blood_group, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 120), text="", fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 160), text="Emergency/Family contact details:", fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 200), text="", fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 240), text=emergency_contact_1_name_render, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 280), text=emergency_contact_1_contact_render, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 320), text="", fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 360), text=emergency_contact_2_name_render, fill=(255, 255, 255), font=font_type)
			draw.text(xy=(x,y + 400), text=emergency_contact_2_contact_render, fill=(255, 255, 255), font=font_type)

			file_name = "media/{}.png".format(random.randint(1, 255))

			image1.save(file_name)
			file_name = file_name

			form.save(commit=False)
			form.save()

			return render(request, "result.html", {'fn': file_name})
		else:
			return HttpResponse("Opps! An error occured. :(")

	return render(request, 'index.html', {'form': form})
