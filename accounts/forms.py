from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User, Participant
from django.db import transaction


class ParticipantSignUpForm(UserCreationForm):
    participant_avatar = forms.ImageField(required=False,
                                          widget=forms.FileInput(attrs={'class': 'w3-input w3-border'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    password1 = forms.CharField(required=True,
                                label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border'}))
    password2 = forms.CharField(required=True,
                                label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border'}))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    email = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    phone = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    gender_choices = {
        ('male', 'male'),
        ('female', 'female'),
    }
    gender = forms.ChoiceField(choices=gender_choices,
                               label="Gender",
                               initial='',
                               widget=forms.Select(attrs={'class': 'w3-input w3-border'}),
                               required=True)
    birth_date = forms.DateField(label='What is your birth date?',
                                 widget=forms.NumberInput(attrs={'class': 'w3-input w3-border',
                                                                 'type': 'date'}))

    # Address info
    city_province = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,
                                                           'class': 'w3-input w3-border'}))
    # other info
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_participant = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        participant = Participant.objects.create(user=user)
        participant.participant_avatar = self.cleaned_data.get('participant_avatar')
        participant.phone = self.cleaned_data.get('phone')
        participant.gender = self.cleaned_data.get('gender')
        participant.birth_date = self.cleaned_data.get('birth_date')
        participant.city_province = self.cleaned_data.get('city_province')
        participant.address = self.cleaned_data.get('address')
        participant.occupation = self.cleaned_data.get('occupation')
        participant.save()
        return user


class ParticipantUpdateForm(UserCreationForm):
    participant_avatar = forms.ImageField(required=False,
                                          widget=forms.FileInput(attrs={'class': 'w3-input w3-border'}))
    username = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    password1 = forms.CharField(required=True,
                                label="Password",
                                widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border'}))
    password2 = forms.CharField(required=True,
                                label="Confirm Password",
                                widget=forms.PasswordInput(attrs={'class': 'w3-input w3-border'}))
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    email = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    phone = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    gender_choices = {
        ('male', 'male'),
        ('female', 'female'),
    }
    gender = forms.ChoiceField(choices=gender_choices,
                               label="Gender",
                               initial='',
                               widget=forms.Select(attrs={'class': 'w3-input w3-border'}),
                               required=True)
    birth_date = forms.DateField(label='What is your birth date?',
                                 widget=forms.NumberInput(attrs={'class': 'w3-input w3-border',
                                                                 'type': 'date'}))

    # Address info
    city_province = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'rows': 3,
                                                           'class': 'w3-input w3-border'}))
    # other info
    occupation = forms.CharField(widget=forms.TextInput(attrs={'class': 'w3-input w3-border'}))

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_participant = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.save()
        participant = Participant.objects.create(user=user)
        participant.participant_avatar = self.cleaned_data.get('participant_avatar')
        participant.phone = self.cleaned_data.get('phone')
        participant.gender = self.cleaned_data.get('gender')
        participant.birth_date = self.cleaned_data.get('birth_date')
        participant.city_province = self.cleaned_data.get('city_province')
        participant.address = self.cleaned_data.get('address')
        participant.occupation = self.cleaned_data.get('occupation')
        participant.save()
        return user