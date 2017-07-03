#!/usr/bin/python



import Get_Gig
import facePoster
import GigSplit
import datetime

#days = {0:"Monaday", 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 
#        5:"Saturday", 6:"Sunday"}


def main():
    today_num = datetime.date.today().weekday()
    gig_list = Get_Gig.main()
    
    if gig_list:
        if today_num == 0:
            week(gig_list)
            
        elif gig_list[0][1] == today_num:
            today_gigs = []
            for x in gig_list:
                if x[1] == today_num:
                    today_gigs.append(x[0])
            today(today_gigs)
            
        elif gig_list[0][1] == today_num + 1:
            tomorrow_gigs = []
            for x in gig_list:
                if x[1] == today_num + 1:
                    tomorrow_gigs.append(x[0])
            tomorrow(tomorrow_gigs)
            
        else: 
            pass
        
    
def week(gig_list):
    msg = "This weeks schedule. See you there! \n"
    for x in gig_list:
        for y in GigSplit.week(x[0]):
            msg += ("\n" + x[2] + ": " + y)
    facePoster.main(msg)    
    



def today(gig):
    parsed = GigSplit.day(gig)
    if parsed:
        msg = "Come on out for some live music. I will playing today at " + parsed
    facePoster.main(msg)

def tomorrow(gig):
    parsed = GigSplit.day(gig)
    if parsed:
        msg = "No gigs today, but I will be playing tomorrow at " + parsed
    facePoster.main(msg)


if __name__ == '__main__':
    main()