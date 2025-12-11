%define		qtver		6.6.0

Summary:	Companion library for PCManFM
Summary(pl.UTF-8):	Biblioteka towarzysząca dla PCManFM
Name:		libfm-qt
Version:	2.3.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Libraries
Source0:	https://github.com/lxqt/libfm-qt/releases/download/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	d51de358b739c17a0d35e889aeb126b0
URL:		http://www.lxqt.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6Gui-devel >= %{qtver}
BuildRequires:	Qt6Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 3.18.0
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	libexif-devel
BuildRequires:	libglvnd-libGL-devel
BuildRequires:	lxqt-menu-data >= 2.3.0
BuildRequires:	menu-cache-devel >= 1.1.0
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-linguist >= %{qtver}
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-renderutil-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.9.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libfm-Qt is a companion library providing components to build desktop
file managers.

%description -l pl.UTF-8
Libfm-Qt to biblioteka towarzysząca, która udostępnia komponenty do
tworzenia menedżerów plików.

%package devel
Summary:	libfm-qt - header files and development documentation
Summary(pl.UTF-8):	libfm-qt - pliki nagłówkowe i dokumentacja do kdelibs
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt6Core-devel >= %{qtver}
Requires:	Qt6Gui-devel >= %{qtver}
Obsoletes:	razor-qt-devel

%description devel
This package contains header files and development documentation for
libfm-qt.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących libfm-qt.

%prep
%setup -q

%build
%cmake -B build

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
    DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%ghost %{_libdir}/libfm-qt6.so.17
%{_libdir}/libfm-qt6.so.17.*.*
%{_datadir}/mime/packages/libfm-qt6-mimetypes.xml
%dir %{_datadir}/libfm-qt6
# required for the lang files
%dir %{_datadir}/libfm-qt6/translations
%{_datadir}/libfm-qt6/archivers.list
%{_datadir}/libfm-qt6/terminals.list

%files devel
%defattr(644,root,root,755)
%{_includedir}/libfm-qt6
%{_libdir}/libfm-qt6.so
%{_pkgconfigdir}/libfm-qt6.pc
%{_datadir}/cmake/fm-qt6
