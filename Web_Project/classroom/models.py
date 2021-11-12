from django.db import models

#models begin from here.
        
class ClassRoom(models.Model):
    title = models.CharField(null=True, max_length=120)
    course_name = models.CharField(max_length=20)
    section = models.IntegerField()


  
        
        
        
        
    
    
    
    