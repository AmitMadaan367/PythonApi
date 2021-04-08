from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import time
import json
import pandas as pd


class Current_PairAPIView1(APIView):
    def post(self, request, format=None):
        data={}
        value = request.headers.get('value',None)

        def initial():
            excel_data_df = pd.read_excel('mdcLookup.xlsx')
            excel_data_df = pd.DataFrame(excel_data_df)
            return excel_data_df
        def driver(inputParameter):
            df = initial()
            df.set_index('DiagCode')
            rowFound = df.loc[df['DiagCode'] == inputParameter]
            output=rowFound['MDC'].to_string(index=False)
            return output

        output=driver(value)
        data.update({"data":output})


        
        return Response(data)
        