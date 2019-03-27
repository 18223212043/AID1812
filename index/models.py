from django.db import models

# Create your models here.

#创建一个实体类－Publisher
#表示出版社信息，属性如下：
#name:出版社名称
#address:出版社所在地址
#city:出版社所在地址
#country:出版社所在国家
#website:出版社网址
class Publisher(models.Model):
    name = models.CharField(max_length=30,verbose_name='出版社名称')
    address = models.CharField(max_length=200,verbose_name='出版社地址')
    city = models.CharField(max_length=20,verbose_name='所在城市')
    country = models.CharField(max_length=20,verbose_name='国家')
    website = models.URLField(verbose_name='站点')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'
        verbose_name = '出版社'
        verbose_name_plural = verbose_name

class Author(models.Model):
    #verbose_name在后台管理中显示的名称
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(null=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        db_table = 'author'
        verbose_name = '作者'
        verbose_name_plural = verbose_name
        #排序
        ordering = ['age','-id']

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50,verbose_name='书名')
    publicate_date = models.DateTimeField(verbose_name='发行时间')
    publisher = models.ForeignKey(Publisher,null=True,verbose_name='出版社')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
        verbose_name = '书籍'
        verbose_name_plural = verbose_name
        ordering = ['publicate_date']


class Wife(models.Model):
    name = models.CharField(max_length=30,verbose_name='姓名')
    age = models.IntegerField(verbose_name='年龄')
    author = models.OneToOneField(Author,null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'wife'
        verbose_name = '夫人'
        verbose_name_plural = verbose_name