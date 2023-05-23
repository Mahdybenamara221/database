from django.db import models

# Create your models here.

class Asset(models.Model):
    name=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    category=models.CharField(max_length=100)
    status=models.CharField(max_length=100)

    #workstation='Workstation'
    #server='Server'
    #choice=[
    #    (workstation,'Workstation'),
     #   (server,'Server'),
    #]
    #category=models.CharField(max_length=11,
    #choices=choice)


   # ready='Ready to deploy'
    #deployed='Deployed'
    #pending='Pending'
    #lost='Lost/Stolen'

  #  choice2=[
    #    (ready,'Ready to deploy'),
      #  (deployed,'Deployed'),
     #   (pending,'Pending'),
    #    (lost,'Lost/Stolen'),
   # ]
    #status=models.CharField(max_length=15,
    #choices=choice2)


    def __str__(self):
        return "%s"%(self.name)
    
    class Meta:
        db_table="Assets"