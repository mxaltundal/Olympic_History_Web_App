import database

def homePage():
    #database veri çek
    #sayfayı renderla döndür
    return 'home_page'    


def userProfile(id):
    return 'User bilmemne id : ' + str(id)