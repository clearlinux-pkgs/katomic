#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : katomic
Version  : 23.04.3
Release  : 57
URL      : https://download.kde.org/stable/release-service/23.04.3/src/katomic-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/katomic-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/katomic-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GFDL-1.2 GPL-2.0
Requires: katomic-bin = %{version}-%{release}
Requires: katomic-data = %{version}-%{release}
Requires: katomic-license = %{version}-%{release}
Requires: katomic-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : libkdegames-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n katomic-23.04.3
cd %{_builddir}/katomic-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688857969
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688857969
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/katomic
cp %{_builddir}/katomic-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/katomic/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/katomic-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/katomic/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/katomic-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/katomic/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/katomic-%{version}/LICENSES/GFDL-1.2-or-later.txt %{buildroot}/usr/share/package-licenses/katomic/7697008f58568e61e7598e796eafc2a997503fde || :
cp %{_builddir}/katomic-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/katomic/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang katomic
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/katomic
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
/usr/share/knsrcfiles/katomic.knsrc
/usr/share/metainfo/org.kde.katomic.appdata.xml
/usr/share/qlogging-categories5/katomic.categories

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
/usr/share/package-licenses/katomic/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/katomic/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/katomic/7697008f58568e61e7598e796eafc2a997503fde
/usr/share/package-licenses/katomic/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/katomic/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c

%files locales -f katomic.lang
%defattr(-,root,root,-)

