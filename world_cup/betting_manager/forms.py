from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from .models import Team,MatchGroupStageBetting,MatchFinalStageRealSixteen\
,MatchFinalStageRealEight,MatchFinalStageRealFour,MatchFinalStageRealFinal \
    ,MatchFinalStageBettingSixteen,MatchFinalStageBettingEight\
    ,MatchFinalStageBettingFour,MatchFinalStageBettingFinal

class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ['name','group']

class BettingForm(ModelForm):
    class Meta:
        model = MatchGroupStageBetting
        fields = "__all__"
        exclude = ['person_betting']


class BettingSixteenForm(ModelForm):
    class Meta:
        model = MatchFinalStageBettingSixteen
        fields = "__all__"
        exclude = ['person_betting']


class BettingEightForm(ModelForm):
    class Meta:
        model = MatchFinalStageBettingEight
        fields = "__all__"
        exclude = ['person_betting']


class BettingFourForm(ModelForm):
    class Meta:
        model = MatchFinalStageBettingFour
        fields = "__all__"
        exclude = ['person_betting']


class BettingFinalForm(ModelForm):
    class Meta:
        model = MatchFinalStageBettingFinal
        fields = "__all__"
        exclude = ['person_betting']


class MatchSixteenForm(ModelForm):
    class Meta:
        model = MatchFinalStageRealSixteen
        fields = "__all__"


class MatchEightForm(ModelForm):
    class Meta:
        model = MatchFinalStageRealEight
        fields = "__all__"


class MatchFourForm(ModelForm):
    class Meta:
        model = MatchFinalStageRealFour
        fields = "__all__"


class MatchFinalForm(ModelForm):
    class Meta:
        model = MatchFinalStageRealFinal
        fields = "__all__"
