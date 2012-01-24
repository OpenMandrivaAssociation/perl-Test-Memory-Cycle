%define upstream_name    Test-Memory-Cycle
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary: 	Check for memory leaks and circular memory references
License: 	GPL+ or Artistic
Group: 		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}/
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2
BuildRequires:	perl(Devel::Cycle) >= 1.07
BuildRequires:	perl(Getopt::Long)
BuildRequires:	perl(PadWalker)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Simple) >= 0.62
BuildRequires:	perl(CGI)
Requires:	perl(Devel::Cycle) >= 1.07
BuildArch: 	    noarch
BuildRoot: 	    %{_tmppath}/%{name}-%{version}-%{release}

%description 
Perl's garbage collection has one big problem: Circular references can't get
cleaned up. A circular reference can be as simple as two objects that refer to
each other. Test::Memory::Cycle is built on top of Devel::Cycle to give you an
easy way to check for these circular references.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor </dev/null
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test
%{_mandir}/*/*
