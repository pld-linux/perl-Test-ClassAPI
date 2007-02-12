#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	ClassAPI
Summary:	Test::ClassAPI - provides basic first-pass API testing for large class trees
Summary(pl.UTF-8):   Test::ClassAPI - podstawowy pierwszy przebieg testowania API dużych drzew klas
Name:		perl-Test-ClassAPI
Version:	1.02
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f242a7d8ca652d7207a50461e328dafc
URL:		http://search.cpan.org/dist/Test-ClassAPI/
%if %{with tests}
BuildRequires:	perl(File::Spec) >= 0.83
BuildRequires:	perl-Class-Inspector >= 1.05
BuildRequires:	perl-Config-Tiny >= 1.9
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
