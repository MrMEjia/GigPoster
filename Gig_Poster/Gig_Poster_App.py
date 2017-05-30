import Get_Gig
import facePoster

gig = Get_Gig.main()

if gig:
    msg = "My gig tonight is: " + gig
    facePoster.main(msg)
