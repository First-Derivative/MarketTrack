from django.db import models
from django.core.exceptions import SuspiciousOperation # Consider writing on Error Classs
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserAccountManager(BaseUserManager):
  def create_user(self, username, email, password=None):
      if not email:
          raise ValueError("Users require an email address")
      if not username:
          raise ValueError("Users require a username")

      user = self.model(
          email = self.normalize_email(email),
          username = username,
      )

      user.set_password(password)
      user.save()
      return user

  def create_superuser(self, email, username, password):
      user = self.create_user(
          email = self.normalize_email(email),
          username = username,
          password = password
      )

      user.is_admin = True
      user.save(using=self._db)
      return user

class UserAccount(AbstractBaseUser):
  email = models.EmailField(verbose_name="email",max_length=50, unique=True)
  username = models.CharField(max_length=30, unique=True)
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  class Meta:
    verbose_name = "account"
    verbose_name_plural = "accounts"

  USERNAME_FIELD = 'username'
  REQUIRED_FIELDS = ('email',)

  objects = UserAccountManager()

  def __str__(self):
      return self.username

  #default override for has_perm
  def has_perm(self, perm, obj=None):
      return self.is_admin

  #default override for has_module_perms
  def has_module_perms(self, app_label):
      return self.is_active

  @property
  def is_staff(self):
      return self.is_admin