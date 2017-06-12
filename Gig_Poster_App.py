#!/usr/bin/python



import Get_Gig
import facePoster

gig_list = Get_Gig.main()

gig = ""

if len(gig_list) > 1:
    gig = gig_list[0] + " and " + gig_list[1]
else:
    gig = gig_list[0]

if gig:
    msg = "Come on out for some live music. I will playing today at " + gig
    facePoster.main(msg)
