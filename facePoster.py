import facebook
from config import facebook_token     

# this is working and the token should be infinite

def main(msg):
    graph = facebook.GraphAPI(
        facebook_token ,
        version='2.7')
    graph.put_object("206114322854301", "feed", message=msg)
