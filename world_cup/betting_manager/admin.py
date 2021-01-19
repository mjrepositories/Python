from django.contrib import admin
from .models import Team,MatchGroupStageReal,MatchFinalStageReal,Player,MatchGroupStageBetting\
    ,MatchFinalStageRealSixteen,MatchFinalStageBettingSixteen,MatchFinalStageRealEight\
    ,MatchFinalStageBettingEight,MatchFinalStageRealFour,MatchFinalStageBettingFour\
    , MatchFinalStageRealFinal,MatchFinalStageBettingFinal

# Register your models here.


from import_export.admin import ImportExportModelAdmin

admin.site.register(Player)


@admin.register(Team,MatchGroupStageReal,MatchFinalStageReal,MatchGroupStageBetting,
                MatchFinalStageRealSixteen,MatchFinalStageBettingSixteen,MatchFinalStageRealEight\
    ,MatchFinalStageBettingEight,MatchFinalStageRealFour,MatchFinalStageBettingFour\
    , MatchFinalStageRealFinal,MatchFinalStageBettingFinal)
class ViewAdmin(ImportExportModelAdmin):
    pass