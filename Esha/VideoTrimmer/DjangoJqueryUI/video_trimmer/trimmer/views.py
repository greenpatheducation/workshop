from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, Http404
import mimetypes
import os
from moviepy.editor import *


uploaded_file_url = ""


def home(request):
    return render(request, 'home.html')


def trim(request):
    if request.method == 'POST' and request.FILES['myfile'] and request.POST.get('selectedoptions'):
        option = request.POST.get('selectedoptions')
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        global uploaded_file_url
        uploaded_file_url = fs.url(filename)
        if(option == "span"):
            return render(request, 'span.html')
        else:
            return render(request, 'withoutspan.html')

    return render(request, 'home.html')


def result(request):
    global uploaded_file_url
    total_files = []
    files = []
    st = []
    et = []
    x = 1
    temp_file = request.POST.get('file' + str(x), "NULL")
    temp_start = request.POST.get('start' + str(x), 0)
    temp_end = request.POST.get('end' + str(x), 0)
    while(temp_file != "NULL"):
        st.append(int(temp_start.split(":")[
                  0])*60*60+int(temp_start.split(":")[1])*60+int(temp_start.split(":")[2]))
        et.append(int(temp_end.split(":")[
                  0])*60*60+int(temp_end.split(":")[1])*60+int(temp_end.split(":")[2]))
        files.append(temp_file)
        x += 1
        temp_file = request.POST.get('file' + str(x), "NULL")
        temp_start = request.POST.get('start' + str(x), 0)
        temp_end = request.POST.get('end' + str(x), 0)
    file = uploaded_file_url.split('/')[2]
    clip = VideoFileClip("media/"+file)
    count = 0
    while(count < len(files)):
        clip2 = clip.subclip(st[count], et[count])
        f = files[count] + ".mp4"
        clip2.write_videofile("media/"+f)
        total_files.append(f)
        count += 1
    return render(request, 'result.html', {
        'total_files': total_files
    })


def result2(request):

    global uploaded_file_url
    total_files = []
    span = []
    st = []
    et = []
    x = 1
    temp_span = request.POST.get('span' + str(x), "NULL")
    temp_start = request.POST.get('start' + str(x), 0)
    temp_end = request.POST.get('end' + str(x), 0)
    while(temp_span != "NULL"):
        st.append(int(temp_start.split(":")[
                  0])*60*60+int(temp_start.split(":")[1])*60+int(temp_start.split(":")[2]))
        et.append(int(temp_end.split(":")[
                  0])*60*60+int(temp_end.split(":")[1])*60+int(temp_end.split(":")[2]))
        span.append(int(temp_span))
        x += 1
        temp_span = request.POST.get('span' + str(x), "NULL")
        temp_start = request.POST.get('start' + str(x), 0)
        temp_end = request.POST.get('end' + str(x), 0)

    file = uploaded_file_url.split('/')[2]
    clip = VideoFileClip("media/"+file)
    count = 0
    while(count < len(span)):

        if et[count] != 0:
            dummyTime = st[count]+span[count]
            inner_count = 1
            while dummyTime <= et[count]:
                clip2 = clip.subclip(st[count], dummyTime)
                f = file.split('.')[0] + "_" + \
                    str(inner_count) + "." + file.split('.')[1]
                clip2.write_videofile("media/"+f)
                total_files.append(f)
                st[count] = dummyTime
                dummyTime = st[count] + span[count]
                inner_count += 1
        if et[count] == 0:
            et[count] = clip.duration
            leftDuration = et[count] - st[count]
            if leftDuration < span[count]:
                dummyTime = st[count] + leftDuration
            else:
                dummyTime = st[count] + span[count]
            inner_count = 1
            while dummyTime <= et[count] and st[count] != dummyTime:
                clip2 = clip.subclip(st[count], dummyTime)
                f = file.split('.')[0] + "_" + \
                    str(inner_count) + "." + file.split('.')[1]
                clip2.write_videofile("media/"+f)
                total_files.append(f)
                st[count] = dummyTime
                leftDuration = et[count] - st[count]
                if leftDuration < span[count]:
                    dummyTime = st[count] + leftDuration
                else:
                    dummyTime = st[count]+span[count]
                inner_count += 1
        count += 1
    return render(request, 'result.html', {
        'total_files': total_files
    })
