%define modname	Test-Memory-Cycle
%define modver	1.06

Summary:	Check for memory leaks and circular memory references
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Test/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
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

%description 
Perl's garbage collection has one big problem:	Circular references can't get
cleaned up. A circular reference can be as simple as two objects that refer to
each other. Test::Memory::Cycle is built on top of Devel::Cycle to give you an
easy way to check for these circular references.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Test
%{_mandir}/man3/*

