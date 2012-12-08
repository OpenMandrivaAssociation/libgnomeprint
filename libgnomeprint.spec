%define api 2-2
%define major 0
%define libname %mklibname gnomeprint %{api} %{major}
%define develname %mklibname -d gnomeprint%{api}

Summary:	GNOME print library
Name:		libgnomeprint
Version:	2.18.8
Release:	4
License:	LGPLv2+
Group:		System/Libraries
Url:		http://www.levien.com/gnome/print-arch.html
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
# debian
Patch0:		12_cups-transport.patch

BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	gtk-doc >= 1.2
BuildRequires:	intltool
BuildRequires:	pkgconfig(libart-2.0)
BuildRequires:	pkgconfig(libbonobo-2.0)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(libgnomecups-1.0)

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

%package -n %{develname}
Summary:	Development libraries, include files for GNOME print
Group:		Development/GNOME and GTK+
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}
Obsoletes:	%{mklibname -d gnomeprint2-2_ 0} < 2.18.8-4

%description -n %{develname}
This is an implementation of the Gnome Printing Architecture, as
described in:

   http://www.levien.com/gnome/print-arch.html

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

%files -n %{develname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/*
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*



%changelog
* Fri Dec 23 2011 Matthew Dawkins <mattydaw@mandriva.org> 2.18.8-3
+ Revision: 744900
- added p0 from debian to fix build
- more fixes/cleanups to spec
- rebuild
- cleaned up spec
- converted BRs to pkgconfig provides

* Fri Apr 29 2011 Oden Eriksson <oeriksson@mandriva.com> 2.18.8-2
+ Revision: 660256
- mass rebuild

* Tue Sep 28 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.8-1mdv2011.0
+ Revision: 581738
- update to new version 2.18.8

* Tue Mar 30 2010 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.7-1mdv2010.1
+ Revision: 529687
- update to new version 2.18.7

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.18.6-3mdv2010.1
+ Revision: 520849
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.18.6-2mdv2010.0
+ Revision: 425556
- rebuild

* Fri Mar 06 2009 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.6-1mdv2009.1
+ Revision: 349818
- update to new version 2.18.6

* Tue Sep 23 2008 Frederic Crozat <fcrozat@mandriva.com> 2.18.5-2mdv2009.0
+ Revision: 287191
- Remove unneeded calls to autotools

* Mon Sep 22 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.5-1mdv2009.0
+ Revision: 286811
- new version
- update license

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 2.18.4-3mdv2009.0
+ Revision: 225639
- rebuild
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Feb 12 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.4-1mdv2008.1
+ Revision: 166444
- new version

* Mon Jan 28 2008 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.3-1mdv2008.1
+ Revision: 159248
- new version

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 2.18.2-2mdv2008.1
+ Revision: 150621
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Sep 17 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.2-1mdv2008.0
+ Revision: 89136
- new version

* Wed Aug 08 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.1-1mdv2008.0
+ Revision: 60255
- new version
- new devel name


* Tue Mar 13 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.18.0-1mdv2007.1
+ Revision: 142150
- new version
- readd ChangeLog

  + Thierry Vignaud <tvignaud@mandriva.com>
    - no need to package big ChangeLog when NEWS is already there

* Mon Feb 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.92-1mdv2007.1
+ Revision: 126088
- new version

* Mon Feb 12 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.91-1mdv2007.1
+ Revision: 119850
- new version

* Mon Jan 22 2007 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.90-1mdv2007.1
+ Revision: 112103
- new version

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.17.0-1mdv2007.1
+ Revision: 87582
- new version

* Mon Nov 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 2.12.1-8mdv2007.1
+ Revision: 87546
- Import libgnomeprint

* Sat Sep 02 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-8mdv2007.0
- Rebuild, fix Mdv bug #23630

* Sat Jul 01 2006 Stefan van der Eijk <stefan@eijk.nu> 2.12.1-1mdv2007.0
- libgnutls rebuild

* Fri Feb 24 2006 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-6mdk
- Use mkrel

* Fri Nov 18 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-5mdk
- Rebuild with latest openssl

* Wed Oct 19 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-4mdk
- Remove cups-devel in buildrequires (already in libgnomecups-devel)

* Sun Oct 09 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-3mdk
- fix buildrequires

* Sat Oct 08 2005 Götz Waschk <waschk@mandriva.org> 2.12.1-2mdk
- fix buildrequires

* Fri Oct 07 2005 Frederic Crozat <fcrozat@mandriva.com> 2.12.1-1mdk
- Release 2.12.1

* Fri May 13 2005 Götz Waschk <waschk@mandriva.org> 2.10.3-3mdk
- fix buildrequires

* Tue May 10 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.3-2mdk 
- Fix build on x86-64

* Thu Apr 21 2005 Frederic Crozat <fcrozat@mandriva.com> 2.10.3-1mdk 
- Release 2.10.3 (based on Götz Waschk package)
- Remove patches 0, 1 (merged upstream)

* Tue Dec 07 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.8.2-1mdk
- New release 2.8.2

* Mon Nov 29 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.1-1mdk
- update patch 0
- New release 2.8.1

* Tue Nov 09 2004 Götz Waschk <waschk@linux-mandrake.com> 2.8.0.1-1mdk
- New release 2.8.0.1
- Remove patch0 (merged upstream)
- Patch0 (Fedora): Asynchronous query of PPD files
- Patch1 (Fedora): Asynchronous update printer list

* Thu Jun 24 2004 Götz Waschk <waschk@linux-mandrake.com> 2.6.2-1mdk
- reenable libtoolize
- New release 2.6.2

* Fri Apr 23 2004 Goetz Waschk <waschk@linux-mandrake.com> 2.6.1-1mdk
- New release 2.6.1

* Thu Apr 22 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-2mdk
- Fix BuildRequires

* Sat Apr 03 2004 Frederic Crozat <fcrozat@mandrakesoft.com> 2.6.0-1mdk
- Release 2.6.0 (with Götz help)
- Patch0 (gw) : fix doctype

