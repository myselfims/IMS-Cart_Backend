from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import *
from rest_framework_simplejwt import views as jwt_views

router = DefaultRouter()

router.register(r"category",CategoryViewSet)
router.register(r"offers",OffersViewSet)
router.register(r"search",SearchView)
router.register(r"cart",CartViewSet)
router.register(r"order",OrderViewSet)
router.register(r"register",RegisterViewSet)
router.register(r"wishlist",WishlistViewSet)




urlpatterns = [
    path('',include(router.urls)),
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:id>", ProductDetailView.as_view(), name="viewproduct"),
    path("gettoken/",jwt_views.TokenObtainPairView.as_view()),
    path("tokenrefresh/",jwt_views.TokenRefreshView.as_view()),
    path("tokenverify/",jwt_views.TokenVerifyView.as_view()),
    path("getuser/",UserDetaialView.as_view(),name='getuser'),
    path("verifypromo/",VerifyPromoView.as_view(),name='promocode'),
]
