from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from api.serializers import *
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
from rest_framework.response import Response
from rest_framework import filters


# Create your views here.

class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = []
    permission_classes = []

class ProductsView(APIView):
    
    authentication_classes = []
    permission_classes = []
    
    
    def get(self,request,format=None):
        
        if request.data.get('category') != None:
            try:
                cat = Category.objects.get(name=request.data.get('category'))
                objects = Product.objects.filter(category=cat.id)
                ser = ProductsSerializer(objects,many=True)
                return Response({'products':ser.data})
            except Exception as e:
                print(e)
                return Response({'status':False,'message':'category not found!'})
        objects = Product.objects.all()
        ser = ProductsSerializer(objects,many=True)
        return Response({'products':ser.data})
    
    
    def post(self,request,format=None):
        
        if request.data.get('category') != None:
            try:
                cat = Category.objects.get(name=request.data.get('category'))
                objects = Product.objects.filter(category=cat.id)
                ser = ProductsSerializer(objects,many=True)
                return Response({'products':ser.data})
            except Exception as e:
                print(e)
                return Response({'status':False,'message':'category not found!'})
        objects = Product.objects.all()
        ser = ProductsSerializer(objects,many=True)
        return Response({'products':ser.data})
    
    
    
class ProductDetailView(APIView):


    authentication_classes = []
    permission_classes = []
    
    def get(self,request,id=None,format=None):
        print(id)
        if id != None:
            try:
                object = Product.objects.get(id=id)
                recom = Product.objects.filter(category=object.category)
                recser = ProductsSerializer(recom,many=True)
                ser = ProductsSerializer(object)
                return Response({'product':ser.data,'recomended':recser.data})
            except Exception as e:
                print(e)
                return Response({'status':False,'message':'product not found!'})

    

class OffersViewSet(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    serializer_class = OffersSerializer
    queryset = Offers.objects.all()
    
    
class SearchView(ModelViewSet):
    authentication_classes = []
    permission_classes = []
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer
    search_fields = ['name','description','color','varients']
    filter_backends = (filters.SearchFilter,)
    
class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = []
    
    def  get_queryset(self):
        cart = []
        # obj = Cart.objects.filter(user=1)
        obj = Cart.objects.filter(user=self.request.user.id)
        # print(request.user)
        return obj
    
    def create(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().update(request, *args, **kwargs)
    
    
class WishlistViewSet(ModelViewSet):
    queryset = Wishlist.objects.all()
    serializer_class = WishlistSerializer
    permission_classes = [IsAuthenticated]
    
    def  get_queryset(self):
        obj = Wishlist.objects.filter(user=self.request.user)
        return obj
    
    def create(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().update(request, *args, **kwargs)
    
class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def  get_queryset(self):
        obj = Order.objects.filter(user=self.request.user)
        return obj
    
    def create(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        request.data.update(user=request.user.id)
        return super().update(request, *args, **kwargs)
    
    
class RegisterViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    authentication_classes = []
    

    
class UserDetaialView(APIView):
    
    # authentication_classes = [IsAuthenticated]
    permission_classes = [IsAuthenticated]
    
    def post(self,request,format=None):
        try:
            username = request.data['username']
            user = User.objects.get(username=username)
            address = Address.objects.filter(user=user.id)
            userser = RegisterSerializer(user)
            addser = AddressSerializer(address,many=True)
            return Response({"user":userser.data,"address":addser.data})
        except:
            return Response({'status':False,'message':'User not found!'})
        
    def put(self,request):
        try:
            user_id = self.request.user.id
            first_name = request.data['first_name']
            last_name = request.data['last_name']
            email = request.data['email']
            mobile = request.data['mobile']
            gender = request.data['gender']
            address = request.data['address']
            print(address,mobile)
            city = request.data['city']
            pincode = request.data['pincode']
            state = request.data['state']
            
            user = User.objects.get(id=user_id)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            user.save()
            
            try:
                addr_obj = Address.objects.get(user=user)
                addr_obj.address = address
                addr_obj.mobile = mobile
                addr_obj.gender = gender
                addr_obj.city = city
                addr_obj.pincode = pincode
                addr_obj.state = state
                addr_obj.save()
            except :
                addr_obj = Address.objects.create(
                    user = user,
                    mobile = mobile,
                    address = address,
                    city = city,
                    pincode = pincode,
                    state = state 
                )
                addr_obj.save()
            
            try:
                address = Address.objects.filter(user=user_id)
                userser = RegisterSerializer(user)
                addser = AddressSerializer(address,many=True)
                return Response({"user":userser.data,"address":addser.data})
            except:
                return Response({'status':False,'message':'User not found!'})
            
            
        except Exception as e:
            print(e)
        
            return Response({"status":False,"message":"All these fields are required",
                             "first_name":'',
                             "last_name":'',
                             "email":'',
                             "mobile":'',
                             "gender":'',
                             "address":'',
                             "city":'',
                             "pincode":'',
                             "state":''
                            })

