from importlib.metadata import requires
from django.shortcuts import render, redirect
from .models import UserModel
from django.contrib import auth  # 사용자 auth 기능
from django.contrib.auth.decorators import login_required
import re  # 정규표현식 모듈


# Create your views here.

def home(request):
    user = request.user.is_authenticated
    if user:
        return render(request, 'home.html')
    else:
        return redirect('/login')




def sign_up_view(request):
    if request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home/')
        else:
    
            return render(request, 'user/signup.html')

    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '')

        if password != password2:
            return render(request, 'user/signup.html', {'error': '패스워드를 확인 해 주세요!'})
        else:
            if username == '' or password == '':
                return render(request, 'user/signup.html', {'error': '사용자 이름과 패스워드는 필수값 입니다'})

            exist_user = auth.get_user_model().objects.filter(username=username)
            if exist_user:
                return render(request, 'user/signup.html',
                              {'error': '사용자가 이미 존재합니다.'})  # 중복이름 있으니 로그인페이지 다시 띄움, 경고메세지도 넣음 좋을듯


            UserModel.objects.create_user(username=username, password=password, phone=phone, address=address)
            return redirect('/login')  # 회원가입이 완료되었으므로 로그인 페이지로 이동
            
            
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        

        me = auth.authenticate(request, username=username, password=password)  # 사용자 불러오기
        if me is not None:  # 저장된 사용자의 패스워드와 입력받은 패스워드 비교
            auth.login(request, me)
            return redirect('/home/')
        else:
            return render(request, 'user/login.html', {'error': '유저이름 혹은 패스워드를 확인해주세요.'})  # 로그인 실패
    elif request.method == 'GET':
        user = request.user.is_authenticated
        if user:
            return redirect('/home/')
        else:
            return render(request, 'user/login.html')