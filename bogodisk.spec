Summary:	Disk Speed Graphs
Summary(pl.UTF-8):	Wykresy szybkości dysku
Name:		bogodisk
Version:	0.5.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://sweaglesw.com/~djwong/programs/bogodisk/%{name}-%{version}.tar.gz
# Source0-md5:	43a17fc39f700999e0339ca5f2cb6c98
Patch0:		%{name}-as-needed.patch
URL:		http://sweaglesw.com/~djwong/programs/bogodisk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk throughput benchmarking tool.

%description -l pl.UTF-8
Narzędzie do pomiaru przepustowości dysku.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
