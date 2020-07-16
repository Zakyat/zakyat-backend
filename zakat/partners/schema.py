import graphene
from graphene_django.types import DjangoObjectType
from .models import Partner


class PartnerSchema(DjangoObjectType):
    class Meta:
        model = Partner


class Query(object):
    partner = graphene.Field(PartnerSchema, id=graphene.Int())
    partners = graphene.List(PartnerSchema)

    def resolve_partner(self, info, id=graphene.Int()):
        return Partner.objects.get(id)

    def resolve_partners(self, info, **kwargs):
        return Partner.objects.all()
