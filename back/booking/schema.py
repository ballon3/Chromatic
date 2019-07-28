import graphene

class Queries(
    graphene.ObjectType
):
    booking = graphene.String()


schema = graphene.Schema(query=Queries)