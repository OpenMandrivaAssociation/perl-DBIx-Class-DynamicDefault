%define upstream_name    DBIx-Class-DynamicDefault
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Automatically set and update fields
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/DBIx-Class-DynamicDefault
Source0:	https://cpan.metacpan.org/authors/id/M/MS/MSTROUT/DBIx-Class-DynamicDefault-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(DBD::SQLite)
BuildRequires:	perl(DBICx::TestDatabase)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(parent)

BuildArch:	noarch

%description
Automatically set and update fields with values calculated at runtime.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.30.0-2mdv2011.0
+ Revision: 654904
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2011.0
+ Revision: 471396
- adding missing buildrequires:
- import perl-DBIx-Class-DynamicDefault


* Sun Nov 29 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist
