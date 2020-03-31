import graphene
# from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType, ObjectType
from .models import  Request, Project, Campaign 

class RequestSchema(DjangoObjectType):
    class Meta:
        model = Request

class ProjectSchema(DjangoObjectType):
    class Meta:
        model = Project

class CampaignSchema(DjangoObjectType):
    class Meta:
        model = Campaign

class Query(object):
    request = graphene.Field(RequestSchema, id=graphene.Int())
    all_requests = graphene.List(RequestSchema)
    project = graphene.Field(ProjectSchema, id=graphene.Int())
    all_projects = graphene.List(ProjectSchema)
    campaign = graphene.Field(CampaignSchema, id=graphene.Int())
    all_campaigns = graphene.List(CampaignSchema)

    def resolve_all_users(self, info, **kwargs):
        return User.objects.all()
    def resolve_user(self, info, **kwargs):
        return User.objects.get(**kwargs)

    def resolve_all_projects(self, info, **kwargs):
        return Project.objects.all()
    def resolve_project(self, info, **kwargs):
        return Project.objects.get(**kwargs)

    def resolve_all_campaigns(self, info, **kwargs):
        return Campaign.objects.all()
    def resolve_Campaign(self, info, **kwargs):
        return Campaign.objects.get(**kwargs)
