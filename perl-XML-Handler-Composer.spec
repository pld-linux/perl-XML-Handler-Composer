#
# Conditional build:
%bcond_without tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	Handler-Composer
Summary:	XML::Handler::Composer - another XML printer/writer/generator
Summary(pl):	XML::Handler::Composer - jeszcze jeden modu³ do drukowania/pisania/generowania XML-a
Name:		perl-XML-Handler-Composer
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38dbb960176ee73f66e6a3c9ded75647
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-XML-UM
%endif
Obsoletes:	perl-libxml-enno
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XML::Handler::Composer Perl module is similar to XML::Writer,
XML::Handler::XMLWriter, XML::Handler::YAWriter etc. in that it
generates XML output.

%description -l pl
XML::Handler::Composer to modu³ Perla podobny do modu³ów XML::Writer,
XML::Handler::XMLWriter, XML::Handler::YAWriter itp. pod tym wzglêdem,
¿e generuje wyj¶cie XML.

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
%{perl_vendorlib}/XML/Handler/Composer.pm
%{_mandir}/man3/*
