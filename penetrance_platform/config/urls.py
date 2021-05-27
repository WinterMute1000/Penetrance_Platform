from django.conf.urls import url
from ..port_scan import views as port_scan_view
from ..information_disclosure import views as information_disclosure_view
from ..xss import views as xss_view
from ..sql_injection import views as sql_injection_view
from ..xxe import views as xxe_view
"""penetrance_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    url(
        regex=r"^$",
        view=port_scan_view.PortScanView.as_view(),
        name="port_scan"
    ),
    url(
        regex=r"^(port_scan)$",
        view=port_scan_view.PortScanView.as_view(),
        name="port_scan"
    ),
    url(
        regex=r"^(information_disclosure)$",
        view=information_disclosure_view.InformationDisclosureView.as_view(),
        name="information_disclosure"
    ),
    url(
        regex=r"^(xss)$",
        view=xss_view.XSSView.as_view(),
        name="xss"
    ),
    url(
        regex=r"^(sql_injection)$",
        view=sql_injection_view.SQLInjectionView.as_view(),
        name="sql_injection"
    ),
    url(
        regex=r"^(xxe)$",
        view=xxe_view.XXEView.as_view(),
        name="xxe"
    ),
]
