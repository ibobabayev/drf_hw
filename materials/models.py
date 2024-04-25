from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100,verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='materials/',verbose_name='превью',null=True,blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"


class Subject(models.Model):
    name = models.CharField(max_length=100,verbose_name='название')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='materials/',verbose_name='превью',null=True,blank=True)
    link = models.URLField(max_length=200,verbose_name='ссылка на видео',null=True,blank=True)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,verbose_name='курс')

    def __str__(self):
        return f'Урок {self.name} из курса {self.course}'

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"