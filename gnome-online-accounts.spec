#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnome-online-accounts
Version  : 3.30.2
Release  : 26
URL      : https://download.gnome.org/sources/gnome-online-accounts/3.30/gnome-online-accounts-3.30.2.tar.xz
Source0  : https://download.gnome.org/sources/gnome-online-accounts/3.30/gnome-online-accounts-3.30.2.tar.xz
Summary  : Single sign-on framework for GNOME
Group    : Development/Tools
License  : LGPL-2.0
Requires: gnome-online-accounts-data = %{version}-%{release}
Requires: gnome-online-accounts-lib = %{version}-%{release}
Requires: gnome-online-accounts-libexec = %{version}-%{release}
Requires: gnome-online-accounts-license = %{version}-%{release}
Requires: gnome-online-accounts-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : e2fsprogs-dev
BuildRequires : gettext
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : krb5-dev
BuildRequires : libc-bin
BuildRequires : libxslt-bin
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(gio-unix-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(rest-0.7)
BuildRequires : pkgconfig(webkit2gtk-4.0)

%description
GNOME Online Accounts - Single sign-on framework for GNOME
==========================================================

%package data
Summary: data components for the gnome-online-accounts package.
Group: Data

%description data
data components for the gnome-online-accounts package.


%package dev
Summary: dev components for the gnome-online-accounts package.
Group: Development
Requires: gnome-online-accounts-lib = %{version}-%{release}
Requires: gnome-online-accounts-data = %{version}-%{release}
Provides: gnome-online-accounts-devel = %{version}-%{release}

%description dev
dev components for the gnome-online-accounts package.


%package lib
Summary: lib components for the gnome-online-accounts package.
Group: Libraries
Requires: gnome-online-accounts-data = %{version}-%{release}
Requires: gnome-online-accounts-libexec = %{version}-%{release}
Requires: gnome-online-accounts-license = %{version}-%{release}

%description lib
lib components for the gnome-online-accounts package.


%package libexec
Summary: libexec components for the gnome-online-accounts package.
Group: Default
Requires: gnome-online-accounts-license = %{version}-%{release}

%description libexec
libexec components for the gnome-online-accounts package.


%package license
Summary: license components for the gnome-online-accounts package.
Group: Default

%description license
license components for the gnome-online-accounts package.


%package locales
Summary: locales components for the gnome-online-accounts package.
Group: Default

%description locales
locales components for the gnome-online-accounts package.


%prep
%setup -q -n gnome-online-accounts-3.30.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549903955
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
export SOURCE_DATE_EPOCH=1549903955
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-online-accounts
cp COPYING %{buildroot}/usr/share/package-licenses/gnome-online-accounts/COPYING
%make_install
%find_lang gnome-online-accounts

%files
%defattr(-,root,root,-)

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

%files lib
%defattr(-,root,root,-)
/usr/lib64/goa-1.0/web-extensions/libgoawebextension.so
/usr/lib64/libgoa-1.0.so.0
/usr/lib64/libgoa-1.0.so.0.0.0
/usr/lib64/libgoa-backend-1.0.so.1
/usr/lib64/libgoa-backend-1.0.so.1.0.0

%files libexec
%defattr(-,root,root,-)
/usr/libexec/goa-daemon
/usr/libexec/goa-identity-service

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnome-online-accounts/COPYING

%files locales -f gnome-online-accounts.lang
%defattr(-,root,root,-)

