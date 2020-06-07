from django.db import models

# Create your models here.
JOB_TYPE = (
   ('Full Time','Full Time'), 
   ('Part Time','Part Time'),
)


def image_upload(instance, filename):
    imagename , extention = filename.split(".")
    return "jobs/%s.%s"%(instance.id,extention)



class job(models.Model):
    title = models.CharField(max_length=100)
    #location
    job_type = models.CharField(("Job Type"), max_length=15 , choices = JOB_TYPE)
    description = models.TextField(("Description") , max_length=1000)
    published_at = models.DateTimeField(("Puplished At"), auto_now=True)
    vacanvy = models.IntegerField(("Vacanvy") , default=1)
    salary = models.IntegerField(("Salary") , default=0)
    experience = models.IntegerField(("Experience") , default=1)
    category = models.ForeignKey("category", verbose_name=(""), on_delete=models.CASCADE)
    image = models.ImageField(("Image"), upload_to=image_upload)

    class Meta:
        verbose_name = ("job")
        verbose_name_plural = ("jobs")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("job_detail", kwargs={"pk": self.pk})


class category(models.Model):
    name = models.CharField((""), max_length=25)    

    class Meta:
        verbose_name = ("category")
        verbose_name_plural = ("categorys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})

