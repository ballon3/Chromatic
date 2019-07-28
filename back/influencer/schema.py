import graphene

class Queries(
    graphene.ObjectType
):
    influencer = graphene.String()


schema = graphene.Schema(query=Queries)