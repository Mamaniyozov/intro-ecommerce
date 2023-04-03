from django.views import View
from django.http import HttpRequest, JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json

# import models
from .models import (
    Product,
    Company,
    Category
)

def to_dict(product: Product) -> dict:
    '''convert product obj to dict'''
    return {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'color': product.color,
        'price': product.price,
        'company': product.company.id,
    }


class ProductView(View):
    def get(self, request: HttpRequest, id=None) -> JsonResponse:
        '''get products'''
        if id is None:
            # get all products
            products = Product.objects.all()

            # list of products
            products_list = [to_dict(product) for product in products]

            return JsonResponse(products_list, safe=False)
        else:
            try:
                product = Product.objects.get(id=id)
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def add_post(self, request: HttpRequest)-> JsonResponse:
        if request.method == 'POST':
            data=request.body

            decodet=data.decode()
            data = json.loads(decodet)

            name =data.get('name')
            color = data.get('color')
            price = data.get('price')
            description = data.get('description')
            company=data.get('company')
            fix=Product()
            fix.name=name
            fix.color=color
            fix.price=price
            fix.description=description
            fix.company=company
            fix.save()
            return JsonResponse(to_dict(fix))
    def update(self,request:HttpRequest)->JsonResponse:
        if request.method == 'POST':
            
            product = [to_dict(product)]

            return JsonResponse(product, safe=False)
        else:
            try:
                product = Product.objects.get(id=id)
                company= Company
                company.name='Samsung'
                company.description='Samsung is a South Korean company'
                company.website= "https://wwww.samsung.com/"
                company.save()
                prod = Product
                prod.name ='Samsung Galaxy  S21'
                prod.color = "red"
                company=Company.objects.get(id=company('company'))
                prod.save()

               
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def delete_produck(self,request:HttpRequest)->JsonResponse:
        if request.method == 'POST':
            
            product = [to_dict(product)]

            return JsonResponse(product, safe=False)
        else:
            try:
                product = Product.objects.get(id=id)
                product.delete()
           
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def get_all_companys(self,request:HttpRequest)->JsonResponse:
         
        '''get products'''
        if id is None:
            # get all products
            companys = Company.objects.all()

            # list of products
            products_list = [to_dict(company) for company in companys]

            return JsonResponse(products_list, safe=False)
        else:
            try:
                company = Product.objects.get(id=id)
                return JsonResponse(to_dict(company))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def add_company(self,request:HttpRequest)->JsonResponse:
        if request.method == 'POST':
            data=request.body

            decodet=data.decode()
            data = json.loads(decodet)

            name =data.get('name')
            description = data.get('description')
            website =data.get('https://samsung.com')
            fixs=Company
            fixs.name=name
            fixs.description = description
            fixs.website = website
            fixs.save()
            return JsonResponse(to_dict(fixs))
    def get_all_catigory(self,request:HttpRequest)->JsonResponse:
        
        if id is None:
            # get all products
            products = Category.objects.all()

            # list of products
            products_list = [to_dict(product) for product in products]

            return JsonResponse(products_list, safe=False)
        else:
            try:
                products = Product.objects.get(id=id)
                return JsonResponse(to_dict(products))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def get_category_products(self,request:HttpRequest)->JsonResponse:
        if request.method == 'GET':
            data=request.body

            decodet=data.decode()
            data = json.loads(decodet)

            products =data.get('products')
            cate=Category
            cate.products= products
            products_list = [to_dict(product) for product in products]

            return JsonResponse(products_list, safe=False)
        else:
            try:
                product = Category.objects.get(id=id)
                return JsonResponse(to_dict(product))
            except ObjectDoesNotExist:
                return JsonResponse({'status': 'does not exist'}, status=404)
    def add_category(self,request:HttpRequest)->JsonResponse:
        if request.method == 'POST':
            data=request.body

            decodet=data.decode()
            data = json.loads(decodet)

            products =data.get('products')
            name = data.get('name')
            cate=Category
            cate.products= products
            cate.name= name
            cate.save()
            return JsonResponse(to_dict(cate))

            

            


