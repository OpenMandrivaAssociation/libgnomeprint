%define url_ver %(echo %{version}|cut -d. -f1,2)

%define api	2-2
%define major	0
%define libname %mklibname gnomeprint %{api} %{major}
%define devname %mklibname -d gnomeprint%{api}

Summary:	GNOME print library
Name:		libgnomeprint
Version:	2.18.8
Release:	7
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.levien.com/gnome/print-arch.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnomeprint/%{url_ver}/%{name}-%{version}.tar.bz2
# debian
Patch0:		12_cups-transport.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc >= 1.2
BuildRequires:	intltool
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libbonobo-2.0)
BuildRequires:	pkgconfig(libgnomecups-1.0)
BuildRequires:	pkgconfig(pangoft2)

%description
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{libname}
Summary:	Library for GNOME print support
Group:		%{group}

%description -n %{libname}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{devname}
Summary:	Development libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d gnomeprint2-2_ 0} < 2.18.8-4

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

%find_lang %{name}-2.2

%files -f %{name}-2.2.lang
%doc README AUTHORS NEWS
%dir %{_libdir}/libgnomeprint
%dir %{_libdir}/libgnomeprint/%{version}
%dir %{_libdir}/libgnomeprint/%{version}/modules
%dir %{_libdir}/libgnomeprint/%{version}/modules/transports
%dir %{_libdir}/libgnomeprint/%{version}/modules/filters
%{_libdir}/libgnomeprint/%{version}/modules/*.so
%{_libdir}/libgnomeprint/%{version}/modules/transports/*.so
%{_libdir}/libgnomeprint/%{version}/modules/filters/*.so
%{_datadir}/libgnomeprint

%files -n %{libname}
%{_libdir}/libgnomeprint-%{api}.so.%{major}*

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

