from django.db import models
import math
# Yanvar = 'Yanvar'
# Fevral = 'Fevral'
# Mart = 'Mart'
# Aprel = 'Aprel'
# May = 'May'
# Iyun = "Iyun"
# Iyul = 'Iyul'
# August = 'August'
# Sentabr = 'Sentabr'
# Oktabr= 'Oktabr'
# Noyabr = 'Noyabr'
# Dekabr = "Dekabr"
# month= [
#     (Yanvar , 'Yanvar'),
#     (Fevral , 'Fevral'),
#     (Mart , 'Mart'),
#     (Aprel , 'Aprel'),
#     (May , 'May'),
#     (Iyun , "Iyun"),
#     (Iyul , 'Iyul'),
#     (August , 'August'),
#     (Sentabr , 'Sentabr'),
#     (Oktabr, 'Oktabr'),
#     (Noyabr , 'Noyabr'),
#     (Dekabr , "Dekabr"),
#     ]
Male = "M"
Female = "F"
bal = 0
bal1 = 0.5
ball = 1.0
bal2 = 1.5
bL =2.0
bal3 = 2.5
bal4 = 3.0
bal5 = 3.5
bal6 =4.0
bL6 = 4.5
ok1 = 5.0
ok2= 5.5
ok3 = 6.0
ok4 = 6.5
ok5 =7.0
ok6 = 7.5
ok7 = 8.0
ok8 =8.5
ok9 = 9.0
score = [
        (bal , 0),
        (bal1 , 0.5),
        (ball , 1.0),
        (bal2 , 1.5),
        (bL ,2.0),
        (bal3 , 2.5),
        (bal4 , 3.0),
        (bal5 , 3.5),
        (bal6 , 4.0),
        (bL6 , 4.5),
        (ok1 , 5.0 ),
        (ok2 , 5.5),
        (ok3 , 6.0),
        (ok4 , 6.5),
        (ok5 ,7.0),
        (ok6 , 7.5),
        (ok7 , 8.0),
        (ok8 , 8.5),
        (ok9 , 9.0),
    ]
jins= [
        (Male , 'M'),
        (Female , 'F')]


#====================================================================================
class Student(models.Model):
    familiya=models.CharField(max_length=200)
    ism=models.CharField(max_length=200)
    jinsi = models.CharField(choices=jins,max_length=6)
    tel_raqam=models.CharField(max_length=13,help_text="+998901112233") 
    rasm = models.ImageField(upload_to="puple/pic",null=True,blank=True)
    tulov = models.BooleanField()
    Country = models.CharField(help_text="Davlati",max_length=200)
    millati = models.CharField(max_length=200)
    birth = models.DateField()
    @property
    def one_id(self):
        return self.id+1000


    def __str__(self):
        return f"{self.familiya}  | {self.ism} | {self.one_id}"

    
#============================================================================================
    
      
 

class Ielts_date(models.Model):
    Date=models.DateField()

    def __str__(self) -> str:
        return f"{self.Date}"
    class Meta:
       
        verbose_name = 'Test kun '
        verbose_name_plural = 'Test kunlari'
#====================================================================================
class Full(models.Model):
    
    Date = models.ForeignKey(Ielts_date, on_delete=models.CASCADE)
    FIO= models.ForeignKey("Student",on_delete=models.CASCADE)   
    Listening = models.FloatField(choices=score)
    Reading = models.FloatField(choices=score)
    Writing = models.FloatField(choices=score)
    Speaking = models.FloatField(choices=score)



    @property 
    def familiya(self):
        return self.FIO.familiya
    
    def overal(self):
        a = self.Listening +self.Reading+self.Writing+self.Speaking      
        l = a%4
        d = l / 4
        c=a//4     
        if d>=0.25 and  d<=0.73:
            return c+0.5
        elif d>=0 and  d<0.25:
            return c+0
        else:
            return c+1
    def ID(self):
        return self.FIO.one_id
    def img(self):
        return self.FIO.rasm
    def ism(self):
        return self.FIO.ism
    def tel_raqam(self):
        return self.FIO.tel_raqam
    def jinsi(self):
        return self.FIO.jinsi
 
        

    class Meta:
       
        verbose_name = 'student '
        verbose_name_plural = 'Full Mock'
  #=-=--=--=-=-=-=-=-=--=-=-===========================================--->
class Reading(models.Model):
    
    Date = models.ForeignKey(Ielts_date, on_delete=models.CASCADE)
    FIO= models.ForeignKey("Student",on_delete=models.CASCADE)   
    Listening = models.FloatField(choices=score)
    Reading = models.FloatField(choices=score)
    



    @property 
    def familiya(self):
        b=self.FIO.familiya
        return b
    def ID(self):
        return self.FIO.one_id
    def ism(self):
        return self.FIO.ism
    def tel_raqam(self):
        return self.FIO.tel_raqam
    def img(self):
        return self.FIO.rasm
    def jinsi(self):
        return self.FIO.jinsi
    def overal(self):
        a = (self.Listening +self.Reading)   
        l = a%2
        d = l / 2
        c=a//2     
        if d>=0.25 and  d<=0.73:
             return c+0.5
        elif d>=0 and  d<0.25:
            return c+0
        else:
            return c+1
        

    class Meta:
       
        verbose_name = 'student '
        verbose_name_plural = 'Listening Reading Mock'      
#====================================================================================
class Speaking(models.Model):
    
    Date = models.ForeignKey(Ielts_date, on_delete=models.CASCADE)
    FIO= models.ForeignKey("Student",on_delete=models.CASCADE)   
    Grammar = models.FloatField(choices=score)
    Pronunciation = models.FloatField(choices=score)
    Fluency = models.FloatField(choices=score)
    Lexical = models.FloatField(choices=score)





    @property 
    def familiya(self):
        return self.FIO.familiya

    def ID(self):
        return self.FIO.one_id
    def img(self):
        return self.FIO.rasm
    def ism(self):
        return self.FIO.ism
    def tel_raqam(self):
        return self.FIO.tel_raqam
    def jinsi(self):
        return self.FIO.jinsi
    def overal(self):
        a = (self.Grammar +self.Pronunciation+self.Fluency+self.Lexical)   
        l = a%4
        d = l / 4
        c=a//4     
        if d>=0.25 and  d<=0.73:
             return c+0.5
        elif d>=0 and  d<0.25:
            return c+0
        else:
            return c+1
        

    class Meta:
       
        verbose_name = 'Student'
        verbose_name_plural = 'Speaking Mock'
  #=-=--=--=-=-=-=-=-=--=-=-===========================================--->




    
    

        
        
       
    
  


    
    
   
    
   
    


