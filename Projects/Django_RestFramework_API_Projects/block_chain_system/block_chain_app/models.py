from django.db import models
from django.contrib.auth.models import User

# Isko purane Candidate model se replace kar dein
class Candidate(models.Model):
    name = models.CharField(max_length=100, unique=True)
    party_name = models.CharField(max_length=50, default="Independent") # Nayi field
    vote_count = models.IntegerField(default=0)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.party_name})"

class Block(models.Model):
    index = models.IntegerField()
    timestamp = models.FloatField()
    candidate_name = models.CharField(max_length=100)
    voter_id = models.CharField(max_length=100)
    previous_hash = models.CharField(max_length=64)
    block_hash = models.CharField(max_length=64)

    def __str__(self):
        return f"Block {self.index} - {self.candidate_name}"