%include	/usr/lib/rpm/macros.perl
Summary:	HTML-PageIndex perl module
Summary(pl):	Modu� perla HTML-PageIndex
Name:		perl-HTML-PageIndex
Version:	0.2
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTML/HTML-PageIndex-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTML-PageIndex is a slass to create HTML page index objects.

%description -l pl
HTML-PageIndex jest klas� do tworzenia stron indeksowych w HTML

%prep
%setup -q -n HTML-PageIndex-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTML/PageIndex
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/HTML/PageIndex.pm
%{perl_sitearch}/auto/HTML/PageIndex

%{_mandir}/man3/*
