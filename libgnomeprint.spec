%define lib_major   0
%define libname	%mklibname gnomeprint2-2_ %{lib_major}
%define libnamedev %mklibname -d gnomeprint2-2

Summary: GNOME print library
Name: libgnomeprint
Version: 2.18.7
Release: %mkrel 1
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
License: LGPLv2+
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
BuildRequires: intltool


%description
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{libname}
Summary:	Library for GNOME print support
Group:		%{group}

Requires:	%{name} >= %{version}

%description -n %{libname}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

%package -n %{libnamedev}
Summary:	Static libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}2-2-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Requires:	%{name} = %{version}
Obsoletes: %mklibname -d gnomeprint2-2_ 0

%description -n %{libnamedev}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html


%prep
%setup -q

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


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
  
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif


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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libgnomeprint-2-2.so.%{lib_major}*

%files -n %{libnamedev}
%defattr(-,root,root)
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*
