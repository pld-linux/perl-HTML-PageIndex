%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	PageIndex
Summary:	HTML::PageIndex perl module
Summary(pl):	Modu� perla HTML::PageIndex
Name:		perl-HTML-PageIndex
Version:	0.2
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::PageIndex is a slass to create HTML page index objects.

%description -l pl
HTML::PageIndex jest klas� do tworzenia stron indeksowych w HTML.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTML/PageIndex.pm
%{_mandir}/man3/*
