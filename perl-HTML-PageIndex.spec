%include	/usr/lib/rpm/macros.perl
%define	pdir	HTML
%define	pnam	PageIndex
Summary:	HTML::PageIndex - class to create HTML page index objects
Summary(pl):	HTML::PageIndex - klasa do tworzenia obiektów stron indeksowych w HTML-u
Name:		perl-HTML-PageIndex
Version:	0.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1586ce9b8dfab1178224ef35a1c556e9
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML::PageIndex is a class to create HTML page index objects.

%description -l pl
HTML::PageIndex jest klas± do tworzenia stron indeksowych w HTML-u.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/HTML/PageIndex.pm
%{_mandir}/man3/*
