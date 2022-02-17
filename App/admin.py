from django.contrib import admin,messages

# Register your models here.
from App.models import Etudiant, Coach, Projet

admin.site.register(Etudiant)
admin.site.register(Coach)
# admin.site.register(Projet, ProjetAdmin)


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = (
    'nom_projet', 'superviseur', 'duree_projet', 'temps_alloue_par_projet', 'besoins', 'est_valide', 'createur',)
    fieldsets = (('A propos', {'fields': ('nom_projet', 'besoins', 'description',)}),
                 ('Etat', {'fields': ('est_valide',)}),
                 ('Duree', {'fields': ('duree_projet', 'temps_alloue_par_projet',)}),
                 ('People', {'fields': ('superviseur', 'createur',)}))
    list_per_page = 2

    def set_to_valid(self,request, queryset):
        queryset.update(est_valide=True)

    def set_to_invalid(self,request, queryset):
        row_invalid = queryset.filter(est_valide=False)
        if(row_invalid.count()>0):
            messages.errors(request,"%s this article is already invalid"%row_invalid.count())
        #queryset.update(est_valide=False)


    set_to_valid.short_description= 'validate project'
    set_to_invalid.short_description= 'invalidate project'
    actions = ['set_to_valid','set_to_invalid']





