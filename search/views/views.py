from rest_framework.views import APIView
from search.serializers import CountrySerializer,RegionSerializer,PersonSerializer,UnknownPersonSerializer
from search.models import Country,Region,Person
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import face_recognition
import json
import numpy as np
from json import JSONEncoder
from search import serveces
from django.shortcuts import redirect
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,api_view

######################## COUNTRY #################
class CountryListView(APIView):
    def get(self,request):
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)

class CountryDetailView(APIView):
    def get(self,request, pk):
        queryset = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(queryset)
        return Response(serializer.data)

class CountryCreateView(APIView):
    def post(self,request):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class CountryDetailUpdateDeleteView(APIView):
    def get(self,request, pk):
        queryset = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(queryset)
        return Response(serializer.data)

    def put(self,request, pk):
        queryset = get_object_or_404(Country, pk=pk)
        serializer = CountrySerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        queryset = get_object_or_404(Country, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

########################## REGION ###############################
class RegionListView(APIView):
    def get(self, request):
        queryset = Region.objects.all()
        serializer = RegionSerializer(queryset, many=True)
        return Response(serializer.data)

class RegionDetailView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Region, pk=pk)
        serializer = RegionSerializer(queryset)
        return Response(serializer.data)

class RegionCreateView(APIView):
    def post(self, request):
        serializer = RegionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegionDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Region, pk=pk)
        serializer = RegionSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Region, pk=pk)
        serializer = RegionSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = get_object_or_404(Region, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

############################ PERSON ######################################
class PersonListView(APIView):
    def get(self, request):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)
        return Response(serializer.data)

class PersonDetailView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)

class PersonCreateView(APIView):
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PersonDetailUpdateDeleteView(APIView):
    def get(self, request, pk):
        queryset = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        queryset = get_object_or_404(Person, pk=pk)
        serializer = PersonSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = get_object_or_404(Person, pk=pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##########

class UnknownPersonDetail(APIView):
    def post(self,request):
        with open('sample.json') as json_file:
            data = json.load(json_file)
        known_face_encodings = [np.asarray(i['encode']) for i in data]
        serializeri = UnknownPersonSerializer(data=request.data)
        if serializeri.is_valid(raise_exception=True):
            serializeri.save()
            pic = request.data.get('image')
            pic = face_recognition.load_image_file(pic) #unknown rasm olindi
            uknown_encoding = face_recognition.face_encodings(pic)[0] #unknown rasm encodi
            minimum = 0.5
            result_index = None
            for i in range(len(known_face_encodings)):
                face_distances = face_recognition.face_distance([known_face_encodings[i]], uknown_encoding)[0]
                result = face_recognition.compare_faces([known_face_encodings[i]], uknown_encoding)[0]

                if result and face_distances < minimum:  # Here we used this method to reduce the number of True booleans and to help our program to choose correct one
                    minimum = face_distances
                    result_index = i  # known rasmlar ro'yhati ichidan o'xshash % eng yaqinini index raqami
            if result_index != None:
                pk = data[result_index]['id']
                queryset = get_object_or_404(Person, pk=pk)
                # queryset1 = get_object_or_404(UnknownPerson,images = pic)
                serializer = PersonSerializer(queryset)
                return Response(data=serializer.data, status=status.HTTP_302_FOUND)
            else:
                return  Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)


#########

def AllPersonEncode(request):
    list_encode = serveces.get_encode()
    class NumpyArrayEncoder(JSONEncoder):
        def default(self, obj):
            if isinstance(obj, np.ndarray):
                return obj.tolist()
            return JSONEncoder.default(self, obj)

    data = []
    for one_dict in list_encode:
        id = one_dict['id']
        path = f"media/{one_dict['image']}"
        pic = face_recognition.load_image_file(path)
        encode_pic = face_recognition.face_encodings(pic)[0]
        d = {
            'id': id,
            'encode': encode_pic
        }
        data.append(d)
    print(data)
    encodedNumpyData = json.dumps(data, indent=4, cls=NumpyArrayEncoder)

    with open("sample.json", "w") as outfile:
        outfile.write(encodedNumpyData)
    return redirect('/')