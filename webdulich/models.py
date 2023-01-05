from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.utils.text import slugify
from datetime import date
from ckeditor.fields import RichTextField

class Post(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Post')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'

class FastNews(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(FastNews, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('FastNews')
        verbose_name_plural = _('FastNews')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'

class Experience(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Experience, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Experience')
        verbose_name_plural = _('Experience')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'
        
class Discover(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Discover, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Discover')
        verbose_name_plural = _('Discover')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'
        
class Food(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Food')
        verbose_name_plural = _('Food')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'
        
class Brand(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Brand')
        verbose_name_plural = _('Brand')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'
        
class Restaurant(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(max_length=254, unique=True, blank=True, editable=True)
    author_name = models.CharField(max_length=35)
    short_description = models.TextField(verbose_name=_('Short description'))
    description = RichTextField()
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    publish_at = models.DateTimeField(verbose_name=_('Publish at'),)
    feature_img = models.ImageField(upload_to='media', blank=True, null=True, max_length=254,
                                      verbose_name=_('Feature Image'))
    status = models.BooleanField(default=0, verbose_name=_('Status'))
    views_count = models.IntegerField(default=0, verbose_name=_('Views count'))

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Restaurant, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurant')
        ordering = ['-publish_at']
        get_latest_by = 'created_at'
        