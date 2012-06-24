# TODO:
# - port to libtool && produce shared library

Summary:	DomainKey Library for email servers & clients
Name:		libdomainkeys
Version:	0.65a
Release:	1
License:	Yahoo! DomainKeys Public License Agreement v1.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/domainkeys/%{name}-%{version}.tar.gz
# Source0-md5:	7d246213e832e86a25e1741063266a34
URL:		http://domainkeys.sourceforge.net/
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DomainKey Library for email servers & clients.

%package devel
Summary:	Header files for libdomainkeys library
Summary(pl):	Pliki nag��wkowe biblioteki libdomainkeys
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel

%description devel
Header files for libdomainkeys library.

%description devel -l pl
Pliki nag��wkowe biblioteki libdomainkeys.

%package static
Summary:	Static libdomainkeys library
Summary(pl):	Statyczna biblioteka libdomainkeys
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdomainkeys library.

%description static -l pl
Statyczna biblioteka libdomainkeys.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DBIND_8_COMPAT"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}}

install domainkeys.h $RPM_BUILD_ROOT%{_includedir}
install *.a $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.html CHANGES
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/*.a
#%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

#%files devel
#%defattr(644,root,root,755)
#%attr(755,root,root) %{_libdir}/lib*.so
#%{_libdir}/lib*.la
#%dir %{_includedir}/*.h

#%files static
#%defattr(644,root,root,755)
#%{_libdir}/lib*.a
