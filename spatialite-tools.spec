Summary:	Collection of CLI utilities supporting SpatiaLite
Summary(pl.UTF-8):	Zestaw narzędzi linii poleceń obsługujących bazy SpatiaLite
Name:		spatialite-tools
Version:	5.1.0a
Release:	1
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/%{name}-%{version}.tar.gz
# Source0-md5:	bbd752730e1638e03d2555b184f1f5bd
URL:		https://www.gaia-gis.it/fossil/spatialite-tools
BuildRequires:	expat-devel >= 1.95
BuildRequires:	libspatialite-devel >= 5.1
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel
BuildRequires:	readosm-devel >= 1.1.0
BuildRequires:	sqlite3-devel >= 3
Requires:	libspatialite >= 5.1
Requires:	readosm >= 1.1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Collection of CLI utilities supporting SpatiaLite.

%description -l pl.UTF-8
Zestaw narzędzi linii poleceń obsługujących bazy SpatiaLite.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/exif_loader
%attr(755,root,root) %{_bindir}/shp_doctor
%attr(755,root,root) %{_bindir}/shp_sanitize
%attr(755,root,root) %{_bindir}/spatialite*
