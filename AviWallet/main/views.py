from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib.auth.models import User

from .models import Users, Wallet, History

from .forms import UserForm, UserLoginForm, WalletForm,HistoryForm
from django.contrib.auth import authenticate
import logging
import random
from datetime import datetime

id_login = ''

def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')

def community(request):
    return render(request, 'main/community.html')

def profile(request):

    page = 'wallet'
    error = ''
    username = request.user.username

    if (username == ''):
        return redirect('login')

    user = Users.objects.filter(email=username)
    if len(user) == 0:
        return redirect('login')
    id = user[0].id
    data = Wallet.objects.filter(user_id=id)

    Wallet_User = data[0].wallet
    Wallet_Tron = data[0].Tron
    Wallet_Avira = data[0].Avira
    Wallet_USDT = data[0].USDT

    if request.method == 'POST':
        TokenName = request.POST['SelectToken']
        WalletIn = request.POST['Inputwallet']
        CountToken = request.POST['Inputcount']

        IsWallet = Wallet.objects.filter(wallet=WalletIn)

        try:
            CountToken = float(CountToken)
        except ValueError:
            CountToken = -1

        logging.warning('tokens - ' + str(CountToken))

        if (type(CountToken) == str):
            logging.warning(type(CountToken) == str)
            CountToken = -3

        if(len(IsWallet) != 0 ):
            IsWallet_id = IsWallet[0].user_id
            IsWallet_Tron = IsWallet[0].Tron
            IsWallet_Avira = IsWallet[0].Avira
            IsWallet_USDT = IsWallet[0].USDT
            logging.warning(str(Wallet_Tron))

        if (float(CountToken) * 0.1 > Wallet_Tron):
            CountToken = -4

        if (TokenName == 'Avira' and CountToken > float(Wallet_Avira)):
            CountToken = -2
        elif (TokenName == 'USDT' and CountToken > float(Wallet_USDT)):
            CountToken = -2
        elif (TokenName == 'Tron' and CountToken > float(Wallet_Tron)):
            CountToken = -2

        if (len(IsWallet) != 0 and int(CountToken) > 0 and float(CountToken) * 0.1 <= Wallet_Tron):

            logging.warning(IsWallet)

            #logging.warning('tokens - ' + CountToken)

            walletNew = Wallet(user_id=int(IsWallet_id))  # ИД страницы, которую надо обновить

            walletNew.Avira = IsWallet_Avira
            walletNew.USDT = IsWallet_USDT
            walletNew.Tron = IsWallet_Tron

            if(TokenName == 'Avira'):
                walletNew.Avira = float(float(IsWallet_Avira) + float(CountToken))
            elif(TokenName == 'USDT'):
                walletNew.USDT = float(float(IsWallet_USDT) + float(CountToken))
            elif (TokenName == 'Tron'):
                walletNew.Tron = float(float(IsWallet_Tron) + float(CountToken))



            walletNew.wallet = str(WalletIn)
            walletNew.save()

            #UserWallet
            walletNew = Wallet(user_id=int(id))  # ИД страницы, которую надо обновить

            walletNew.Avira = Wallet_Avira
            walletNew.USDT = Wallet_USDT
            walletNew.Tron = Wallet_Tron

            if (TokenName == 'Avira'):
                walletNew.Avira = float(float(Wallet_Avira) - float(CountToken))
            elif (TokenName == 'USDT'):
                walletNew.USDT = float(float(Wallet_USDT) - float(CountToken))
            elif (TokenName == 'Tron'):
                walletNew.Tron = float(float(Wallet_Tron) - float(CountToken))

            walletNew.Tron = float(float(Wallet_Tron) - (float(CountToken) * 0.1))
            walletNew.wallet = str(Wallet_User)
            walletNew.save()

            error = 'Good!'
            page = 'transactoin'

            current_datetime = datetime.now()

            fields = {'wallet': WalletIn, 'DateTime': current_datetime, 'user': id, 'count': str(CountToken) + " " + TokenName}

            form = HistoryForm(fields)

            form.save()

        else:
            page = 'transactoin'
            if(len(IsWallet) == 0):
                error = 'no wallet in base'
            elif(CountToken == -4):
                error = 'No Tron'
            elif (CountToken == -2):
                error = 'No Tokens'
            elif (CountToken == -3):
                error = 'fake sum'

    logging.warning('pafe - ' + page)
    #logging.warning(data[0].wallet)

    wallet_short = data[0].wallet + ''
    wallet_short = wallet_short[0:15] + "..."

    USD = data[0].Avira * 3.2

    history = History.objects.filter(user_id=id)

    typetoken = ''
    wallet = ''
    count = ''
    data = {
        'error': error,
        'typetoken': typetoken,
        'count': count,
        'wallet': data[0].wallet,
        'wallet_short': wallet_short,
        'Tron': toFixed(Wallet_Tron,2),
        'Avira': toFixed(Wallet_Avira,2),
        'USDT': toFixed(Wallet_USDT,2),
        'USD': toFixed(USD,2),
        'page': page,
        'history': history
    }

    return render(request, 'main/profile.html',data)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

def transactoin(request):


    return render(request, 'main/index.html')

def register(request):
    return render(request, 'main/register.html')

def miner(request):
    return render(request, 'main/miner.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid() and request.POST['g-recaptcha-response'] != '':

            user = User.objects.create_user(request.POST['email'], 'myemail@crazymail.com', request.POST['password'])
            user.first_name = request.POST['name']
            user.save()

            form.save()

            new_user = Users.objects.filter(email=request.POST['email']);

            logging.warning(new_user[0].id)
            id = new_user[0].id

            bits = random.getrandbits(256)
            wallet = hex(bits)

            fields = {'user': id,'wallet': wallet, 'Tron': 0, 'Avira': 0, 'USDT':0}

            form = WalletForm(fields)

            form.save()

            return redirect('general')
        else:
            if request.POST['g-recaptcha-response'] == '':
                error = 'Капча не вирішена'
            else:
                error = 'Заповнено не вірно'

    form = UserForm()

    data = {
        'form':form,
        'error': error
    }

    return render(request, 'main/register.html', data)


def login_in(request):
    error = ''

    if request.method == 'POST':
        logging.warning(request.POST['g-recaptcha-response'])
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=request.POST['email'], password=request.POST['password'])
            if user is not None and request.POST['g-recaptcha-response'] != '':
                auth.login(request, user)
                return redirect('general')
            else:
                if request.POST['g-recaptcha-response'] == '':
                    error = 'Капча не вирішена'
                else:
                    error = 'Заповнено не вірно'

    form = UserLoginForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'main/login.html', data)
