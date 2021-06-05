from rest_framework import viewsets
from blog.models import Tag, Article
from blog.serializers import ArticleSerializer, TagSerializer

# Create your views here.
class TagViewSet(viewsets.ModelViewSet):
	serializer_class = TagSerializer
	queryset = Tag.objects.all()
	

class ArticleViewSet(viewsets.ModelViewSet):
	queryset = Article.objects.filter(is_public=True)
	serializer_class = ArticleSerializer
	lookup_field = 'slug'
