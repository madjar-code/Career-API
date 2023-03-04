import uuid
from django.db import models
from .managers import SoftDeletionManager


class SoftDeletionModel(models.Model):
    """
    Abstract model with soft deletion
    """
    is_active = models.BooleanField(
        default=True,
        verbose_name='Активность'
    )

    objects = models.Manager()
    active_objects = SoftDeletionManager()

    class Meta:
        abstract = True

    def soft_delete(self) -> None:
        self.is_active = False
        self.save()
    
    def restore(self) -> None:
        self.is_active = True
        self.save()


class UUIDModel(models.Model):
    """
    Abstract model for uuid
    """
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        db_index = True,
        editable = False
    )

    class Meta:
        abstract = True


class TimeStampModel(models.Model):
    """
    Abstract model with timestamp
    """
    created_at = models.DateTimeField(
        auto_now=True, null=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now_add=True, null=True,
        verbose_name='Дата последнего редактирования'
    )

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimeStampModel, SoftDeletionModel):
    """
    Base model for inheritance
    """
    class Meta:
        abstract = True

