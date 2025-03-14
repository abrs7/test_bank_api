from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.utils.decorators import method_decorator
import json
from .models import tbl_application, tbl_bank, tbl_branch

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_banks(request):
    banks = tbl_bank.objects.values('id', 'value')
    return Response({'banks': banks})
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_branches(request):
    bank_id = request.GET.get('bank_id')
    branches = tbl_branch.objects.filter(bank_id=bank_id).values('id', 'value')
    return Response({'branches': branches})

@permission_classes([IsAuthenticated])
@method_decorator(csrf_exempt, name='dispatch')
class SubmitApplication(APIView):
    def post(self, request):
        try:
            data = json.loads(request.body)
            application = tbl_application.objects.create(
                bank_name=data.get('bank_name'),
                branch_name=data.get('branch_name'),
                account_name=data.get('account_name'),
                account_number=data.get('account_number'),
                status='Submitted'
            )
            return Response({'message': 'Application submitted successfully', 'id': application.id}, status=201)
        except Exception as e:
            return Response({'error': str(e)}, status=400)# def get_banks(request):
