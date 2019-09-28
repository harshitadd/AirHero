import numpy as np 

def weather():
    w,h = 8,67 
    #receive weather data - wind speed and wind direction
    return w,h

def sunlight():

    s=0
    if(s == 0):
        s_map = 'Low'
    elif(s == 1):
        s_map = 'Moderate'
    elif(s == 2):
        s_map = 'High'
    elif(s == 3):
        s_map = 'Very High'
    elif(s == 4):
        s_map = 'Extreme'
                    
    #recieve the sunlight reading from the UV sensor 
    return s,s_map

def app_data():

    a,m,n= 1,2,2
    if(a == 1):
        a_map = "More than 2 years"
    else:
        a_map = "Less than 2 years"
    #return a age of the article, m - mech ventiliation, n = number of windows  
    return a,m,n,a_map

def VOC():

    v = 55
    #recieve voc reading 
    return v



def recommend(choice,w,h,s_map,a_map,m,n,v):
    ws_tval = 4
    humidity_tval = 60
     
    if(choice == 1):
        print("High VOC and not very new product")
        if(n!=0 and s>1):
            print("Adequate sunlight is present and Room has adequate Windows ")
            if(w > ws_tval and h < humidity_tval):
                print("Good Air Dispersion")
                print('Natural Ventiliation needed')
                if(v>40):
                    t = 30
                elif(v<60): 
                    t = 45
                else:
                    t = 60
                rec = "You may want to open the windows in the room for " + t + " minutes.Please put in direct sunlight"
            elif(m!=0):
                if(m>=2):
                    t = 30
                else:
                    t = 60
                rec = "You may want to use the fans for " + t + "minutes "    
        else:
            print('Mechanical Ventiation needed')
            if(m>=2):
                t = 30
            else:
                t = 60 

    if(choice == 2):
        print("Relatively Old item yet has high VOC content")
        print("Both Mechanical as well Natural Ventiliation Required")
        if(v>40):
            print("Please use a protective varnish")
            t = 30
        elif(v<60): 
            t = 45
        else:
            t = 60
        rec = "You may want to open the windows in the room for " + str(t) + " minutes.Please put in direct sunlight"
        if(m>=2):
            t = 30
        else:
            t = 60
        rec = "You may want to use the fans for " + str(t) + "minutes " 
    else:
        print("Use plants instead")

                    
 

def algo():

    s,s_map = sunlight()
    a,m,n,a_map = app_data()
    v = VOC()
    w,h = weather()
    
    
    threshold_value = 0.1 ##highest average safe value for toluene and formaldehyde


    ##MAIN ALGORITHM 

    if v > threshold_value and a < 1:
        recommend(1,w,h,s_map,a_map,m,n,v)
        
    else:
        recommend(2,w,h,s_map,a_map,m,n,v)
    
    print("\nGENERATED REPORT FOR ANALYSIS \n\n")
    
    report(w,h,s_map,a_map,m,n,v)    

def report(w,h,s_map,a_map,m,n,v):
    print("Wind speed is "+ str(w) +" Km/h")
    print("Humidity is "+ str(h) +" %")
    print("Sunlight is "+ s_map)
    print("Age of the Article is "+ a_map)
    print("Number of mechanical ventiliation sources "+ str(m))
    print("Number of windows in the room is "+ str(n))
    print("VOC value detected from the Handheld device is "+ str(v) +" ppm")
    #print("Wind speed is "+ str(w) +" Km/h")
    
if __name__ == ('__main__'):
    algo()
