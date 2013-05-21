%define upstream_name    Test-Memory-Cycle
%define upstream_version 1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Check for memory leaks and circular memory references
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl(Devel::Cycle) >= 1.07
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple) >= 0.62
BuildRequires:	perl(CGI)
BuildRequires:	perl-devel
Requires:	perl(Devel::Cycle) >= 1.07
BuildArch: 	    noarch

%description 
Perl's garbage collection has one big problem: Circular references can't get
cleaned up. A circular reference can be as simple as two objects that refer to
each other. Test::Memory::Cycle is built on top of Devel::Cycle to give you an
easy way to check for these circular references.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*


%changelog
* Tue Jan 24 2012 Oden Eriksson <oeriksson@mandriva.com> 1.40.0-3mdv2012.0
+ Revision: 767860
- fix deps
- rebuilt for perl-5.14.2

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.40.0-1mdv2010.0
+ Revision: 405553
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 1.04-5mdv2009.0
+ Revision: 258520
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.04-4mdv2009.0
+ Revision: 246540
- rebuild

* Wed Jan 02 2008 Olivier Blin <blino@mandriva.org> 1.04-2mdv2008.1
+ Revision: 140721
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-2mdv2008.0
+ Revision: 86968
- rebuild


* Fri Aug 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.04-1mdv2007.0
- New version 1.04

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-4mdk
- Fix Requires and BuildRequires

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-3mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Requires
	- Source URL

* Thu Sep 29 2005 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-2mdk
- Fix BuildRequires

* Wed Jun 01 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.02-1mdk 
- new version 
- rpmbuildupdate aware
- spec cleanup
- make test in %%check

* Wed Feb 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.00-1mdk
- 1.00
- make test belongs to build, not install
- requires, buildrequires

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-3mdk
- fix buildrequires in a backward compatible way

* Sat Aug 28 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-2mdk 
- fix directory ownership (distlint)

* Mon Mar 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.02-1mdk
- first mdk release

