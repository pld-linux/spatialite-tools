Summary:	Collection of CLI utilities supporting SpatiaLite
Summary(pl.UTF-8):	Zestaw narzędzi linii poleceń obsługujących bazy SpatiaLite
Name:		spatialite-tools
Version:	4.0.0
Release:	1
License:	GPL v3+
Group:		Applications/Databases
Source0:	http://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/%{name}-%{version}.tar.gz
# Source0-md5:	2eab56d3a91ae872d985e32a3623ec6f
URL:		https://www.gaia-gis.it/fossil/spatialite-tools
BuildRequires:	expat-devel >= 1.95
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	libspatialite-devel
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	readline-devel
BuildRequires:	readosm-devel
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
%attr(755,root,root) %{_bindir}/spatialite*
