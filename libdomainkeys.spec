Summary:	DomainKey Library for email servers & clients
Summary(pl.UTF-8):	Biblioteka DomainKey dla serwerów i klientów poczty elektronicznej
Name:		libdomainkeys
Version:	0.68
Release:	7
License:	Yahoo! DomainKeys Public License Agreement v1.1
Group:		Libraries
Source0:	http://dl.sourceforge.net/domainkeys/%{name}-%{version}.tar.gz
# Source0-md5:	c9fe164d6296e7ad5468580875ac4f2e
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-segv.patch
Patch2:		%{name}-dknewkey.patch
URL:		http://domainkeys.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
Requires:	mktemp
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DomainKey Library for email servers & clients.

%description -l pl.UTF-8
Biblioteka DomainKey dla serwerów i klientów poczty elektronicznej.

%package devel
Summary:	Header files for libdomainkeys library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libdomainkeys
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	openssl-devel

%description devel
Header files for libdomainkeys library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libdomainkeys.

%package static
Summary:	Static libdomainkeys library
Summary(pl.UTF-8):	Statyczna biblioteka libdomainkeys
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libdomainkeys library.

%description static -l pl.UTF-8
Statyczna biblioteka libdomainkeys.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DBIND_8_COMPAT"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

libtool --mode=install install dknewkey dktest $RPM_BUILD_ROOT%{_bindir}
install dktrace.h domainkeys.h $RPM_BUILD_ROOT%{_includedir}
libtool --mode=install install libdomainkeys.la $RPM_BUILD_ROOT%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.html CHANGES
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
