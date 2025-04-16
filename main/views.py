from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def meetings_view(request):
    return render(request, 'meetings.html')

def meeting_detail_view(request, meeting_id):
    return render(request, 'meeting_detail.html', {'meeting_id': meeting_id})


