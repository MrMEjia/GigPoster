#!/usr/bin/python



import Get_Gig
import facePoster
import GigSplit

gig_list = Get_Gig.main()

gig = GigSplit.main(gig_list)

if gig:
    msg = "Come on out for some live music. I will playing today at " + gig
    facePoster.main(msg)
