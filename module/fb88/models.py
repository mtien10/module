from django.db import models


class TimeStampMixin(models.Model):
    """
    An abstract base class model that provides self-updating
    ``created`` and ``modified`` fields.
    """
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return ""


class Fb88(TimeStampMixin):
    name = models.CharField(max_length=255, null=True,blank=True, help_text='Hay dien doi bong ban dat cuoc ',
                            verbose_name='Dat cuoc cho doi bong than yeu')

    class Meta:
        db_table = 'nhacai_fb88'
        verbose_name = 'Fb88'
        verbose_name_plural = 'Nha cai uy tin'

    def __str__(self):
        return self.name


class Question(TimeStampMixin):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Bạn muốn cược đội nào giải này',
                            verbose_name='Dat cuoc')
    fb88 = models.ForeignKey(Fb88, null=True, blank=True, help_text='Chon dat cuoc', on_delete=models.DO_NOTHING,
                             related_name='Selection')
    image = models.ForeignKey("Image", null=True, blank=True, on_delete=models.DO_NOTHING,
                              related_name='question_image')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = 'fb88_question'
        verbose_name = 'Cau hoi'
        verbose_name_plural = 'Cau hoi?'

    def __str__(self):
        return self.name


class Answer(TimeStampMixin):
    name = models.CharField(max_length=255, null=True, blank=True, help_text='Hay dien ten doi bong muon cuoc ',
                            verbose_name='Cau tra loi ')
    question = models.ForeignKey(Question, null=True, blank=True, help_text='Selection',
                                 on_delete=models.DO_NOTHING,
                                 related_name='answer')
    is_deleted = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        db_table = 'fb88_answer'
        verbose_name = 'Cau tra loi'
        verbose_name_plural = 'cau tra loi'

    def __str__(self):
        return self.name


class Image(TimeStampMixin):
    image = models.ImageField(null=True, blank=True, upload_to='upload/images/%Y/%m/%d')
    h = models.FloatField(null=True, blank=True, default=0)
    w = models.FloatField(null=True, blank=True, default=0)

    class Meta:
        db_table = 'fb88_image'

    @staticmethod
    def get_entity_name():
        return 'Image'

# Create your models here.
