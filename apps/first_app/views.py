from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
	context = {
		'current_date': datetime.now().strftime('%b %d, %Y'),
		'current_time': datetime.now().strftime('%I:%M %p')
	}
	return render(request, 'first_app/index.html', context)