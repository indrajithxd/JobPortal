from django.shortcuts import render,get_object_or_404
from rest_framework.views import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job,Applications
from .serializers import JobSerializer,ApplicationSerializer,ReviewSerializer
# Create your views here.

class JobListCrateView(APIView):

    def get(self,request):
        qs=Job.objects.all()
        serializer_instance=JobSerializer(qs,many=True)
        return Response(data=serializer_instance.data)

    def post(self,request):
        form_data=request.data
        serializer_instance=JobSerializer(data=form_data)
        if serializer_instance.is_valid():
            actual_data=serializer_instance.validated_data
            Job.objects.create(**actual_data)
            return Response(data={"message":"jobposted"})
        else:
            return Response(data=serializer_instance.errors)

        
class JobRetreiveUpdateDelete(APIView):
    def get(self,request,pk):
        qs=get_object_or_404(Job,id=pk)
        job_instance=JobSerializer(qs)

        return Response(data=job_instance.data)


    def put(self,request,pk):
        job=get_object_or_404(Job,id=pk)
        form_data=request.data
        j_instance=JobSerializer(data=form_data)
        if j_instance.is_valid():
            actualdata=j_instance.validated_data
            Job.objects.filter(id=job.id).update(**actualdata)
            return Response(data={"message":"job data updated!"})
        else:
            return Response(data=j_instance.error,status=status.HTTP_400_BAD_REQUEST)


    def delete(self,request,pk):
        job=get_object_or_404(Job,id=pk)
        job.delete()
        return Response(data={"message":"job data updated"})

class ApplicationListCreateView(APIView):

    def get(self,request):
        qs=Applications.objects.all()
        job_instance = ApplicationSerializer(qs,many=True)
        return Response(data=job_instance.data)

    def post(self,request):
        form_data=request.data
        s_instance=ApplicationSerializer(data=form_data)
        if s_instance.is_valid():
            actual_data=s_instance.validated_data
            Applications.objects.create(**actual_data)
            return Response(data={"message":"application posted!"})
        else:
            return Response(data=s_instance.errors,status=status.HTTP_400_BAD_REQUEST)

class ApplicationsRetreiveUpdateDeleteView(APIView):

    def get(self,request,pk):
        qs=get_object_or_404(Applications,id=pk)
        s_instance=ApplicationSerializer(qs)
        return Response(data=s_instance.data)

    def post(self,request,pk):
        application=get_object_or_404(Applications,id=pk)
        form_data=request.data
        s_instance=ApplicationSerializer(data=form_data)
        if s_instance.is_valid():
            actual_data=s_instance.validated_data
            Applications.objects.filter(id=application.id).update(**actual_data)
            return Response(data={"message":"Data updated!"})
        else:
            return Response(data=s_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
       
        application = get_object_or_404(Applications, id=pk)
        application.delete()
        return Response({"message": "application deleted!"})

class ReviewApplicationView(APIView):
    

    def put(self, request, pk):
        application = get_object_or_404(Applications, id=pk)
        form_data = request.data
        s_instance = ReviewSerializer(data=form_data)
        if s_instance.is_valid():
            actual = s_instance.validated_data
            Applications.objects.filter(id=application.id).update(**actual)
            return Response(data= {"message": "Updated!"})
        else:
            return Response(data= s_instance.errors, status= status.HTTP_400_BAD_REQUEST)