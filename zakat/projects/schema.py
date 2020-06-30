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
    requests = graphene.List(RequestSchema)
    project = graphene.Field(ProjectSchema, id=graphene.Int())
    projects = graphene.List(ProjectSchema)
    campaign = graphene.Field(CampaignSchema, id=graphene.Int())
    campaigns = graphene.List(CampaignSchema)

    def resolve_requests(self, info, **kwargs):
        return Request.objects.all()
    def resolve_request(self, info, id=graphene.Int()):
        return Request.objects.get(id=id)

    def resolve_projects(self, info, **kwargs):
        return Project.objects.all()
    def resolve_project(self, info, id=graphene.Int()):
        return Project.objects.get(id=id)

    def resolve_campaigns(self, info, **kwargs):
        return Campaign.objects.all()
    def resolve_campaign(self, info, id=graphene.Int()):
        return Campaign.objects.get(id=id)
