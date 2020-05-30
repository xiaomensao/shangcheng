from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group

def signup(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        # 提交表单
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')
            # 注册完成之后登录
            user = authenticate(username=username, password=password)
            login(request, user)
            # 添加group
            group_id = request.POST.get('group')
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            return redirect('/')
    else:
        # 展示表单
        form = UserCreationForm()
    return render(request, 'registration/signup.html', \
        {'form': form, 'groups': groups})