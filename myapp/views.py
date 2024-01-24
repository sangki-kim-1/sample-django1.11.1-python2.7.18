from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .serializers import memberSerializer
from .models import Member

# Create your views here.
@api_view(['GET','POST'])
def getMember(request):
  if request.method == 'GET':
    query = Member.objects.all()
    serializer = memberSerializer(query,many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    member = memberSerializer(data=request.data)
    if Member.is_valid():
      Member.save()
      return Response(Member.data)
    return Response(Member.errors,status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET','PUT','DELETE'])
def getMemberForId(request,id):
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
  elif request.method=='PUT':
    member = memberSerializer(query,data=request.data)
    if Member.is_valid():
      Member.save()
      return Response(Member.data)
    return Response(Member.errors,status=status.HTTP_400_BAD_REQUEST)
  elif request.method=='DELETE':
    query.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)