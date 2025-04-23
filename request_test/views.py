from django.shortcuts import render
from .models import UploadedFile

# Create your views here.
def request_info_view(request):
    context = {
        'method':request.method,
        'get_data':request.GET,
        'post_data':request.POST,
        'user':request.user,
        'is_logged_in':request.user.is_authenticated,
        'session_value':request.session.get('demo','NON'),
        'user_agent':request.META.get('HTTP_USER_AGENT','UNKNOWN'),
        'client_ip':request.META.get('REMOTE_ADDR','UNKKNOWN'),
        'path':request.path,
        'full_url':request.build_absolute_uri()
    }
    request.session['demo'] = '세션에서 저장한 값입니다.'

    return render(request, 'request_test/request_info.html',context)

def file_upload_view(request):
    uploaded_file_url = None
    title = None

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file'] # <-여기에 동작 코드를 작성하세요 (1점)
        title = request.POST.get('title','') # <-여기에 동작 코드를 작성하세요( 1점)
        uploaded = UploadedFile.objects.create(title=title, file=file)
        uploaded_file_url = uploaded.file.url

    return render(request, 'request_test/upload_file.html',{
        'uploaded_file_url':uploaded_file_url,
        'title':title
    })

