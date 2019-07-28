import graphene

class Queries(
    graphene.ObjectType
):
    offer = graphene.String()


schema = graphene.Schema(query=Queries)