from unicodedata import name
from django.urls import path

from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('favourite',views.favourite,name='favourite'),
    path('addfavourite/<str:pk>',views.addfavourite,name='addfavourite'),
    path('signin',views.signin,name='signin'),
    path('logout',views.logout,name="logout"),
    path('createaccount',views.createaccount,name='createaccount'),
    path('googleadword',views.googleadword ,name="googleadword"),
    path('googleanalytics',views.googleanalytics ,name="googleanalytics"),
    path('googleappmaker',views.googleappmaker ,name="googleappmaker"),
    path('googlecalendar',views.googlecalendar ,name="googlecalendar"),
    path('googlechat',views.googlechat ,name="googlechat"),
    path('googlechrome',views.googlechrome ,name="googlechrome"),
    path('googlecontacts',views.googlecontacts ,name="googlecontacts"),
    path('googledocs',views.googledocs ,name="googledocs"),
    path('googledrawing',views.googledrawing ,name="googledrawing"),
    path('googledrive',views.googledrive ,name="googledrive"),
    path('googleearth',views.googleearth ,name="googleearth"),
    path('googleforms',views.googleforms ,name="googleforms"),
    path('googlegmail',views.googlegmail ,name="googlegmail"),
    path('googlegroups',views.googlegroups ,name="googlegroups"),
    path('googlehangout',views.googlehangout ,name="googlehangout"),
    path('googlekeep',views.googlekeep ,name="googlekeep"),
    path('googlemeet',views.googlemeet ,name="googlemeet"),
    path('googlephotos',views.googlephotos ,name="googlephotos"),
    path('googlesheet',views.googlesheet ,name="googlesheet"),
    path('googlesite',views.googlesite ,name="googlesite"),
    path('googleslides',views.googleslides ,name="googleslides"),
    path('googlewebdesigner',views.googlewebdesigner ,name="googlewebdesigner"),
    path('googleyoutube',views.googleyoutube ,name="googleyoutube"),

    path('microsoftcalendar',views.microsoftcalendar ,name="microsoftcalendar"),
    path('microsoftedge',views.microsoftedge ,name="microsoftedge"),
    path('microsoftexcel',views.microsoftexcel ,name="microsoftexcel"),
    path('microsoftgamebar',views.microsoftgamebar ,name="microsoftgamebar"),
    path('microsoftgroove',views.microsoftgroove ,name="microsoftgroove"),
    path('microsoftmail',views.microsoftmail ,name="microsoftmail"),
    path('microsoftmap',views.microsoftmap ,name="microsoftmap"),
    path('microsoftmoviesandtv',views.microsoftmoviesandtv ,name="microsoftmoviesandtv"),
    path('microsoftoutlook',views.microsoftoutlook ,name="microsoftoutlook"),
    path('microsoftpaint',views.microsoftpaint ,name="microsoftpaint"),
    path('microsoftpaint3d',views.microsoftpaint3d ,name="microsoftpaint3d"),
    path('microsoftphotos',views.microsoftphotos ,name="microsoftphotos"),
    path('microsoftpowerpoint',views.microsoftpowerpoint ,name="microsoftpowerpoint"),
    path('microsoftskype',views.microsoftskype ,name="microsoftskype"),
    path('microsoftteams',views.microsoftteams ,name="microsoftteams"),
    path('microsoftvoicerecorder',views.microsoftvoicerecorder ,name="microsoftvoicerecorder"),
    path('microsoftwindows',views.microsoftwindows ,name="microsoftwindows"),
    path('microsoftword',views.microsoftword ,name="microsoftword"),
    path('microsoftworkpad',views.microsoftworkpad ,name="microsoftworkpad"),
    
    path('ciscowebex',views.ciscowebex ,name="ciscowebex"),
    path('zoom',views.zoom ,name="zoom"),
    path('twitter',views.twitter ,name="twitter"),
    path('whatsapp',views.whatsapp ,name="whatsapp"),

    path('brave',views.brave ,name="brave"),
    path('firefox',views.firefox ,name="firefox"),
    path('internet explorer',views.internet_explorer,name="internet explorer"),
    path('whatsapp',views.whatsapp ,name="whatsapp"),

    path('browsers',views.browsers,name="browsers"),
    path('socialmedia',views.socialmedia,name="socialmedia"),
    path('google',views.google,name='google'),
    path('microsoft',views.microsoft,name='microsoft'),

    #pages:
    path('privacyandpolicy',views.privacyandpolicy, name="privacyandpolicy"),
    path('termsandconditions',views.termsandconditions,name="termsandconditions"),
    path('contactus',views.contactus,name="contactus"),
    path('aboutus',views.aboutus,name="aboutus"),
    path('contact',views.contact,name="contact"),

]