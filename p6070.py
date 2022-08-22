season = input()
season = int(season)
if (season == 12) or (season == 1) or (season == 2) :
    print('winter')
else : 
    if (season == 3) or (season == 4) or (season == 5) :
        print('spring')
    else :
        if (season == 6) or (season == 7) or (season == 8) :
            print('summer')
        else :
            if (season == 9) or (season == 10) or (season == 11) :
                print('fall')
            else :
                print('none')
    
