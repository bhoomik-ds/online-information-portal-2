from django.shortcuts import render, get_object_or_404
from .models import Job, QuickLink, CallLetter, AdmitCard
from results.models import Result
from notifications.models import Notification

# Create your views here.

def home(request):
    jobs = Job.objects.order_by('-created_at')[:10]
    results = Result.objects.order_by('-id')[:5]
    notifications = Notification.objects.order_by('order')[:5]
    quicklinks = QuickLink.objects.all()
    callletters = CallLetter.objects.all()
    admitcards = AdmitCard.objects.all()
    return render(request, 'jobs/home.html', {
        'jobs': jobs,
        'results': results,
        'notifications': notifications,
        'quicklinks': quicklinks,
        'callletters': callletters,
        'admitcards': admitcards,
    })

def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk)
    return render(request, 'jobs/job_detail.html', {'job': job})

def contact(request):
    if request.method == 'POST':
        # You can add form handling logic here
        pass
    return render(request, 'jobs/contact.html')

def job_list(request):
    jobs = Job.objects.all().order_by('-created_at')
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

def result_list(request):
    results = Result.objects.all().order_by('-id')
    return render(request, 'jobs/result_list.html', {'results': results})

def notification_list(request):
    notifications = Notification.objects.all().order_by('order')
    return render(request, 'jobs/notification_list.html', {'notifications': notifications})
