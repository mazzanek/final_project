from django.db import models
from django.contrib.auth.models import User


class DivingRecord(models.Model):
    # Definice disciplín
    DYN = 'DYN'
    DNF = 'DNF'
    DYNB = 'DYNB'
    FIM = 'FIM'
    CTW = 'CTW'
    CTWB = 'CTWB'
    CNF = 'CNF'
    STA = 'STA'

    DISCIPLINE_CHOICES = [
        (DYN, 'Dynamic with Fins (DYN)'),
        (DNF, 'Dynamic No Fins (DNF)'),
        (DYNB, 'Dynamic with Bi-Fins (DYNB)'),
        (FIM, 'Free Immersion (FIM)'),
        (CTW, 'Constant Weight (CTW)'),
        (CTWB, 'Constant Weight Bi-Fins (CTWB)'),
        (CNF, 'Constant Weight No Fins (CNF)'),
        (STA, 'Static apnea (STA)'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    discipline = models.CharField(
        max_length=4,
        choices=DISCIPLINE_CHOICES,
        default=DYN,
    )  # Disciplína potápění
    depth = models.DecimalField(max_digits=5, decimal_places=2)  # Maximální hloubka v metrech
    duration = models.DurationField()  # Délka potápění
    location = models.CharField(max_length=255)  # Místo potápění
    date = models.DateField()  # Datum potápění


    def __str__(self):
        return self.user.username

        """
        return f"{self.user.username} - {self.depth}m {self.discipline} at {self.location} on {self.date}" """""