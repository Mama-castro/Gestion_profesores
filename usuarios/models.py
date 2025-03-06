from django.db import models
from django.contrib.auth.models import AbstractUser
from simple_history.models import HistoricalRecords


# class UserManage(AbstractUser):
#     ROLES = (
#         ('admin', 'Administrador'),
#         ('profesor', 'Profesor'),
#     )
#     role = models.CharField(max_length=10,
#                             choices=ROLES,
#                             default='profesor')
#     history = HistoricalRecords()
#
#     def is_admin(self):
#         return self.role == 'admin'
#
#     def is_profesor(self):
#         return self.role == 'profesor'
