from django.db import models
from common.mixins.models import\
    BaseModel, SoftDeletionModel, TimeStampModel


class NodeType(models.IntegerChoices):
    EDU = 9, 'Edu'
    JOB = 10, 'Job'


class Node(SoftDeletionModel, TimeStampModel):
    SHORT_NAME_LENGTH = 50
    MIDDLE_NAME_LENGTH = 65

    name = models.CharField(max_length=255)
    node_type = models.SmallIntegerField(
        default=NodeType.JOB,
        choices=NodeType.choices
    )
    counter = models.PositiveIntegerField()
    code = models.IntegerField(
        blank=True, null=True)

    @property
    def middle_name(self) -> str:
        name = self.name
        max_length = Node.MIDDLE_NAME_LENGTH
        return name if len(name) < max_length else name[:max_length] + '...'

    @property
    def short_name(self) -> str:
        name = self.name
        max_length = Node.SHORT_NAME_LENGTH
        return name if len(name) < max_length else name[:max_length] + '...'

    def __str__(self) -> str:
        return self.short_name


class Growth(BaseModel):
    start_node = models.ForeignKey(
        to=Node, on_delete=models.CASCADE,
        related_name='outgoing'
    )
    end_node = models.ForeignKey(
        to=Node, on_delete=models.CASCADE,
        related_name='incoming'
    )
    counter = models.PositiveIntegerField()
    period = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )

    def __str__(self) -> str:
        return f'From {self.start_node} to {self.end_node}'
