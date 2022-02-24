from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models




def is_esprit_email(value):
    if not str(value).endswith('@esprit.tn'):
        raise ValidationError("your email is invalid. ", params={'value': value})

# Create your models here.


class User(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    email = models.EmailField('Email', validators=[is_esprit_email])
    def __str__(self):
        #return 'le prenom: '+self.prenom+', le nom: '+self.nom
        return f'First name:  {self.prenom} , Last name: {self.nom}'

class Etudiant(User):
    groupe = models.CharField(max_length=30)


class Coach(User):
    pass


class Projet(models.Model):
    nom_projet = models.CharField('Titre Projet', max_length=30)
    duree_projet = models.IntegerField('Duree Estimee', default=0)
    temps_alloue_par_projet = models.IntegerField('Temps Alloue', validators=[MinValueValidator(1), MaxValueValidator(10)])
    besoins = models.TextField(max_length=100)
    description = models.TextField(max_length=100)
    est_valide = models.BooleanField(default=False)
    createur = models.OneToOneField(
        Etudiant,
        related_name='project_owner',
        on_delete=models.CASCADE

    )
    superviseur = models.ForeignKey(
        Coach,
        on_delete= models.SET_NULL,
        null= True,
        related_name= 'project_coach',

    )
    members = models.ManyToManyField(
        Etudiant,
        through= 'MembershipInProject',
        related_name= 'les_membres',

    )


class MembershipInProject(models.Model):
        projet= models.ForeignKey(Projet, on_delete=models.CASCADE)
        etudiant= models.ForeignKey(Etudiant, on_delete=models.CASCADE)
        time_allocated_by_member= models.IntegerField('temps alloué par les membres')



