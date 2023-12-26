import database
from flask import Flask, render_template

def homePage():
    #database veri çek
    #sayfayı renderla döndür
    return render_template("home.html")    


def userProfile(id):
    return 'User bilmemne id : ' + str(id)