from django.db import models


class Config(models.Model):
    params = models.TextField()
    step_number = models.IntegerField()

    def __str__(self):
        return f"Config with step number {self.step_number} and params {self.params}"


class Rate(models.Model):
    currency_code = models.CharField(max_length=10)
    date = models.DateField()
    currency_abbreviation = models.CharField(max_length=10)
    currency_unit = models.IntegerField()
    currency_name = models.TextField()
    currency_exchange_rate = models.FloatField()

    def __str__(self):
        return f"{self.currency_abbreviation} - {self.date}"


class ActionLog(models.Model):
    action = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Action log created at {self.created_at}"
