%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	PageIndex
Summary:	HTML::PageIndex perl module
Summary(pl):	Modu³ perla HTML::PageIndex
Name:		perl-HTML-PageIndex
Version:	0.3
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::PageIndex is a slass to create HTML page index objects.

%description -l pl
HTML::PageIndex jest klas± do tworzenia stron indeksowych w HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/HTML/PageIndex.pm
%{_mandir}/man3/*
