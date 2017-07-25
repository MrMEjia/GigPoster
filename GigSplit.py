# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:17:55 2017

@author: benny
"""




def day(gigs):
    nums = "01234567890-:"
    parsed = []

    for g in gigs:
        name = ""
        time = ""
        for x in g:
            if x not in nums:
                name += x
            if x in nums:
                time += x
                
        phrase = name + "from " + time
        parsed.append(phrase)
    
    if len(parsed) < 2:
        total = parsed[0]
    else:        
        total =  parsed[0] + " and " + parsed[1]
            
    
    return(total)

def week(gig):
    nums = "01234567890-:"
    parsed = []

    
    name = ""
    time = ""
    for x in gig:
        if x not in nums:
            name += x
        if x in nums:
            time += x
            
    phrase = name + "from " + time
    parsed.append(phrase)
    
    return parsed
