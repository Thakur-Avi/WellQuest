from django.shortcuts import render
import requests
import json
# iYQFWJIrE3NxmQMzHFJIpw==JHHByCMkFF0qAqMo
def cal_count(request):
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query=' + query
        api_request = requests.get(api_url, headers={'X-Api-Key': 'iYQFWJIrE3NxmQMzHFJIpw==JHHByCMkFF0qAqMo'})
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Oops! An error occured"
        return render(request, 'cal_count.html', {'api':api})
    else:
        return render(request, 'cal_count.html', {'query':'Enter a valid query'})