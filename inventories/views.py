from django.shortcuts import render
from .models import Inventory

def inventory_list(request):
	context = {
	"inventories": Inventory.objects.all(),
	}
	return render(request, "inv_list.html", context)