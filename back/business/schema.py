import graphene

class Queries(
    graphene.ObjectType
):
    business = graphene.String()


schema = graphene.Schema(query=Queries)