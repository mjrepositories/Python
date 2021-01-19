from django.shortcuts import render,redirect,reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Team,MatchGroupStageReal,Player,MatchGroupStageBetting,MatchFinalStageRealSixteen\
,MatchFinalStageRealEight,MatchFinalStageRealFour,MatchFinalStageRealFinal \
    ,MatchFinalStageBettingSixteen,MatchFinalStageBettingEight\
    ,MatchFinalStageBettingFour,MatchFinalStageBettingFinal
from .forms import BettingForm,MatchSixteenForm,MatchEightForm,MatchFourForm,MatchFinalForm,BettingSixteenForm\
    ,BettingEightForm,BettingFourForm,BettingFinalForm
from django.contrib.auth import authenticate, login
from django.db.models import Q
from django.forms import formset_factory

# Create your views here.

def home_view(request):
    # rendering home page
    return render(request, 'betting_manager/home_page.html')


def register(request):
    # if method is POST
    if request.method == "POST":
        # passing data for user to user form
        form = UserCreationForm(request.POST)
        # if form is valid
        if form.is_valid():
            # creating user
            form.save()
            messages.success(request,f'Account was successfully created for you')
            print(request.POST)
            # authenticating newly created user into app
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            # logging with authentication
            login(request, new_user)
            # getting person
            person = Player.objects.get(user=request.user)
            # getting all real matches for groups
            matches = MatchGroupStageReal.objects.all()
            # looping over all group matches
            for x in matches:
                # creating initial data
                data = {'person_betting': person, "match": x, 'goals_team_one': 0,
                        'goals_team_two': 0, 'score_team_one': 'DRAW', 'score_team_two': 'DRAW',
                        'points': 0, 'checked': 'NO'}
                # creating instance with initial data
                match_to_bet = MatchGroupStageBetting(**data)
                # saving created bet
                match_to_bet.save()
            # redirecting to home page
            return redirect('home-page')

    else:
        # initiating form
        form = UserCreationForm()
        # sending form to context for rendering
        context = {'form': form}
    return render(request, 'betting_manager/register.html', context)


def about(request):
    # rendering page with information about game
    return render(request,'betting_manager/about.html')


def results(request):
    # getting all players
    people = Player.objects.all()
    # creating dictionary for players and their results
    players_and_scores = {}
    # looping over all players
    for person in people:
        # assigning initial data for each player
        players_and_scores[str(person)]={'points':0,'nailing':0, 'correct':0}
        print(players_and_scores)
        # filtering bets - all not  checked, played and for specific person
        matches_bet = MatchGroupStageBetting.objects.filter(Q(checked="NO")&Q(match__played='YES')&Q(person_betting=person))
        print("what we played",matches_bet)
        if matches_bet:
            # looping over filtered matches for checking
            for game_played in matches_bet:
                # assigning goals and scores
                goal_real_team_one = game_played.match.goals_team_one
                goal_real_team_two = game_played.match.goals_team_two
                goal_bet_team_one = game_played.goals_team_one
                goal_bet_team_two = game_played.goals_team_two
                score_real_team_one = game_played.match.score_team_one
                score_bet_team_one = game_played.score_team_one
                # if score is the same for bet and matched played
                if score_real_team_one == score_bet_team_one:
                    # assigning points to person and number for correct bet
                    players_and_scores[str(person)]["points"] +=1
                    players_and_scores[str(person)]["correct"] += 1
                    print(goal_real_team_one,goal_bet_team_one,goal_real_team_two,goal_bet_team_two)
                # if details for match are matching between bet and score
                if (goal_real_team_one == goal_bet_team_one) \
                        and (goal_real_team_two==goal_bet_team_two):
                    # assigning additional points and additional stat for nailing bet
                    players_and_scores[str(person)]["points"] += 4
                    players_and_scores[str(person)]["nailing"] += 1
                # ticking match as checked
                game_played.checked = "YES"
                # saving info that match was checked
                game_played.save()

        # filtering bets - all not  checked, played and for specific person
        matches_bet = MatchFinalStageBettingSixteen.objects.filter(
            Q(checked="NO") & Q(match__played='YES') & Q(person_betting=person))
        print("what we played", matches_bet)
        # if there are matches available for checking
        if matches_bet:
            # looping over filtered matches for checking
            for game_played in matches_bet:
                # assigning goals and scores
                goal_real_team_one = game_played.match.goals_team_one
                goal_real_team_two = game_played.match.goals_team_two
                penalties_real_team_one = game_played.match.penalties_team_one
                penalties_real_team_two = game_played.match.penalties_team_two
                goal_bet_team_one = game_played.goals_team_one
                goal_bet_team_two = game_played.goals_team_two
                penalties_bet_team_one = game_played.penalties_team_one
                penalties_bet_team_two = game_played.penalties_team_two
                score_real_team_one = game_played.match.score_team_one
                score_bet_team_one = game_played.score_team_one
                # if score is the same for bet and matched played
                if score_real_team_one == score_bet_team_one:
                    # assigning points to person and number for correct bet
                    players_and_scores[str(person)]["points"] += 1
                    players_and_scores[str(person)]["correct"] += 1
                    print(goal_real_team_one, goal_bet_team_one, goal_real_team_two, goal_bet_team_two)
                # if details for match are matching between bet and score
                if (goal_real_team_one == goal_bet_team_one) \
                        and (goal_real_team_two == goal_bet_team_two) \
                        and (penalties_real_team_two == penalties_bet_team_two) \
                        and (penalties_real_team_one == penalties_bet_team_one):
                    # assigning additional points and additional stat for nailing bet
                    players_and_scores[str(person)]["points"] += 4
                    players_and_scores[str(person)]["nailing"] += 1
                # ticking match as checked
                game_played.checked = "YES"
                # saving info that match was checked
                game_played.save()

    # filtering bets - all not  checked, played and for specific person
    matches_bet = MatchFinalStageBettingEight.objects.filter(
        Q(checked="NO") & Q(match__played='YES') & Q(person_betting=person))
    print("what we played", matches_bet)
    # if there are matches available for checking
    if matches_bet:
        # looping over filtered matches for checking
        for game_played in matches_bet:
            # assigning goals and scores
            goal_real_team_one = game_played.match.goals_team_one
            goal_real_team_two = game_played.match.goals_team_two
            penalties_real_team_one = game_played.match.penalties_team_one
            penalties_real_team_two = game_played.match.penalties_team_two
            goal_bet_team_one = game_played.goals_team_one
            goal_bet_team_two = game_played.goals_team_two
            penalties_bet_team_one = game_played.penalties_team_one
            penalties_bet_team_two = game_played.penalties_team_two
            score_real_team_one = game_played.match.score_team_one
            score_bet_team_one = game_played.score_team_one
            # if score is the same for bet and matched played
            if score_real_team_one == score_bet_team_one:
                # assigning points to person and number for correct bet
                players_and_scores[str(person)]["points"] += 1
                players_and_scores[str(person)]["correct"] += 1
                print(goal_real_team_one, goal_bet_team_one, goal_real_team_two, goal_bet_team_two)
                # if details for match are matching between bet and score
            if (goal_real_team_one == goal_bet_team_one) \
                    and (goal_real_team_two == goal_bet_team_two) \
                    and (penalties_real_team_two == penalties_bet_team_two) \
                    and (penalties_real_team_one == penalties_bet_team_one):
                # assigning additional points and additional stat for nailing bet
                players_and_scores[str(person)]["points"] += 4
                players_and_scores[str(person)]["nailing"] += 1

            # ticking match as checked
            game_played.checked = "YES"
            # saving info that match was checked
            game_played.save()

    # filtering bets - all not  checked, played and for specific person
    matches_bet = MatchFinalStageBettingFour.objects.filter(
        Q(checked="NO") & Q(match__played='YES') & Q(person_betting=person))
    print("what we played", matches_bet)
    # if there are matches available for checking
    if matches_bet:
        # looping over filtered matches for checking
        for game_played in matches_bet:
            # assigning goals and scores
            goal_real_team_one = game_played.match.goals_team_one
            goal_real_team_two = game_played.match.goals_team_two
            penalties_real_team_one = game_played.match.penalties_team_one
            penalties_real_team_two = game_played.match.penalties_team_two
            goal_bet_team_one = game_played.goals_team_one
            goal_bet_team_two = game_played.goals_team_two
            penalties_bet_team_one = game_played.penalties_team_one
            penalties_bet_team_two = game_played.penalties_team_two
            score_real_team_one = game_played.match.score_team_one
            score_bet_team_one = game_played.score_team_one
            # if score is the same for bet and matched played
            if score_real_team_one == score_bet_team_one:
                # assigning points to person and number for correct bet
                players_and_scores[str(person)]["points"] += 1
                players_and_scores[str(person)]["correct"] += 1
                print(goal_real_team_one, goal_bet_team_one, goal_real_team_two, goal_bet_team_two)
            # if details for match are matching between bet and score
            if (goal_real_team_one == goal_bet_team_one) \
                    and (goal_real_team_two == goal_bet_team_two) \
                    and (penalties_real_team_two == penalties_bet_team_two) \
                    and (penalties_real_team_one == penalties_bet_team_one):
                # assigning additional points and additional stat for nailing bet
                players_and_scores[str(person)]["points"] += 4
                players_and_scores[str(person)]["nailing"] += 1

            # ticking match as checked
            game_played.checked = "YES"
            # saving info that match was checked
            game_played.save()

    # filtering bets - all not  checked, played and for specific person
    matches_bet = MatchFinalStageBettingFinal.objects.filter(
        Q(checked="NO") & Q(match__played='YES') & Q(person_betting=person))
    print("what we played", matches_bet)
    # if there are matches available for checking
    if matches_bet:
        # looping over filtered matches for checking
        for game_played in matches_bet:
            # assigning goals and scores
            goal_real_team_one = game_played.match.goals_team_one
            goal_real_team_two = game_played.match.goals_team_two
            penalties_real_team_one = game_played.match.penalties_team_one
            penalties_real_team_two = game_played.match.penalties_team_two
            goal_bet_team_one = game_played.goals_team_one
            goal_bet_team_two = game_played.goals_team_two
            penalties_bet_team_one = game_played.penalties_team_one
            penalties_bet_team_two = game_played.penalties_team_two
            score_real_team_one = game_played.match.score_team_one
            score_bet_team_one = game_played.score_team_one
            # if score is the same for bet and matched played
            if score_real_team_one == score_bet_team_one:
                # assigning points to person and number for correct bet
                players_and_scores[str(person)]["points"] += 1
                players_and_scores[str(person)]["correct"] += 1
                print(goal_real_team_one, goal_bet_team_one, goal_real_team_two, goal_bet_team_two)
            # if details for match are matching between bet and score
            if (goal_real_team_one == goal_bet_team_one) \
                    and (goal_real_team_two == goal_bet_team_two) \
                    and (penalties_real_team_two == penalties_bet_team_two) \
                    and (penalties_real_team_one == penalties_bet_team_one):
                # assigning additional points and additional stat for nailing bet
                players_and_scores[str(person)]["points"] += 4
                players_and_scores[str(person)]["nailing"] += 1

            # ticking match as checked
            game_played.checked = "YES"
            # saving info that match was checked
            game_played.save()

    # looping over all players and there scores checked
    for player in players_and_scores:
        # getting the profile
        account = Player.objects.get(user__username=player)
        # assigning values for points, nails and correct bets to profile
        account.points += players_and_scores[str(player)]["points"]
        account.nailing += players_and_scores[str(player)]["nailing"]
        account.correct += players_and_scores[str(player)]["correct"]
        # saving profile
        account.save()

    # creating ranking dictionary
    ranking = {}
    # getting all players
    all_players = Player.objects.all()
    # looping over all players
    for better in all_players:
        # assigning data to each player in dictionary
        ranking[str(better)] ={'points':better.points,'nailing':better.nailing,'correct':better.correct}
    print(ranking)

    # sorting results based on points, nails and then correct bets
    ranking = {k:v for k,v in sorted(ranking.items(),key=lambda item: (item[1]['points'],
                                                                 item[1]['nailing'],
                                                                item[1]['correct']), reverse=True)}

    # getting all players
    players_betting = [k for k in ranking.keys()]
    # looping over players
    for x, who in enumerate(players_betting, 1):
        # assigning position to a player
        ranking[who]['position'] = x
    # passing ranking to context for rendering
    context = {'players':ranking}
    return render(request,'betting_manager/results.html',context)


def groups(request, group_value):
    # getting person
    person = Player.objects.get(user=request.user)
    # getting teams for specific group
    teams = Team.objects.filter(group=group_value)
    print(teams)
    # getting teams names
    teams_names = [x.name for x in teams]
    # getting matches for betting in a group
    matches_bet = MatchGroupStageBetting.objects.filter(Q(match__team_one__in=teams)&Q(person_betting=person))
    # getting matches for a group
    matches = MatchGroupStageReal.objects.filter(team_one__in=teams)
    print('matches from betting',matches_bet)
    print('standard matches',matches)
    print(matches)

    # filtering matches played
    played_matches = MatchGroupStageReal.objects.filter(played='YES')
    # filtering matches for a group
    played_matches = played_matches.filter(team_one__group=group_value)
    print(played_matches)
    # creating counter for points
    points_counter={}
    # looping through all teams
    for team in teams_names:
        # assigning initial values for results
        points_counter[team] = {}
        points_counter[team]['points'] = 0
        points_counter[team]['scored'] = 0
        points_counter[team]['lost'] = 0


    # looping over all matches for a group
    for match in played_matches:
        print(match.team_one,list(points_counter.keys()))
        # if team one won
        if match.score_team_one == 'WIN':
            # assigning points, goals scored and lost
            points_counter[str(match.team_one)]['points'] += 3
            points_counter[str(match.team_one)]['scored'] += match.goals_team_one
            points_counter[str(match.team_one)]['lost'] += match.goals_team_two
            points_counter[str(match.team_two)]['points'] += 0
            points_counter[str(match.team_two)]['scored'] += match.goals_team_two
            points_counter[str(match.team_two)]['lost'] += match.goals_team_one
        # if there was draw
        elif match.score_team_one == 'DRAW':
            # assigning points, goals scored and lost
            points_counter[str(match.team_one)]['points'] += 1
            points_counter[str(match.team_one)]['scored'] += match.goals_team_one
            points_counter[str(match.team_one)]['lost'] += match.goals_team_two
            points_counter[str(match.team_two)]['points'] += 1
            points_counter[str(match.team_two)]['scored'] += match.goals_team_two
            points_counter[str(match.team_two)]['lost'] += match.goals_team_one
        # if team one lost
        else:
            # assigning points, goals scored and lost
            points_counter[str(match.team_one)]['points'] += 0
            points_counter[str(match.team_one)]['scored'] += match.goals_team_one
            points_counter[str(match.team_one)]['lost'] += match.goals_team_two
            points_counter[str(match.team_two)]['points'] += 3
            points_counter[str(match.team_two)]['scored'] += match.goals_team_two
            points_counter[str(match.team_two)]['lost'] += match.goals_team_one
    # sorting based on number of points
    points_counter = {k:v for k,v in sorted(points_counter.items(),key=lambda item: item[1]['points'], reverse=True)}
    # getting team names
    teams_names = [k for k in points_counter.keys()]
    # looping over all teams
    for x,team in enumerate(teams_names,1):
        #assigning positions
        points_counter[team]['position'] = x


    # passing data to context - matches and details on results
    context = {'teams': points_counter, "matches":matches_bet}
    return render(request, 'betting_manager/group.html', context)


def betting(request, match, stage):
    print(stage)
    # getting person
    person = Player.objects.get(user=request.user)
    # checking stage
    if stage == 'GROUP':
        # filtering match for stage
        game = MatchGroupStageBetting.objects.get(Q(person_betting=person) & Q(match=match))
        print(stage)
        # if match is not played
        if game.match.played == "NO":
            # getting real match for group checking
            scrimmage = MatchGroupStageReal.objects.get(id=match)
            # checking group
            group = scrimmage.team_one.group
            print(scrimmage)
            # if method is POST
            if request.method == "POST":
                # fill in form with instance of filtered match
                form = BettingForm(request.POST, instance=game)
                # if form is valid
                if form.is_valid():
                    print(request.POST)
                    # create instance of bet without saving
                    instance = form.save(commit=False)
                    print("Person betting is", instance.person_betting)
                    # saving instance of object
                    instance.save()
                    # redirecting to stage
                    return redirect('groups', group_value=group)
                    print('redirected')
                else:
                    print(form.errors)
            else:
                # filling in form with instance of a match
                form = BettingForm(instance=game)
            # passing form and match to context for rendering
            context = {'form': form, 'match': scrimmage}
            return render(request, 'betting_manager/group_betting.html', context)
        else:
            # redirecting because changes are not allowed
            return redirect('not_allowed')

    # checking stage
    elif stage == 'BEST16':
        # filtering match for stage
        game = MatchFinalStageBettingSixteen.objects.get(Q(person_betting=person) & Q(match=match))
        print(stage)
        # if match is not played
        if game.match.played == "NO":
            # getting real match
            scrimmage = MatchFinalStageRealSixteen.objects.get(id=match)
            print(scrimmage)
            # if method is POST
            if request.method == "POST":
                # fill in form with instance of filtered match
                form = BettingSixteenForm(request.POST, instance=game)
                # if form is valid
                if form.is_valid():
                    print(request.POST)
                    # create instance of bet without saving
                    instance = form.save(commit=False)
                    print("Person betting is", instance.person_betting)
                    # saving instance of object
                    instance.save()
                    # redirecting to stage
                    return redirect('sweet_16')
                    print('redirected')
                else:
                    print(form.errors)
            else:
                # filling in form with instance of a match
                form = BettingSixteenForm(instance=game)
            # passing form and match to context for rendering
            context = {'form': form, 'match': scrimmage}
            return render(request, 'betting_manager/group_betting.html', context)
        else:
            # redirecting because changes are not allowed
            return redirect('not_allowed')

    # checking stage
    elif stage == 'QF':
        # filtering match for stage
        game = MatchFinalStageBettingEight.objects.get(Q(person_betting=person) & Q(match=match))
        print(stage)
        # if match is not played
        if game.match.played == "NO":
            # getting real match
            scrimmage = MatchFinalStageRealEight.objects.get(id=match)
            print(scrimmage)
            # if method is POST
            if request.method == "POST":
                # fill in form with instance of filtered match
                form = BettingEightForm(request.POST, instance=game)
                # if form is valid
                if form.is_valid():
                    print(request.POST)
                    # create instance of bet without saving
                    instance = form.save(commit=False)
                    print("Person betting is", instance.person_betting)
                    # saving instance of object
                    instance.save()
                    # redirecting to stage
                    return redirect('elite_8')
                    print('redirected')
                else:
                    print(form.errors)
            else:
                # filling in form with instance of a match
                form = BettingEightForm(instance=game)
            # passing form and match to context for rendering
            context = {'form': form, 'match': scrimmage}

            return render(request, 'betting_manager/group_betting.html', context)
        else:
            # redirecting because changes are not allowed
            return redirect('not_allowed')

    # checking stage
    elif stage == 'SF':
        # filtering match for stage
        game = MatchFinalStageBettingFour.objects.get(Q(person_betting=person) & Q(match=match))
        print(stage)
        # if match is not played
        if game.match.played == "NO":
            # getting real match
            scrimmage = MatchFinalStageRealFour.objects.get(id=match)
            print(scrimmage)
            # if method is POST
            if request.method == "POST":
                # fill in form with instance of filtered match
                form = BettingFourForm(request.POST, instance=game)
                # if form is valid
                if form.is_valid():
                    print(request.POST)
                    # create instance of bet without saving
                    instance = form.save(commit=False)
                    print("Person betting is", instance.person_betting)
                    # saving instance of object
                    instance.save()
                    # redirecting to stage
                    return redirect('final_4')
                    print('redirected')
                else:
                    print(form.errors)
            else:
                # filling in form with instance of a match
                form = BettingFourForm(instance=game)
            # passing form and match to context for rendering
            context = {'form': form, 'match': scrimmage}
            return render(request, 'betting_manager/group_betting.html', context)
        else:
            # redirecting because changes are not allowed
            return redirect('not_allowed')

    # checking stage
    elif stage == 'F':
        # filtering match for stage
        game = MatchFinalStageBettingFinal.objects.get(Q(person_betting=person) & Q(match=match))
        print(stage)
        # if match is not played
        if game.match.played == "NO":
            # getting real match
            scrimmage = MatchFinalStageRealFinal.objects.get(id=match)
            print(scrimmage)
            # if method is POST
            if request.method == "POST":
                # fill in form with instance of filtered match
                form = BettingFinalForm(request.POST, instance=game)
                # if form is valid
                if form.is_valid():
                    print(request.POST)
                    # create instance of bet without saving
                    instance = form.save(commit=False)
                    print("Person betting is", instance.person_betting)
                    # saving instance of object
                    instance.save()
                    return redirect('final_4')
                    # redirecting to stage
                    print('redirected')
                else:
                    print(form.errors)
            else:
                # filling in form with instance of a match
                form = BettingFinalForm(instance=game)
            # passing form and match to context for rendering
            context = {'form': form, 'match': scrimmage}
            return render(request, 'betting_manager/group_betting.html', context)
        else:
            # redirecting because changes are not allowed
            return redirect('not_allowed')


def sweetsixteen(request):
    # filtering person
    person = Player.objects.get(user=request.user)
    # filtering match for current stage
    matches_bet = MatchFinalStageBettingSixteen.objects.filter(person_betting=person)
    if not matches_bet:
        # redirecting to warning
        return redirect('stage_warning')
    # otherwise - passing match to context for rendering
    context = {'matches':matches_bet}
    return render(request,'betting_manager/sweet_16.html',context)

def eliteeight(request):
    # filtering person
    person = Player.objects.get(user=request.user)
    # filtering match for current stage
    matches_bet = MatchFinalStageBettingEight.objects.filter(person_betting=person)
    # if there is no match
    if not matches_bet:
        # redirecting to warning
        return redirect('stage_warning')
    # otherwise - passing match to context for rendering
    context = {'matches': matches_bet}
    return render(request,'betting_manager/elite_8.html',context)

def finalfour(request):
    # filtering person
    person = Player.objects.get(user=request.user)
    # filtering match for current stage
    matches_bet = MatchFinalStageBettingFour.objects.filter(person_betting=person)
    # if there is no match
    if not matches_bet:
        # redirecting to warning
        return redirect('stage_warning')
    # otherwise - passing match to context for rendering
    context = {'matches': matches_bet}
    return render(request,'betting_manager/final_4.html',context)

def championship(request):
    # filtering person
    person = Player.objects.get(user=request.user)
    # filtering match for current stage
    matches_bet = MatchFinalStageBettingFinal.objects.filter(person_betting=person)
    # if there is no match
    if not matches_bet:
        # redirecting to warning
        return redirect('stage_warning')
    # otherwise - passing match to context for rendering
    context = {'matches': matches_bet}
    return render(request,'betting_manager/championship.html',context)

def not_allowed(request):
    # rendering page with warning that changing scores is not allowed
    return render(request,'betting_manager/action_not_allowed.html')

def stage_warning(request):
    # rendering page with warning on unknown matches
    return render(request,'betting_manager/stage_warning.html')

def create_matches(request):
    # creating details on form sets
    sixteenFormSet = formset_factory(MatchSixteenForm,extra=0)
    eightFormSet = formset_factory(MatchEightForm,extra=0)
    fourFormSet = formset_factory(MatchFourForm,extra=0)
    finalFormSet = formset_factory(MatchFinalForm,extra=0)

    # initiating form sets with initial values and their number to be seen on page
    sixteenform = sixteenFormSet(initial=[{'goals_team_one':"0",'goals_team_two': '0','penalties_team_one':'0',
                                           'penalties_team_two':'0','score_team_one':'DEFEAT',
                                           'score_team_two':'DEFEAT','played':'NO','stage':"BEST16"} for _ in range(8)])

    eightform = eightFormSet(initial=[{'goals_team_one': "0", 'goals_team_two': '0', 'penalties_team_one': '0',
                                           'penalties_team_two': '0', 'score_team_one': 'DEFEAT',
                                           'score_team_two': 'DEFEAT', 'played': 'NO','stage':"QF"} for _ in range(4)])

    fourform = fourFormSet(initial=[{'goals_team_one': "0", 'goals_team_two': '0', 'penalties_team_one': '0',
                                           'penalties_team_two': '0', 'score_team_one': 'DEFEAT',
                                           'score_team_two': 'DEFEAT', 'played': 'NO','stage':"SF"} for _ in range(2)])

    finalform = finalFormSet(initial=[{'goals_team_one': "0", 'goals_team_two': '0', 'penalties_team_one': '0',
                                           'penalties_team_two': '0', 'score_team_one': 'DEFEAT',
                                           'score_team_two': 'DEFEAT', 'played': 'NO','stage':"F"} for _ in range(1)])

    # checking if method is post and submit is done for specific form
    if request.method == 'POST' and "Submit_16" in request.POST.keys():
        # passing values from POST to formset
        sixteenform = sixteenFormSet(request.POST)
        print(request.POST)
        # checking if formset is valid
        if  sixteenform.is_valid():
            # looping over all forms in formset
            for form in sixteenform:
                # saving form
                form.save()
            # getting all matches for stage and all players
            matches = MatchFinalStageRealSixteen.objects.all()
            players = Player.objects.all()
            # looping over all new matches and all players to create bets for them
            for match in matches:
                for player in players:
                    data = {'person_betting': player, "match": match, 'goals_team_one': 0,
                            'goals_team_two': 0, 'penalties_team_one': 0, 'penalties_team_two': 0,
                            'score_team_one': 'DEFEAT', 'score_team_two': 'DEFEAT',
                            'points': 0, 'checked': 'NO'}
                    # passing data to create bets
                    match_to_bet = MatchFinalStageBettingSixteen(**data)
                    # saving created custom bets
                    match_to_bet.save()


            print('valid')
        else:
            print(sixteenform.errors)

    # checking if method is post and submit is done for specific form
    elif request.method == 'POST' and "Submit_8" in request.POST.keys():
        # passing values from POST to formset
        eightform = eightFormSet(request.POST)
        print(request.POST)
        # checking if formset is valid
        if  eightform.is_valid():
            # looping over all forms in formset
            for form in eightform:
                # saving form
                form.save()
            # getting all matches for stage and all players
            matches = MatchFinalStageRealEight.objects.all()
            players = Player.objects.all()
            # looping over all new matches and all players to create bets for them
            for match in matches:
                for player in players:
                    data = {'person_betting': player, "match":match, 'goals_team_one': 0,
                            'goals_team_two': 0,'penalties_team_one':0,'penalties_team_two':0,
                            'score_team_one': 'DEFEAT', 'score_team_two': 'DEFEAT',
                            'points': 0, 'checked': 'NO'}
                    # passing data to create bets
                    match_to_bet = MatchFinalStageBettingEight(**data)
                    # saving created custom bets
                    match_to_bet.save()
        else:
            print(eightform.errors)

    # checking if method is post and submit is done for specific form
    elif request.method == 'POST' and "Submit_4" in request.POST.keys():
        # passing values from POST to formset
        fourform = fourFormSet(request.POST)
        print(request.POST)
        # checking if formset is valid
        if fourform.is_valid():
            # looping over all forms in formset
            for form in fourform:
                # saving form
                form.save()
            # getting all matches for stage and all players
            matches = MatchFinalStageRealFour.objects.all()
            players = Player.objects.all()
            # looping over all new matches and all players to create bets for them
            for match in matches:
                for player in players:
                    data = {'person_betting': player, "match": match, 'goals_team_one': 0,
                            'goals_team_two': 0, 'penalties_team_one': 0, 'penalties_team_two': 0,
                            'score_team_one': 'DEFEAT', 'score_team_two': 'DEFEAT',
                            'points': 0, 'checked': 'NO'}
                    # passing data to create bets
                    match_to_bet = MatchFinalStageBettingFour(**data)
                    # saving created custom bets
                    match_to_bet.save()
        else:
            print(fourform.errors)

    # checking if method is post and submit is done for specific form
    elif request.method == 'POST' and "Submit_final" in request.POST.keys():
        # passing values from POST to formset
        finalform = finalFormSet(request.POST)
        print(request.POST)
        # checking if formset is valid
        if  finalform.is_valid():
            # looping over all forms in formset
            for form in finalform:
                # saving form
                form.save()
            # getting all matches for stage and all players
            matches = MatchFinalStageRealFinal.objects.all()
            players = Player.objects.all()
            # looping over all new matches and all players to create bets for them
            for match in matches:
                for player in players:
                    data = {'person_betting': player, "match": match, 'goals_team_one': 0,
                            'goals_team_two': 0, 'penalties_team_one': 0, 'penalties_team_two': 0,
                            'score_team_one': 'DEFEAT', 'score_team_two': 'DEFEAT',
                            'points': 0, 'checked': 'NO'}
                    # passing data to create bets
                    match_to_bet = MatchFinalStageBettingFinal(**data)
                    # saving created custom bets
                    match_to_bet.save()
        else:
            print(finalform.errors)
    # passing all forms to context
    context = {'sixteenform':sixteenform,'eightform':eightform,'fourform':fourform,'finalform':finalform}
    return render(request,'betting_manager/create_matches.html',context)


# BACKUP FOR BETTING

# def betting(request,match,stage):
#     person = Player.objects.get(user=request.user)
#     game = MatchGroupStageBetting.objects.get(Q(person_betting=person)&Q(match=match))
#     print("ahllo")
#     print(stage)
#     if game.match.played == "NO":
#         scrimmage = MatchGroupStageReal.objects.get(id=match)
#         group = scrimmage.team_one.group
#         print(scrimmage)
#         if request.method == "POST":
#             form = BettingForm(request.POST,instance=game)
#
#             if form.is_valid():
#                 print(request.POST)
#                 instance = form.save(commit=False)
#                 # print("Who betted",instance.person_betting)
#                 # instance.person_betting = person
#                 print("Person betting is",instance.person_betting)
#                 instance.save()
#                 return redirect('groups',group_value=group)
#                 print('redirected')
#             else:
#                 print(form.errors)
#         else:
#             form = BettingForm(instance=game)
#         context = {'form': form,'match':scrimmage}
#
#
#         return render(request,'betting_manager/group_betting.html',context)
#     else:
#         return redirect('not_allowed')
