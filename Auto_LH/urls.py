from django.urls import path, include
from Auto_LH.GB_Script import urls_gb
from Auto_LH.HC_Script import urls_hc
from Auto_LH.HP_Script import urls_hp
from Auto_LH.CS_Script import urls_cs


urlpatterns = [
    path("GB/",  include(urls_gb)),
    path("HC/",  include(urls_hc)),
    path("HP/",  include(urls_hp)),
    path("CS/",  include(urls_cs)),
]