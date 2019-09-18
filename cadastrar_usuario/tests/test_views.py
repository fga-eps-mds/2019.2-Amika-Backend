from django.test import TestCase, Client
from django.urls import reverse
from cadastrar_usuario.models import Project, Category, Expense
import json

class TestViews(TestCase):

    
