from django.shortcuts import render, redirect
from django.forms import modelformset_factory, inlineformset_factory, widgets
from .models import *
from django.views.generic.edit import CreateView
from .forms import RegistrationForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from .formUser import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.views.decorators.cache import cache_control
from telepot import Bot
from django.conf import settings


"""BLOCK №2. TelegramBot - New registrations"""

def teleRequest(request):   
    telegramBot = Bot(settings.TELEGRAM_BOT_API_KEY)
    def send_message(text):
        telegramBot.sendMessage(settings.TELEGRAM_MY_ID, text, parse_mode="Markdown")
    send_message("Кто-то хочет записаться на робототехнику!")
    return redirect('/registration')

"""END BLOCK №2. TelegramBot - New registrations"""


"""BLOCK №3. TelegramBot - Who visit my shop"""

def shop(request):   
    telegramBot = Bot(settings.TELEGRAM_BOT_API_KEY)
    def send_message(text):
        telegramBot.sendMessage(settings.TELEGRAM_MY_ID, text, parse_mode="Markdown")
    send_message("Кто-то зашел в магазин!")
    return redirect('http://robocluba.tilda.ws/')

"""END BLOCK №3. TelegramBot - Who visit my shop"""


"""BLOCK №4. Registration a new pupils at technical section"""


class RegistrationCreateView(CreateView):
    template_name = 'app_1/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ways'] = Ways.objects.all()
        return context


"""END BLOCK №4. Registration a new pupils at technical section"""


"""BLOCK №5. Simple pages"""

def awards(request):
    return render(request, 'app_1/awards.html')
    
    
def clean(request):
    return render(request, 'app_1/clean.html')


def index(request):
    return render(request, 'app_1/shedule.html')


def project(request):
    return render(request, 'app_1/projects.html')

def er(request):
    return render(request, 'error/er.html')

def kind_of_studing(request):
    return render(request, 'app_1/kind_of_studing.html')

@cache_control(private=True)
def TimetableRobots(request):
    return render(request, 'app_1/TimetableRobots.html')

def UsefullResources(request):
    return render(request, 'app_1/UsefullResources.html')

"""END BLOCK №5. Simple pages"""


"""BLOCK №6. Speed of read"""


def speed_read(request):
    group = Group_text.objects.all()
    first = group.filter(id_group='1 класс')
    second = group.filter(id_group='2 класс')
    three = group.filter(id_group='3 класс')
    four = group.filter(id_group='4 класс')
    adults = group.filter(id_group='взрослые')
    all_text = SpeedText.objects.all().order_by('name_text') 
    return render(request, 'app_1/speed_read.html', {'all': all_text, 'fi': first, 'se': second,
    'th': three, 'fo': four, 'ad': adults})


def text(request, name_text):
        textik = SpeedText.objects.filter(name_text=name_text)
        data = {
            'x': list(textik.values())
        }
        return JsonResponse(data)


"""END BLOCK №6. Speed of read"""


"""BLOCK №7. Profile of user"""


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')


"""END BLOCK №7. Profile of user"""


"""BLOCK №8. Enty of site"""


class BBLoginView(LoginView):
    template_name = 'registration/login.html'


"""BLOCK №8. Entry of site"""


"""BLOCK №9. Registration"""


class RegisterView(TemplateView):
    template_name = "registration/signup.html"

    def dispatch(self, request, *args, **kwargs):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            password2 = request.POST.get('password2')

            if password == password2:
                User.objects.create_user(username, email, password, is_active=True)
                return redirect(reverse("login"))

        return render(request, self.template_name)


"""END BLOCK №9. Registration"""


"""BLOCK №10. Rewrite profile information"""


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = Profile(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect(reverse("profile"))
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = Profile(instance=request.user.profile)
    return render(request, 'formUser/formUser1.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


"""BLOCK №10. Rewrite profile information"""


"""BLOCK №11. Representation diary"""
@login_required
def diary_user(request):
    user_diary = diary.objects.filter(user=request.user)
    return render(request, 'app_1/r_diary.html', {'diary': user_diary})

"""END BLOCK №11. Representation diary"""


"""BLOCK №12. Rewrite the diary"""
@login_required
def diary_rewrite(request):

    class diaryForm(forms.ModelForm):
        class Meta:
            model = diary
            fields = ('author', 'title', 'start_page', 'end_page', 'date',)
            widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'})
        }
            fields_required = ['author', 'start_page']


            
    form = diaryForm()    
    if request.method == 'POST':
        form = diaryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            print('ОК-1')
            form.save_m2m()
            
            return redirect(reverse("profile"))
        else:
            print('пидор!')
    else:
        user_form = diaryForm()
    return render(request, 'formUser/formUser1.html', {
        'user_form': user_form,
    })


"""END BLOCK №12. Rewrite the diary"""