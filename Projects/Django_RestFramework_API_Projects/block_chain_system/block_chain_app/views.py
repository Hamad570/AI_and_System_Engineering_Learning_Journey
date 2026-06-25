from django.shortcuts import render
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Candidate, Block
from .serializers import CandidateSerializer, BlockSerializer
from .blockchain import Blockchain

# Serve single page application layout
def index_view(request):
    return render(request, 'index.html')

class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
    permission_classes = [permissions.AllowAny]
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def perform_create(self, serializer):
        serializer.save(last_updated_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(last_updated_by=self.request.user)

@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def cast_vote(request):
    candidate_id = request.data.get('candidate_id')
    voter_id = request.data.get('voter_id')

    if not candidate_id or not voter_id:
        return Response({"error": "Missing candidate_id or voter_id"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        candidate = Candidate.objects.get(id=candidate_id)
    except Candidate.DoesNotExist:
        return Response({"error": "Candidate not found"}, status=status.HTTP_404_NOT_FOUND)

    # Get last block to chain hashes
    last_block = Block.objects.all().order_by('-index').first()
    if last_block:
        prev_hash = last_block.block_hash
        next_index = last_block.index + 1
    else:
        prev_hash = "0" * 64
        next_index = 1

    block_data = {"candidate": candidate.name, "voter": voter_id}
    new_raw_block = Blockchain.create_block(next_index, prev_hash, block_data)

    # Save to database
    Block.objects.create(
        index=new_raw_block['index'],
        timestamp=new_raw_block['timestamp'],
        candidate_name=candidate.name,
        voter_id=voter_id,
        previous_hash=new_raw_block['previous_hash'],
        block_hash=new_raw_block['hash']
    )

    # Increment votes securely
    candidate.vote_count += 1
    candidate.save()

    return Response({"message": "Vote successfully chained!"}, status=status.HTTP_201_CREATED)
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def blockchain_history(request):
    blocks = Block.objects.all().order_by('index')
    # Simple dictionary conversion taake bina naye serializer ke direct fetch ho jaye
    data = [{
        "index": b.index,
        "timestamp": b.timestamp,
        "candidate": b.candidate_name,
        "voter": b.voter_id,
        "previous_hash": b.previous_hash,
        "block_hash": b.block_hash
    } for b in blocks]
    return Response(data, status=status.HTTP_200_OK)