from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.
JOB_TYPE = (
   ('Full Time','Full Time'), 
   ('Part Time','Part Time'),
)


def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)



class job(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(("Job Type"), max_length=15 , choices = JOB_TYPE)
    description = models.TextField(("Description") , max_length=1000)
    published_at = models.DateTimeField(("Puplished At"), auto_now=True)
    vacancy = models.IntegerField(("Vacancy") , default=1)
    salary = models.IntegerField(("Salary") , default=0)
    experience = models.IntegerField(("Experience") , default=1)
    category = models.ForeignKey("category", verbose_name=(""), on_delete=models.CASCADE)
    image = models.ImageField(("Image"), upload_to=image_upload)

    slug = models.SlugField(blank=True , null=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(job , self).save(*args, **kwargs)

        pass
    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("jobs")

    def __str__(self):
        return self.title



class category(models.Model):
    name = models.CharField((""), max_length=25)    

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    def __str__(self):
        return self.name


class Apply(models.Model):
    job = models.ForeignKey(job, on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = models.EmailField( max_length=254)
    website = models.URLField( max_length=200)
    cv = models.FileField( upload_to='apply/')
    cover_letter = models.TextField(max_length=500)
    created_at = models.DateTimeField(("Puplished At"), auto_now=True)

    

    class Meta:
        verbose_name = ("Apply")
        verbose_name_plural = ("Applys")

    def __str__(self):
        return self.name

