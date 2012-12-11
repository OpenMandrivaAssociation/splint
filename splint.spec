%define name    splint 
%define version 3.1.2
%define release %mkrel 5

Name:           %{name} 
Summary:        Splint - Secure Programming Lint
Version:        %{version} 
Release:        %{release} 
Source0:        http://www.splint.org/downloads/splint-%{version}.tar.bz2
URL:            http://www.splint.org
Group:          Development/C
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot 
License:        GPL
BuildRequires: flex

%description
Splint is a tool for statically checking C programs for security
vulnerabilities and coding mistakes. With minimal effort, Splint can
be used as a better lint. If additional effort is invested adding
annotations to programs, Splint can perform stronger checking than can
be done by any standard lint.

%prep
%setup -q

%build 
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


%clean 
rm -rf %buildroot

%files 
%defattr(0755,root,root,0755) 
%{_bindir}/splint
%defattr(0644,root,root,0755)
%doc README
%{_mandir}/man1/splint.1*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*


%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.1.2-5mdv2010.0
+ Revision: 434058
- rebuild

* Sat Aug 02 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1.2-4mdv2009.0
+ Revision: 260951
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.1.2-3mdv2009.0
+ Revision: 252956
- rebuild
- fix spacing at top of description

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 3.1.2-1mdv2008.1
+ Revision: 127555
- kill re-definition of %%buildroot on Pixel's request

  + Couriousous <couriousous@mandriva.org>
    - 3.1.2
    - Import splint



* Thu Oct 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 3.1.1-2mdk
- Fix BuildRequires
- %%mkrel 

* Sat Dec 11 2004 Couriousous <couriousous@mandrake.org> 3.1.1-1mdk
- Minors spec fix
- Disabled parallal build
- From: Christophe Vu-Brugier <cvu-brugier@netcourrier.com>
	- First build for Mandrakelinux.
