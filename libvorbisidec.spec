# https://salsa.debian.org/multimedia-team/libvorbisidec

%global commit0 d3152d0d43981086f01b1f625239cda6b3659ef9
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

#%define _legacy_common_support 1
#%global _lto_cflags %{nil}
%global debug_package %{nil}

Name:          libvorbisidec
Version:       1.2.1
Release:       2%{?dist}
Summary:       A fixed-point version of the Ogg Vorbis decoder for platforms that can' do floating point math
URL:           http://wiki.xiph.org/Tremor

Source:        https://salsa.debian.org/multimedia-team/libvorbisidec/-/archive/%{commit0}/libvorbisidec-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

License:       GPLv2

BuildRequires: glibc-devel 
BuildRequires: libtool
BuildRequires: libogg-devel
BuildRequires: gcc-c++

%description
The Tremor Vorbis I stream and file decoder provides an embeddable,
integer-only library [libvorbisidec] intended for decoding all current
and future Vorbis I compliant streams. The Tremor libvorbisidec library
exposes an API intended to be as similar as possible to the familiar
'vorbisfile' library included with the open source Vorbis reference
libraries distributed for free by Xiph.org.

%package devel
Group:         Development/Libraries
Summary:       Static libraries and headers for %{name}
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
A fixed-point version of the Ogg Vorbis decoder for platforms that can' do floating point math.
This package contains static libraries and header files need for development.

%prep
%autosetup -n %{name}-%{commit0}

%build
./autogen.sh
./configure --prefix=/usr --libdir=%{_libdir}
%make_build

%install
%make_install

rm -f %{buildroot}/%{_libdir}/*.a
rm -f %{buildroot}/%{_libdir}/*la


%files
%{_libdir}/*.so.*
%doc COPYING

%files devel
%{_prefix}/include/tremor/*.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%doc README

%changelog

* Mon Apr 19 2021 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.1-2
- Rebuilt

* Mon Sep 14 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.1-1
- Updated to 1.2.1

* Thu Jul 16 2020 Unitedrpms Project <unitedrpms AT protonmail DOT com> 1.2.0-1
- Initial build
