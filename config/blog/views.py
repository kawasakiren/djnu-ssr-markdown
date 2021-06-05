from rest_framework import viewsets
from blog.models import Tag, Article
from blog.permissions import IsAdminOrReadOnly
from blog.serializers import ArticleSerializer, TagSerializer
from blog.paginations import CustomPagination

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
	serializer_class = TagSerializer
	queryset = Tag.objects.all()
	permission_classes = (IsAdminOrReadOnly,)
	

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.filter(is_public=True)
	serializer_class = ArticleSerializer
	permission_classes = (IsAdminOrReadOnly,)
	pagination_class = CustomPagination
	lookup_field = 'slug'
