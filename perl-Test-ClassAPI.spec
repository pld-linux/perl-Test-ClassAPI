#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Test
%define		pnam	ClassAPI
Summary:	Test::ClassAPI - provides basic first-pass API testing for large class trees
Summary(pl.UTF-8):	Test::ClassAPI - podstawowy pierwszy przebieg testowania API dużych drzew klas
Name:		perl-Test-ClassAPI
Version:	1.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ff06bc671f753f4148c39df08fb6dd98
URL:		https://metacpan.org/release/Test-ClassAPI
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.83
BuildRequires:	perl-Class-Inspector >= 1.12
BuildRequires:	perl-Config-Tiny >= 2.00
BuildRequires:	perl-Params-Util >= 1.00
BuildRequires:	perl-Test-Simple >= 0.47
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For many APIs with large numbers of classes, it can be very useful to
be able to do a quick once-over to make sure that classes, methods,
and inheritance is correct, before doing more comprehensive testing.
This module aims to provide such a capability.

%description -l pl.UTF-8
Przy wielu API z dużą liczbą klas może być bardzo przydatna możliwość
wykonania szybkiego przebiegu, aby upewnić się przed rozpoczęciem
bardziej rozległego testowania, że te klasy, metody i dziedziczenie są
poprawne. Ten moduł próbuje dostarczyć taką możliwość.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/ClassAPI.pm
%{_mandir}/man3/Test::ClassAPI.3pm*
