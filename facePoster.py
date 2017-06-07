import facebook


# this is working and the token should be infinite

def main(msg):
    graph = facebook.GraphAPI(
        "EAAYZBui8MtxsBAJi3hO29GKwHJHITOmstUHoyXquKsSH0RGGKkbwSxSWPESo4iaSEpLnVR9iVks8P0lFrm2ahlkn4QhgbicC3FZC8tK9wT0XEn4sF6VeRKl3XA3KLYwy6fGfPNXwIeQ9aoUtBezK3IHbpDxKcZD",
        version='2.7')
    graph.put_object("206114322854301", "feed", message=msg)
