from accounts.models import Constants, User
from decision.tasks import message
from decision.models import Decision, Recommendation
from django import forms 



class DecisionForm(forms.ModelForm):
    class Meta:
        model = Decision
        fields = '__all__'
    def save(self, commit=True):
        data = self.cleaned_data  
        for user in data['responsible']:
            instance = super().save(commit=commit)
            
            txt= Constants.objects.get(title="message")
            t=f"""
            {txt.text}
            http://194.233.163.50:8006/meeting/{instance.meettings.uuid}/{instance.id}
            """
            re=message.delay(user.telegram_user   ,t)
            re.get()
        for user in data['trailing']:
            txt= Constants.objects.get(title="message2")
            t=f"""
            {txt.text}
            http://194.233.163.50:8006/meeting/{instance.meettings.uuid}/{instance.id}
            """
     
            re=message.delay(user.telegram_user   ,t)
            re.get()
        return instance
    
class RecForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'
    def save(self, commit=True):
        users = User.objects.all()
        instance = super().save(commit=commit)

        for user in users:
            txt= Constants.objects.get(title="tawsia")
            t=f"""
            {txt.text}
            http://194.233.163.50:8006/recs/{instance.uuid}
            """
            re=message.delay(user.telegram_user   ,t)
            re.get()
        return instance
    