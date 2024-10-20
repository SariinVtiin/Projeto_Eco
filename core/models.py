from django.db import models
from django.contrib.auth.models import User

# Lista de estados brasileiros
UF_CHOICES = [
    ('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'),
    ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'),
    ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'),
    ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'),
    ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'),
    ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'),
    ('SE', 'Sergipe'), ('TO', 'Tocantins')
]

class Totem(models.Model):
    STATUS_CHOICES = (
        ('ativo', 'Ativo'),
        ('excluido', 'Excluído'),
    )

    numero_serie = models.CharField(max_length=100, default='1100 1000')
    cidade = models.CharField(max_length=100, default='N/A')
    uf = models.CharField(max_length=2, default='DF')
    geolocalizacao = models.CharField(max_length=100, default='1100 1000' )
    observacao = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ativo')  # Campo de status para soft delete

    def __str__(self):
        return f"{self.numero_serie} - {self.cidade}/{self.uf}"

#    
# NÃO APAGAR email = models.EmailField(max_length=255, unique=True, default='default@example.com')  # Novo campo de e-mail 
#

class Coleta(models.Model):
    totem = models.ForeignKey('Totem', on_delete=models.CASCADE)
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    data_hora = models.DateTimeField(auto_now_add=True)  # Nome correto deve ser `data_hora`
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.usuario} - {self.totem} - {self.peso} Kg" 

class Rota(models.Model):
    nome = models.CharField(max_length=100)
    dias_semana = models.CharField(max_length=200)  # Exemplo: "segunda, terça"
    periodo = models.CharField(max_length=50)  # Exemplo: "manhã, tarde, noite"
    data_criacao = models.DateTimeField(auto_now_add=True)
    ordem_totens = models.JSONField(default=list)  # Novo campo para armazenar a ordem dos Totens

    def __str__(self):
        return self.nome


