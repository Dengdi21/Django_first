from django.db import models

# Create your models here.
# 数据库模型


class MovieKind(models.Model):
    """
    电影类型
    """

    name = models.CharField(max_length=255, verbose_name="电影类型")
    desc = models.CharField(max_length=255, verbose_name="电影类型的描述")

    def __str__(self):
        return self.name


class MovieDetail(models.Model):
    title = models.CharField(max_length=255, verbose_name='电影标题',unique="True")
    desc = models.CharField(max_length=1000, verbose_name='电影简介',default="暂无简介")
    online_time = models.DateField(verbose_name='上映日期')
    # upload_to:上传图片到某个地方
    img = models.ImageField(upload_to='movie', null=True, default=None)

    kind = models.ManyToManyField (MovieKind)

    def __str__(self):
        return self.title


