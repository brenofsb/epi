from django.db import models
from django.utils import timezone

class Colaborador(models.Model):
    nome = models.CharField(max_length=30, null=False, blank=False)
    telefone = models.CharField(max_length=30)

    def __str__(self):
        return self.nome

class Equipamento(models.Model):
    nome = models.CharField(max_length=30, null= False, blank=False)
   
    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    status_choices = [
        ('emprestado', 'Emprestado'),
        ('fornecido','Fornecido'),
        ('devolvido', 'Devolvido'),
        ('danificado', 'Danificado'),
        ('perdido', 'Perdido'),
    ]

    colaborador = models.ForeignKey(Colaborador, on_delete=models.PROTECT)
    equipamento = models.ForeignKey(Equipamento, on_delete=models.PROTECT)
    dt_emprest = models.DateTimeField(default=timezone.now)
    dt_prev_devo = models.DateTimeField()
    dt_devo = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=status_choices, default='Emprestado')
    condicoes = models.CharField(max_length=200, blank=True)
    obs_devo = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.equipamento} - {self.colaborador}'
