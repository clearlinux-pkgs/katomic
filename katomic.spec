#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : katomic
Version  : 19.04.1
Release  : 9
URL      : https://download.kde.org/stable/applications/19.04.1/src/katomic-19.04.1.tar.xz
Source0  : https://download.kde.org/stable/applications/19.04.1/src/katomic-19.04.1.tar.xz
Source99 : https://download.kde.org/stable/applications/19.04.1/src/katomic-19.04.1.tar.xz.sig
Summary  : A fun and educational game built around molecular geometry
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: katomic-bin = %{version}-%{release}
Requires: katomic-data = %{version}-%{release}
Requires: katomic-license = %{version}-%{release}
Requires: katomic-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : libkdegames-dev
BuildRequires : qtbase-dev mesa-dev

%description
This file describes how to create a new KAtomic theme.
(Last update: 29.05.2007 by dimsuz)

%package bin
Summary: bin components for the katomic package.
Group: Binaries
Requires: katomic-data = %{version}-%{release}
Requires: katomic-license = %{version}-%{release}

%description bin
bin components for the katomic package.


%package data
Summary: data components for the katomic package.
Group: Data

%description data
data components for the katomic package.


%package doc
Summary: doc components for the katomic package.
Group: Documentation

%description doc
doc components for the katomic package.


%package license
Summary: license components for the katomic package.
Group: Default

%description license
license components for the katomic package.


%package locales
Summary: locales components for the katomic package.
Group: Default

%description locales
locales components for the katomic package.


%prep
%setup -q -n katomic-19.04.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557436424
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1557436424
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/katomic
cp COPYING %{buildroot}/usr/share/package-licenses/katomic/COPYING
cp COPYING.DOC %{buildroot}/usr/share/package-licenses/katomic/COPYING.DOC
pushd clr-build
%make_install
popd
%find_lang katomic

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/katomic

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.katomic.desktop
/usr/share/icons/hicolor/128x128/apps/katomic.png
/usr/share/icons/hicolor/16x16/apps/katomic.png
/usr/share/icons/hicolor/22x22/apps/katomic.png
/usr/share/icons/hicolor/32x32/apps/katomic.png
/usr/share/icons/hicolor/48x48/apps/katomic.png
/usr/share/icons/hicolor/64x64/apps/katomic.png
/usr/share/katomic/levels/default_levels.dat
/usr/share/katomic/pics/default_theme.svgz
/usr/share/kconf_update/katomic-levelset-upd.pl
/usr/share/kconf_update/katomic-levelset.upd
/usr/share/kxmlgui5/katomic/katomicui.rc
/usr/share/metainfo/org.kde.katomic.appdata.xml
/usr/share/xdg/katomic.knsrc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/katomic/index.cache.bz2
/usr/share/doc/HTML/ca/katomic/index.docbook
/usr/share/doc/HTML/de/katomic/index.cache.bz2
/usr/share/doc/HTML/de/katomic/index.docbook
/usr/share/doc/HTML/en/katomic/index.cache.bz2
/usr/share/doc/HTML/en/katomic/index.docbook
/usr/share/doc/HTML/en/katomic/mainscreen.png
/usr/share/doc/HTML/es/katomic/index.cache.bz2
/usr/share/doc/HTML/es/katomic/index.docbook
/usr/share/doc/HTML/et/katomic/index.cache.bz2
/usr/share/doc/HTML/et/katomic/index.docbook
/usr/share/doc/HTML/fr/katomic/index.cache.bz2
/usr/share/doc/HTML/fr/katomic/index.docbook
/usr/share/doc/HTML/it/katomic/index.cache.bz2
/usr/share/doc/HTML/it/katomic/index.docbook
/usr/share/doc/HTML/nl/katomic/index.cache.bz2
/usr/share/doc/HTML/nl/katomic/index.docbook
/usr/share/doc/HTML/pt/katomic/index.cache.bz2
/usr/share/doc/HTML/pt/katomic/index.docbook
/usr/share/doc/HTML/pt_BR/katomic/index.cache.bz2
/usr/share/doc/HTML/pt_BR/katomic/index.docbook
/usr/share/doc/HTML/ru/katomic/index.cache.bz2
/usr/share/doc/HTML/ru/katomic/index.docbook
/usr/share/doc/HTML/sv/katomic/index.cache.bz2
/usr/share/doc/HTML/sv/katomic/index.docbook
/usr/share/doc/HTML/uk/katomic/index.cache.bz2
/usr/share/doc/HTML/uk/katomic/index.docbook
/usr/share/doc/HTML/uk/katomic/mainscreen.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/katomic/COPYING
/usr/share/package-licenses/katomic/COPYING.DOC

%files locales -f katomic.lang
%defattr(-,root,root,-)

