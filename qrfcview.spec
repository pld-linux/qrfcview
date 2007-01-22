#
# TODO: - don't know how to deal with rest images
#
Summary:	Smart viewer for IETF RFCs
Summary(pl):	Sprytna przegl±darka dokumentów RFC
Name:		qrfcview	
Version:	0.62
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/qrfcview/%{name}-%{version}.tgz
# Source0-md5:	836783d9c327237f4b1aa40de6b4376a
Source1:	%{name}.desktop
URL:		http://qrfcview.berlios.de/	
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qRFCView is a viewer for IETF RFCs. Advantages are:
 - automatic table of content, with direct opening of section;
 - handling of RFC internal cross-references;
 - automatic downloading of a referenced RFC from the IETF web site on
   a simple click;
 - caching of RFC in a local directory;
 - tab-browsing of RFC;
 - searching. 

%description -l pl
qRFCView to przegl±darka dla RFC z IETF. Jej zalety to:
 - automatyczny spis tre¶ci, z bezpo¶rednim otwieraniem sekcji
 - obs³uga wewnêtrznych odno¶ników w RFC
 - automatyczne ¶ci±ganie wzmiankowanych RFC ze strony WWW IETF
   prostym klikniêciem
 - zapamiêtywanie RFC w lokalnym katalogu
 - przegl±danie RFC z u¿yciem zak³adek
 - wyszukiwanie

%prep
%setup -q
%{__sed} -i '1s@^@#include <stdint.h>@' src/*.{cpp,h}

%build
export QTDIR="%{_prefix}"
qt4-qmake
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

install bin/qRFCView $RPM_BUILD_ROOT%{_bindir}/qrfcview
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install images/rfcview.png $RPM_BUILD_ROOT%{_pixmapsdir}/qrfcview.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
