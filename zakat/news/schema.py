import graphene
from graphene_django.types import DjangoObjectType
from .models import Post


class PostSchema(DjangoObjectType):
	class Meta:
		model = Post

class Query(object):
    post = graphene.Field(PostSchema, id=graphene.Int())
    posts = graphene.List(PostSchema)

    def resolve_post(self, info, id=graphene.Int()):
        return Post.objects.get(id)
    def resolve_posts(self, info, **kwargs):
        return Post.objects.all()
