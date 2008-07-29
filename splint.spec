%define name    splint 
%define version 3.1.2
%define release %mkrel 3 

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
