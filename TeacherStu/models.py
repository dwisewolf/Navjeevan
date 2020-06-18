from django.db import models

# Create your models here.

class Student(models.Model):
    CATEGORY_CHOICES = (
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
    )
    CLASS_CHOICES = (
        ('PREP','PREP'),
        ('LKG','LKG'), 
        ('UKG','UKG'),
        ('I','I'), 
        ('II','II'),
        ('III','III'),
        ('IV','IV'), 
        ('V','V'), 
        ('VI','VI'), 
        ('VII','VII'), 
        ('VIII','VIII'), 
        ('IX','IX'), 
        ('X','X'), 
        ('XI','XI'), 
        ('XII','XII')
    )

    userid = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=255)
    fatherName = models.CharField(max_length=255,null=True,blank=True)
    clas = models.CharField(max_length=30, choices=CLASS_CHOICES,null=True,blank=True)
    # clas = models.CharField(max_length=30,null=True,blank=True)
    section = models.CharField(max_length=255,null=True,blank=True)
    houseName = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255,null=True,blank=True)
    mobileNum = models.IntegerField(null=True, blank=False)
    category = models.CharField(max_length=15, choices=CATEGORY_CHOICES)
    #password = models.CharField(max_length=255,null=True,blank=True)
    # school_code = models.CharField(max_length=15,choices=SCHOOL_CHOICES)
    # school_code = models.ForeignKey(SchoolDB, on_delete=models.CASCADE)

    def __str__(self):
        # return self.name
        return str(self.userid)+" ------- "+str(self.name)+" ------- "+str(self.clas)+" ------- "+str(self.section)+" ------- "+str(self.mobileNum)+" ------- "+str(self.fatherName)

class User(models.Model):
    # userId = models.IntegerField(null=True)
    mobileNum = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.mobileNum

class Video(models.Model):

    userid = models.CharField(max_length=100)
    name = models.CharField(max_length=500)
    # video_link= models.FileField(upload_to='videos/', null=True, verbose_name="Video Link", max_length=1000)
    video_link = models.URLField(verbose_name="Video Link", max_length=1000)
    description = models.CharField(max_length=500)
    thumbnail_link = models.URLField(verbose_name="Image Link", max_length=1000)
    # models.FileField(upload_to='images/', null=True, verbose_name="Image Link", max_length=1000)
    played_time = models.TimeField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('timestamp',)

    def __str__(self):
        return self.userid + " : " + str(self.name)

class News(models.Model):
    # userId = models.IntegerField(null=True)
    school_code = models.CharField(max_length=3,null=True,blank=True)
    user_code = models.CharField(max_length=10,null=True,blank=True)
    class_code = models.CharField(max_length=10,null=True,blank=True)
    news = models.TextField(max_length=255,null=True,blank=True)
    expiryDate = models.DateField(null=True,blank=True)
    addDate = models.DateTimeField(auto_now_add=True)
    modifyDate = models.DateTimeField(auto_now=True)
    link = models.URLField(verbose_name="Image Link", max_length=1000,null=True,blank=True)

    class Meta:
        ordering = ('addDate',)

    def __str__(self):
        return str(self.school_code) + " : " + str(self.user_code) + " : " + str(self.addDate) + " : " + str(self.expiryDate)


