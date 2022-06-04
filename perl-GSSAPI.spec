#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-GSSAPI
Version  : 0.28
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/A/AG/AGROLMS/GSSAPI-0.28.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AG/AGROLMS/GSSAPI-0.28.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-1.0
Requires: perl-GSSAPI-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : e2fsprogs-dev
BuildRequires : krb5-dev

%description
GSSAPI Perlbindings version 0.28
=================================
GSSAPI - Perl extension for using
GSSAPI C-Bindings as described in RFC 2744.

%package dev
Summary: dev components for the perl-GSSAPI package.
Group: Development
Provides: perl-GSSAPI-devel = %{version}-%{release}
Requires: perl-GSSAPI = %{version}-%{release}

%description dev
dev components for the perl-GSSAPI package.


%package perl
Summary: perl components for the perl-GSSAPI package.
Group: Default
Requires: perl-GSSAPI = %{version}-%{release}

%description perl
perl components for the perl-GSSAPI package.


%prep
%setup -q -n GSSAPI-0.28
cd %{_builddir}/GSSAPI-0.28

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/GSSAPI.3
/usr/share/man/man3/GSSAPI::OID.3
/usr/share/man/man3/GSSAPI::OID::Set.3
/usr/share/man/man3/GSSAPI::Status.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
