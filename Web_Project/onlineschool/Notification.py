from material.models import Massage
from Account.models import Faculty

class Notifications:
    notifications = []
    
    class Make_Pair:
        def __init__(self, faculty,msg):
            self.msg = msg
            self.faculty = faculty
            
    def __init__(self):
        self.notifications.clear()
        for temp in Massage.objects.all():
            faculty = temp.faculty_id
            temp = self.Make_Pair(Faculty.objects.get(id = faculty), temp)
            self.notifications.append(temp)
                                    
    def getNotify(self):
        self.notifications.reverse()
        return self.notifications
    
    def __iter__(self):
        return self.notifications.__init__()
            
            

   
        
            
            
        
        
    
    
    