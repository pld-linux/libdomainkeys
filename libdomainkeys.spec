Summary:	DomainKey Library for email servers & clients
Summary(pl.UTF-8):	Biblioteka DomainKey dla serwerów i klientów poczty elektronicznej
Name:		libdomainkeys
Version:	0.69
Release:	3
License:	Yahoo! DomainKeys Public License Agreement v1.1
Group:		Libraries
Source0:	http://downloads.sourceforge.net/domainkeys/%{name}-%{version}.tar.gz
# Source0-md5:	15ec065c6f645a0b9fde3f1ff7681127
Patch0:		%{name}-libtool.patch
Patch1:		%{name}-segv.patch
Patch2:		%{name}-dknewkey.patch
Patch3:		openssl.patch
URL:		http://domainkeys.sourceforge.net/
BuildRequires:	libtool >= 2:1.5
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
%patch3 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -DBIND_8_COMPAT" \
	LDFLAGS="%{rpmldflags}"
	libdir=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

libtool --mode=install install libdomainkeys.la $RPM_BUILD_ROOT%{_libdir}
libtool --mode=install install dknewkey dktest $RPM_BUILD_ROOT%{_bindir}
cp -p dktrace.h domainkeys.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.html CHANGES
%attr(755,root,root) %{_bindir}/dknewkey
%attr(755,root,root) %{_bindir}/dktest
%attr(755,root,root) %{_libdir}/libdomainkeys.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libdomainkeys.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdomainkeys.so
%{_libdir}/libdomainkeys.la
%{_includedir}/dktrace.h
%{_includedir}/domainkeys.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libdomainkeys.a
