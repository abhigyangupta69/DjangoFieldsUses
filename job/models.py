from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from datetime import date


class JobApplication(models.Model):
    title = models.CharField(max_length=100)
    joining_date = models.DateTimeField(null=True,blank=True)
    dob = models.DateField(null=True, blank=True)
    important = models.BooleanField(default=False)
    ############USER Many2One field##########
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #######################################
    location=models.CharField(max_length=100,null=True,blank=True)

    ###########Display Field in Admin pannel###############
    DisplayFields=['title','joining_date','dob','age','user','location',]
    ###########Create Filter###############
    FilterFields=['title','location',]
    ###########Search Pannel###############
    SearchFields = ['title', 'location', ]


    ########Create Compute Field Age(Without Field)#########
    @property
    def age(self):
        if self.dob!=None:
            age=date.today().year- self.dob.year
            return age

    def __str__(self):
        return self.title


class Jobs(models.Model):
    profile = models.ForeignKey(JobApplication, on_delete=models.CASCADE)
    exp_required = models.CharField(max_length=10,default='1+')
    ########One2One Field(only show user where staff status True)#################
    user = models.OneToOneField(User, on_delete=models.PROTECT,limit_choices_to={'is_staff':True},default=False)


class CompanyApplication(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    ############Many2many Field from User###################
    user = models.ManyToManyField(User)
    DisplayFields=['userwritten']

    @property
    def userwritten(self):
        if self.user != None:
            userwritten=",".join([str(u)for u in self.user.all()])
            return userwritten