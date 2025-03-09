
wellness_komplett = input("Haben sie Wellness-Komplettpaket gebucht ? (ja/nein): ").lower()  
drei_uebernachtungen = input("Haben sie für min. drei Tage gebucht ? (ja/nein): ").lower()    
vollpension = input("Haben sie Vollpension ? (ja/nein): ").lower()

def Entscheidung(wellness, drei_ue, voll_p):             
    if wellness == "ja" and drei_ue == "ja" and voll_p == "ja":          
        wellness and drei_ue and voll_p                           
        return "Frühstück + Abendbrot , Mittagessen, Fünf Freigetränke, Freie Nutzung des Fitnessraums, Saunabesuch gratis, Eine Massage gratis"
    elif wellness == "ja" and drei_ue == "ja" and voll_p == "nein":          
        wellness and drei_ue                         
        return "Frühstück + Abendbrot , Fünf Freigetränke, Freie Nutzung des Fitnessraums, Saunabesuch gratis, Eine Massage gratis"
    elif wellness == "ja" and drei_ue == "nein" and voll_p == "ja":          
        wellness and voll_p                           
        return "Frühstück + Abendbrot , Mittagessen, Fünf Freigetränke, Freie Nutzung des Fitnessraums, Saunabesuch gratis, Eine Massage gratis"
    elif wellness == "ja" and drei_ue == "nein" and voll_p == "nein":          
        wellness                          
        return "Frühstück + Abendbrot , Fünf Freigetränke, Freie Nutzung des Fitnessraums, Saunabesuch gratis, Eine Massage gratis"
    elif wellness == "nein" and drei_ue == "ja" and voll_p == "ja":          
        drei_ue and voll_p                           
        return "Frühstück + Abendbrot , Mittagessen, Fünf Freigetränke, Freie Nutzung des Fitnessraums, Saunabesuch gratis "  
    elif wellness == "nein" and drei_ue == "ja" and voll_p == "nein":          
        drei_ue                          
        return "Frühstück + Abendbrot , Freie Nutzung des Fitnessraums, Saunabesuch gratis"  
    elif wellness == "nein" and drei_ue == "nein" and voll_p == "ja":          
        voll_p                           
        return "Frühstück + Abendbrot , Mittagessen, Fünf Freigetränke, Freie Nutzung des Fitnessraums"
    elif wellness == "nein" and drei_ue == "nein" and voll_p == "nein":                                    
        return "Frühstück + Abendbrot , Freie Nutzung des Fitnessraums"  
        


print(Entscheidung(wellness_komplett, drei_uebernachtungen, vollpension))          

