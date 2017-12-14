#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-online-accounts
Version  : 3.26.2
Release  : 18
URL      : https://download.gnome.org/sources/gnome-online-accounts/3.26/gnome-online-accounts-3.26.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-online-accounts/3.26/gnome-online-accounts-3.26.2.tar.xz
Summary  : GNOME Online Accounts Library
Group    : Development/Tools
License  : LGPL-2.1
Requires: gnome-online-accounts-data
Requires: gnome-online-accounts-lib
Requires: gnome-online-accounts-bin
Requires: gnome-online-accounts-locales
Requires: gnome-online-accounts-doc
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : gobject-introspection-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool
BuildRequires : krb5-dev
BuildRequires : libc-bin
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(dbus-glib-1)
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gudev-1.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(rest-0.7)
BuildRequires : pkgconfig(webkit2gtk-4.0)

%description
GNOME Online Accounts - Single sign-on framework for GNOME
==========================================================

%package bin
Summary: bin components for the gnome-online-accounts package.
Group: Binaries
Requires: gnome-online-accounts-data

%description bin
bin components for the gnome-online-accounts package.


%package data
Summary: data components for the gnome-online-accounts package.
Group: Data

%description data
data components for the gnome-online-accounts package.


%package dev
Summary: dev components for the gnome-online-accounts package.
Group: Development
Requires: gnome-online-accounts-lib
Requires: gnome-online-accounts-bin
Requires: gnome-online-accounts-data
Provides: gnome-online-accounts-devel

%description dev
dev components for the gnome-online-accounts package.


%package doc
Summary: doc components for the gnome-online-accounts package.
Group: Documentation

%description doc
doc components for the gnome-online-accounts package.


%package lib
Summary: lib components for the gnome-online-accounts package.
Group: Libraries
Requires: gnome-online-accounts-data

%description lib
lib components for the gnome-online-accounts package.


%package locales
Summary: locales components for the gnome-online-accounts package.
Group: Default

%description locales
locales components for the gnome-online-accounts package.


%prep
%setup -q -n gnome-online-accounts-3.26.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1513290176
%configure --disable-static --disable-inspector \
--disable-telepathy \
--enable-kerberos
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1513290176
rm -rf %{buildroot}
%make_install
%find_lang gnome-online-accounts

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/goa-daemon
/usr/libexec/goa-identity-service

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/Goa-1.0.typelib
/usr/share/dbus-1/services/org.gnome.Identity.service
/usr/share/dbus-1/services/org.gnome.OnlineAccounts.service
/usr/share/gir-1.0/*.gir
/usr/share/glib-2.0/schemas/org.gnome.online-accounts.gschema.xml
/usr/share/icons/hicolor/16x16/apps/goa-account-facebook.png
/usr/share/icons/hicolor/16x16/apps/goa-account-flickr.png
/usr/share/icons/hicolor/16x16/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/16x16/apps/goa-account-google.png
/usr/share/icons/hicolor/16x16/apps/goa-account-msn.png
/usr/share/icons/hicolor/16x16/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/16x16/apps/goa-account-pocket.png
/usr/share/icons/hicolor/16x16/apps/goa-account-todoist.png
/usr/share/icons/hicolor/16x16/apps/goa-account.png
/usr/share/icons/hicolor/22x22/apps/goa-account-facebook.png
/usr/share/icons/hicolor/22x22/apps/goa-account-flickr.png
/usr/share/icons/hicolor/22x22/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/22x22/apps/goa-account-google.png
/usr/share/icons/hicolor/22x22/apps/goa-account-msn.png
/usr/share/icons/hicolor/22x22/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/22x22/apps/goa-account-pocket.png
/usr/share/icons/hicolor/22x22/apps/goa-account-todoist.png
/usr/share/icons/hicolor/22x22/apps/goa-account.png
/usr/share/icons/hicolor/24x24/apps/goa-account-facebook.png
/usr/share/icons/hicolor/24x24/apps/goa-account-flickr.png
/usr/share/icons/hicolor/24x24/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/24x24/apps/goa-account-google.png
/usr/share/icons/hicolor/24x24/apps/goa-account-msn.png
/usr/share/icons/hicolor/24x24/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/24x24/apps/goa-account-pocket.png
/usr/share/icons/hicolor/24x24/apps/goa-account-todoist.png
/usr/share/icons/hicolor/24x24/apps/goa-account.png
/usr/share/icons/hicolor/256x256/apps/goa-account.png
/usr/share/icons/hicolor/32x32/apps/goa-account-facebook.png
/usr/share/icons/hicolor/32x32/apps/goa-account-flickr.png
/usr/share/icons/hicolor/32x32/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/32x32/apps/goa-account-google.png
/usr/share/icons/hicolor/32x32/apps/goa-account-msn.png
/usr/share/icons/hicolor/32x32/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/32x32/apps/goa-account-pocket.png
/usr/share/icons/hicolor/32x32/apps/goa-account-todoist.png
/usr/share/icons/hicolor/32x32/apps/goa-account.png
/usr/share/icons/hicolor/48x48/apps/goa-account-facebook.png
/usr/share/icons/hicolor/48x48/apps/goa-account-flickr.png
/usr/share/icons/hicolor/48x48/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/48x48/apps/goa-account-google.png
/usr/share/icons/hicolor/48x48/apps/goa-account-msn.png
/usr/share/icons/hicolor/48x48/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/48x48/apps/goa-account-pocket.png
/usr/share/icons/hicolor/48x48/apps/goa-account-todoist.png
/usr/share/icons/hicolor/48x48/apps/goa-account.png
/usr/share/icons/hicolor/96x96/apps/goa-account-facebook.png
/usr/share/icons/hicolor/96x96/apps/goa-account-flickr.png
/usr/share/icons/hicolor/96x96/apps/goa-account-foursquare.png
/usr/share/icons/hicolor/96x96/apps/goa-account-google.png
/usr/share/icons/hicolor/96x96/apps/goa-account-msn.png
/usr/share/icons/hicolor/96x96/apps/goa-account-owncloud.png
/usr/share/icons/hicolor/96x96/apps/goa-account-pocket.png
/usr/share/icons/hicolor/96x96/apps/goa-account-todoist.png
/usr/share/icons/hicolor/96x96/apps/goa-account.png

%files dev
%defattr(-,root,root,-)
/usr/include/goa-1.0/goa/goa-generated.h
/usr/include/goa-1.0/goa/goa.h
/usr/include/goa-1.0/goa/goaclient.h
/usr/include/goa-1.0/goa/goaenums.h
/usr/include/goa-1.0/goa/goaenumtypes.h
/usr/include/goa-1.0/goa/goaerror.h
/usr/include/goa-1.0/goa/goaversion.h
/usr/include/goa-1.0/goabackend/goabackend.h
/usr/include/goa-1.0/goabackend/goabackendenums.h
/usr/include/goa-1.0/goabackend/goabackendenumtypes.h
/usr/include/goa-1.0/goabackend/goaprovider.h
/usr/lib64/goa-1.0/include/goaconfig.h
/usr/lib64/libgoa-1.0.so
/usr/lib64/libgoa-backend-1.0.so
/usr/lib64/pkgconfig/goa-1.0.pc
/usr/lib64/pkgconfig/goa-backend-1.0.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/goa-1.0/web-extensions/libgoawebextension.so
/usr/lib64/libgoa-1.0.so.0
/usr/lib64/libgoa-1.0.so.0.0.0
/usr/lib64/libgoa-backend-1.0.so.1
/usr/lib64/libgoa-backend-1.0.so.1.0.0

%files locales -f gnome-online-accounts.lang
%defattr(-,root,root,-)

