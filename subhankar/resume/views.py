from rest_framework.response import Response
from .models import Profile
from .serializers import ProfileSerializer
from rest_framework.views import APIView
# from rest_framework.parsers import MultiPartParser, FormParser
import io, re, PyPDF2
# Create your views here.


class ProfileUpload(APIView):
    # parser_classes = (MultiPartParser, FormParser,)
    # serializer = ProfileSerializer

    def post(self, request, format=None):
        file_serializer = ProfileSerializer(data=request.FILES)
        uploaded_file = request.FILES['file'].read() 
        
        pdfReader = PyPDF2.PdfFileReader(io.BytesIO(uploaded_file))
        i = 0
        content = []
        while (i<pdfReader.numPages):
            text = pdfReader.getPage(i)
            content.append(text.extractText())
            i +=1

        strr = ' '
        for x in content:
        	strr = strr + x

        strr = strr.strip('\n')
        strr = strr.replace('\n','')

        r = re.compile(r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})')
        phone_number = r.findall(strr)

        r = re.compile(r'[\w\.-]+@[\w\.-]+')
        email = r.findall(strr)

        for x in phone_number:
        	phone_number = x.replace(' ', '')
        	break

        for x in email:
        	email = x
        	break

        if file_serializer.is_valid():
        	file = Profile(file=request.FILES['file'], name=request.POST['name'], phone=phone_number, email=email, skill=request.POST['skill'])
        	file.save()
        	print("In")
        	return Response({'success'})
        else:
            return Response(file_serializer.errors, status=400)

    def get(self, request, format=None):
        profile = Profile.objects.all()
        serializer = ProfileSerializer(profile, many=True)
        return Response(serializer.data)