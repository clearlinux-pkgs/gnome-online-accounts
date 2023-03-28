#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gnome-online-accounts
Version  : 3.48.0
Release  : 51
URL      : https://download.gnome.org/sources/gnome-online-accounts/3.48/gnome-online-accounts-3.48.0.tar.xz
Source0  : https://download.gnome.org/sources/gnome-online-accounts/3.48/gnome-online-accounts-3.48.0.tar.xz
Summary  : Backends for GNOME Online Accounts Library
Group    : Development/Tools
License  : LGPL-2.0
Requires: gnome-online-accounts-data = %{version}-%{release}
Requires: gnome-online-accounts-lib = %{version}-%{release}
Requires: gnome-online-accounts-libexec = %{version}-%{release}
Requires: gnome-online-accounts-license = %{version}-%{release}
Requires: gnome-online-accounts-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : json-glib-dev
BuildRequires : krb5-dev
BuildRequires : libc-bin
BuildRequires : pkgconfig(gcr-3)
BuildRequires : pkgconfig(javascriptcoregtk-4.1)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libsecret-1)
BuildRequires : pkgconfig(rest-1.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: backport-gcr.patch

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
Requires: gnome-online-accounts = %{version}-%{release}

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
%setup -q -n gnome-online-accounts-3.48.0
cd %{_builddir}/gnome-online-accounts-3.48.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680029678
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gnome-online-accounts
cp %{_builddir}/gnome-online-accounts-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnome-online-accounts/21e40770dfa802576ee515345cef47ecedff6524 || :
DESTDIR=%{buildroot} ninja -C builddir install
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
/usr/share/icons/hicolor/scalable/apps/goa-account-exchange.svg
/usr/share/icons/hicolor/scalable/apps/goa-account-fedora.svg
/usr/share/icons/hicolor/scalable/apps/goa-account-google.svg
/usr/share/icons/hicolor/scalable/apps/goa-account-lastfm.svg
/usr/share/icons/hicolor/scalable/apps/goa-account-msn.svg
/usr/share/icons/hicolor/scalable/apps/goa-account-owncloud.svg
/usr/share/icons/hicolor/scalable/apps/goa-account.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-exchange-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-google-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-lastfm-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-msn-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-owncloud-symbolic.svg
/usr/share/icons/hicolor/symbolic/apps/goa-account-symbolic.svg
/usr/share/vala/vapi/goa-1.0.deps
/usr/share/vala/vapi/goa-1.0.vapi

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
/usr/share/package-licenses/gnome-online-accounts/21e40770dfa802576ee515345cef47ecedff6524

%files locales -f gnome-online-accounts.lang
%defattr(-,root,root,-)

