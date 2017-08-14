# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)

	class Meta: 
		verbose_name = 'Categoria'
		verbose_name_plural = 'Categorias'
		ordering = ['name']

	def __unicode__(self):
		return self.name

class Product(models.Model):
	name = models.CharField('Nome', max_length=100)
	slug = models.SlugField('Identificador', max_length=100)
	category = models.ForeignKey('catalog.Category', verbose_name='Categoria')
	description = models.TextField('Descrição', blank=True)
	price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

	created = models.DateTimeField('Criado em', auto_now_add=True)
	modified = models.DateTimeField('Modificado em', auto_now=True)	


	class Meta: 
		verbose_name = 'Produto'
		verbose_name_plural = 'produtos'
		ordering = ['name']

	def __unicode__(self):
		return self.name