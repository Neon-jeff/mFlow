from django.shortcuts import redirect


def redirect_dashboard(func):
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return func(request,*args,**kwargs)
    return wrapper



def check_onboarding(func):
    def wrapper(request,*args,**kwargs):
        if request.user.profile.email_verified==False:
            return redirect('verify-email')
        if request.user.profile.onboarding_complete==False:
            return redirect('choose')
        if request.user.profile.account_type=='affiliate':
            if len(request.user.subscription.all())==0:
                return redirect('subscribe')
            if request.user.subscription.all()[0].verified==False:
                return redirect ('success')
        if request.user.profile.account_type=='vendor':
            if len(request.user.vendor_subscription.all())==0:
                return redirect('subscribe-vendor')
            if request.user.vendor_subscription.all()[0].verified==False:
                return redirect ('success')        
        return func(request,*args, **kwargs)
    return wrapper