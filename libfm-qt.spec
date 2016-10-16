%define		qtver		5.3.1

Summary:	libfm-qt
Name:		libfm-qt
Version:	0.11.1
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	http://downloads.lxqt.org/libfm-qt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	ebff48dbcec7169cdac2a81a79c050db
URL:		http://www.lxqt.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	Qt5Xml-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.3
BuildRequires:	libfm-devel >= 1.2.0
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-linguist >= %{qtver}
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libfm-qt.

%package devel
Summary:	libfm-qt - header files and development documentation
Summary(pl.UTF-8):	libfm-qt - pliki nagłówkowe i dokumentacja do kdelibs
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libfm-qt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących fm-qt.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS:BOOL=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
    DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%ghost %{_libdir}/libfm-qt.so.3
%attr(755,root,root) %{_libdir}/libfm-qt.so.3.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libfm-qt
%attr(755,root,root) %{_libdir}/libfm-qt.so
%{_pkgconfigdir}/libfm-qt.pc
%{_datadir}/cmake/fm-qt
