from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import memberSerializer
from .models import Member

# Create your views here.
@api_view(['GET'])
def get_members(request):
  if request.method == 'GET':
    query = Member.objects.all()
    serializer = memberSerializer(query, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_member_for_id(request, id):
  try:
    query = Member.objects.get(id=id)
  except Member.DoesNotExist:
    return Response({'error' : {
      'code' : 404,
      'message' : "Article not found!"
    }}, status = status.HTTP_404_NOT_FOUND)

  if request.method == "GET":
    serializer = memberSerializer(query)
    return Response(serializer.data)