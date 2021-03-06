from django.contrib import admin,messages

# Register your models here.
from App.models import Etudiant, Coach, Projet, MembershipInProject

admin.site.register(Etudiant)
admin.site.register(Coach)
# admin.site.register(Projet, ProjetAdmin)

class Membership(admin.TabularInline): #StackedInline
    model=MembershipInProject
    extra=1

@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    inlines = (Membership,)
    list_display = (
    'nom_projet', 'superviseur', 'duree_projet', 'temps_alloue_par_projet', 'besoins', 'est_valide', 'createur',)
    fieldsets = (('A propos', {'fields': ('nom_projet', 'besoins', 'description',)}),
                 ('Etat', {'fields': ('est_valide',)}),
                 ('Duree', {'fields': ('duree_projet', 'temps_alloue_par_projet',)}),
                 ('People', {'fields': ('superviseur', 'createur',)}))
    list_per_page = 2

    def set_to_valid(self,request, queryset):
        x=queryset.update(est_valide=True)
        if(x!=0):
            messages.success(request,"%s Project updated successfully! "%x)

    def set_to_invalid(self,request, queryset):
        row_invalid = queryset.filter(est_valide=False)
        if(row_invalid.count()>0):
            messages.error(request,"%s this article is already invalid"%row_invalid.count())
        else:
            x=queryset.update(est_valide=False)
            if(x!=0):
                messages.success(request,"%s Project updated successfully! "%x)


    set_to_valid.short_description= 'validate project'
    set_to_invalid.short_description= 'invalidate project'
    actions = ['set_to_valid','set_to_invalid']
    #actions_on_bottom = True

    list_filter=('est_valide','createur')
    search_fields = ['nom_projet']





