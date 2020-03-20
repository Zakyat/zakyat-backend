import graphene
from graphene_django.debug import DjangoDebug

import accounts.schema


class Query(
	accounts.schema.Query,
	graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query)
