import graphene
from graphene_django.debug import DjangoDebug

import accounts.schema
<<<<<<< HEAD
import payment.schema


class Query(
	accounts.schema.Query,
	payment.schema.Query,
=======
import projects.schema

class Query(
	accounts.schema.Query,
	projects.schema.Query,
>>>>>>> #8 add schema for Projects App
	graphene.ObjectType,
):
    debug = graphene.Field(DjangoDebug, name="_debug")

schema = graphene.Schema(query=Query)
