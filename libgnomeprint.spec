%define lib_major   0
%define lib_name	%mklibname gnomeprint2-2_ %{lib_major}

Summary: GNOME print library
Name: libgnomeprint
Version: 2.18.0
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPL
Group: System/Libraries
Url: http://www.levien.com/gnome/print-arch.html
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires: libart_lgpl-devel
BuildRequires: libbonobo2_x-devel
BuildRequires: pango-devel >= 1.5
BuildRequires: libgnomecups-devel >= 0.2
BuildRequires: bison
BuildRequires: flex
BuildRequires: gtk-doc >= 1.2
BuildRequires: perl-XML-Parser
#if patched
BuildRequires: automake1.7
BuildRequires: intltool

%description
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{lib_name}
Summary:	Library for GNOME print support
Group:		%{group}

Requires:	%{name} >= %{version}

%description -n %{lib_name}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{lib_name}-devel
Summary:	Static libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}2-2-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{lib_name} = %{version}
Requires:	%{name} = %{version}
Requires:   libart_lgpl-devel
Requires:   libbonobo2_x-devel

%description -n %{lib_name}-devel
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html


%prep
%setup -q

#fix build on x86-64
aclocal-1.7
automake-1.7
autoconf

%build

%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall_std

%find_lang %{name}-2.2

#remove unpackaged files
rm -f $RPM_BUILD_ROOT%{_libdir}/libgnomeprint/%{version}/modules/*.{la,a} \
 $RPM_BUILD_ROOT%{_libdir}/libgnomeprint/%{version}/modules/*/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT


%post -n %{lib_name} -p /sbin/ldconfig
  
%postun -n %{lib_name} -p /sbin/ldconfig


%files -f %{name}-2.2.lang
%defattr(-,root,root)
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

%files -n %{lib_name}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*


