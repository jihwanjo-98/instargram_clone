from django.shortcuts import render,redirect
from rest_framework.views import APIView
#from django.views.generic import ListView,DetailView
from .models import Feed
from rest_framework.response import Response
import os
from django.conf import settings
from instargram.settings import MEDIA_ROOT
from uuid import uuid4
# APIView는 클라이언트와 서버가 데이터를 주고받을 수 있도록 도와주는 역할

# Create your views here.
class Main_post(APIView):
    
    template_name= 'kiki_h/html/feed_detail.html'
    
    def get(self, request):
        # 포스트(Post) 목록을 가져와서 템플릿에 전달
        feed_list = Feed.objects.all().order_by('-id')
        context = {'feed_list': feed_list}
        return render(request, self.template_name, context)
    '''
    def post(self,request):   
        
        if(request.method == 'POST'):
            
            feed_content = request.POST.get('content',None)   # post로 전달받은 'content'이름의 태그 가져오기 
            post=Feed()                                  # 모델 불러오기
            post.content = feed_content                  # 테이블에 데이터 입력
            post.save()                                  # 모델저장
            return redirect(request.path)
        else:
            return render(request,self.template_name)
    '''

class UploadFeed(APIView):
    def post(self, request):
        file = request.FILES.get('file')  # 요청한 파일을 읽어옴
        uuid_name = uuid4().hex     # 임의의 고유 id 생성 => 파일명이 한글이나 특수문자 포함될때 에러 차단하기 위해
        save_path = os.path.join(MEDIA_ROOT, uuid_name)   
        with open(save_path, 'wb+') as destination:   # 이미지파일을 media디렉토리에 바이너리로 읽어서 저장
            for chunk in file.chunks():
                destination.write(chunk)
        content = request.data.get('content')
        image = uuid_name
        profile_image = request.data.get('profile_image')
        user_id = request.data.get('user_id')
        try:
            Feed.objects.create(content=content, image=image, profile_image=profile_image, user_id=user_id, like_count=0)
        except:
            return Response(status = 404)
        return Response(status=200)