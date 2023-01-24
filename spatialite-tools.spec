Summary:	Collection of CLI utilities supporting SpatiaLite
Summary(pl.UTF-8):	Zestaw narzędzi linii poleceń obsługujących bazy SpatiaLite
Name:		spatialite-tools
Version:	5.0.0
Release:	1
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/%{name}-%{version}.tar.gz
# Source0-md5:	e7a836fe205431c233fbf2f05ac0fcd0
URL:		https://www.gaia-gis.it/fossil/spatialite-tools
BuildRequires:	expat-devel >= 1.95
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	librttopo-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	minizip-devel
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	readline-devel
BuildRequires:	readosm-devel >= 1.1.0
BuildRequires:	sqlite3-devel >= 3
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
