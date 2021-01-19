from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Player(models.Model):

    user = models.OneToOneField(User,null=True,blank=True,on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    nailing = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Team(models.Model):

    GROUP = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('H', 'H')
    )

    name = models.CharField(max_length=20, null=True)
    group = models.CharField(max_length=1, null=True, choices=GROUP)
    points = models.IntegerField(default=0)


    def __str__(self):
        return self.name

class MatchGroupStageReal(models.Model):

    GOALS = list(zip(range(0,11),range(0,11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DRAW', 'DRAW'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_group')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_group')
    goals_team_one = models.IntegerField(null=True,choices=GOALS)
    goals_team_two = models.IntegerField(null=True,choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    stage = models.CharField(max_length=6,null=True,choices=STAGE)
    played = models.CharField(max_length=3,null=True,choices=STATUS)

    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)

class MatchGroupStageBetting(models.Model):

    GOALS = list(zip(range(0,11),range(0,11)))


    RESULTS = (
        ('WIN', 'WIN'),
        ('DRAW', 'DRAW'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ("YES",'YES'),
        ("NO", 'NO')
    )

    person_betting = models.ForeignKey(Player,null=True,on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0,choices=GOALS)
    goals_team_two = models.IntegerField(default=0,choices=GOALS)
    score_team_one = models.CharField(max_length=6,null=True,choices=RESULTS)
    score_team_two = models.CharField(max_length=6,null=True,choices=RESULTS)
    match = models.ForeignKey(MatchGroupStageReal,null=True, on_delete=models.SET_NULL)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3,null=True, choices=STATUS)


    def __str__(self):
        return str(self.match.team_one.name) + " : " +  str(self.match.team_two.name)+ " - " \
               + str(self.person_betting.user.username)


class MatchFinalStageReal(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_final')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_final')
    goals_team_one = models.IntegerField(null=True, choices=GOALS)
    goals_team_two = models.IntegerField(null=True, choices=GOALS)
    penalties_team_one = models.CharField(max_length=1, null=True, choices=GOALS)
    penalties_team_two = models.CharField(max_length=1, null=True, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    played = models.CharField(max_length=3,null=True,choices=STATUS)


    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)



class MatchFinalStageBetting(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    person_betting = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0, choices=GOALS)
    goals_team_two = models.IntegerField(default=0, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    match = models.ForeignKey(MatchFinalStageReal, null=True, on_delete=models.SET_NULL)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3,null=True, choices=STATUS)

    def __str__(self):
        return str(self.match) + " - " + str(self.person_betting.user.username)


class MatchFinalStageRealSixteen(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_final_sixteen')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_final_sixteen')
    goals_team_one = models.IntegerField(null=True, choices=GOALS)
    goals_team_two = models.IntegerField(null=True, choices=GOALS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    stage = models.CharField(max_length=6, null=True, choices=STAGE)
    played = models.CharField(max_length=3, null=True, choices=STATUS)

    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)

class MatchFinalStageBettingSixteen(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    person_betting = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0, choices=GOALS)
    goals_team_two = models.IntegerField(default=0, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    match = models.ForeignKey(MatchFinalStageRealSixteen, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3, null=True, choices=STATUS)

    def __str__(self):
        return str(self.match) + " - " + str(self.person_betting.user.username)


class MatchFinalStageRealEight(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_final_eight')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_final_eight')
    goals_team_one = models.IntegerField(null=True, choices=GOALS)
    goals_team_two = models.IntegerField(null=True, choices=GOALS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    stage = models.CharField(max_length=6, null=True, choices=STAGE)
    played = models.CharField(max_length=3,null=True,choices=STATUS)


    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)



class MatchFinalStageBettingEight(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    person_betting = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0, choices=GOALS)
    goals_team_two = models.IntegerField(default=0, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    match = models.ForeignKey(MatchFinalStageRealEight, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3,null=True, choices=STATUS)

    def __str__(self):
        return str(self.match) + " - " + str(self.person_betting.user.username)

class MatchFinalStageRealFour(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_final_four')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_final_four')
    goals_team_one = models.IntegerField(null=True, choices=GOALS)
    goals_team_two = models.IntegerField(null=True, choices=GOALS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    stage = models.CharField(max_length=6, null=True, choices=STAGE)
    played = models.CharField(max_length=3,null=True,choices=STATUS)


    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)



class MatchFinalStageBettingFour(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    person_betting = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0, choices=GOALS)
    goals_team_two = models.IntegerField(default=0, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    match = models.ForeignKey(MatchFinalStageRealFour, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3,null=True, choices=STATUS)

    def __str__(self):
        return str(self.match) + " - " + str(self.person_betting.user.username)


class MatchFinalStageRealFinal(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    STAGE = (
        ('GROUP', 'GROUP'),
        ('BEST16', 'BEST16'),
        ('QF', 'QF'),
        ('SF', 'SF'),
        ('F', 'F')
    )

    team_one = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_one_final_championship')
    team_two = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL, related_name='team_two_final_championship')
    goals_team_one = models.IntegerField(null=True, choices=GOALS)
    goals_team_two = models.IntegerField(null=True, choices=GOALS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    stage = models.CharField(max_length=6, null=True, choices=STAGE)
    played = models.CharField(max_length=3,null=True,choices=STATUS)


    def __str__(self):
        return str(self.team_one.name) + " : " + str(self.team_two.name)



class MatchFinalStageBettingFinal(models.Model):
    GOALS = list(zip(range(0, 11), range(0, 11)))

    RESULTS = (
        ('WIN', 'WIN'),
        ('DEFEAT', 'DEFEAT')
    )

    STATUS = (
        ('YES', 'YES'),
        ('NO', 'NO'),
    )

    person_betting = models.ForeignKey(Player, null=True, on_delete=models.SET_NULL)
    goals_team_one = models.IntegerField(default=0, choices=GOALS)
    goals_team_two = models.IntegerField(default=0, choices=GOALS)
    score_team_one = models.CharField(max_length=6, null=True, choices=RESULTS)
    score_team_two = models.CharField(max_length=6, null=True, choices=RESULTS)
    penalties_team_one = models.IntegerField(null=True, choices=GOALS)
    penalties_team_two = models.IntegerField(null=True, choices=GOALS)
    match = models.ForeignKey(MatchFinalStageRealFinal, null=True, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    checked = models.CharField(max_length=3,null=True, choices=STATUS)

    def __str__(self):
        return str(self.match) + " - " + str(self.person_betting.user.username)
