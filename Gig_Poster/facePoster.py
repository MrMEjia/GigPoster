import facebook


# this is working and the token should be infinite

def main(msg):
    graph = facebook.GraphAPI(
        "EAAYZBui8MtxsBAH1uZCZBCe4CIFGyxT3Kw8IOpyF7K2YoBjG6d5Ydx9yWxBexYQZBZCQMu5djjmgkhGQlh6ZC9R3VeirpWuToXEDAjcX0uBJu3EwzNFfwmwTll0aqLq46E7xxPU0aZBAhMSZCQnDEzh5ElbrvupWUZAUZD",
        version='2.7')
    graph.put_object("206114322854301", "feed", message=msg)
