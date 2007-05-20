Summary:	Disk Speed Graphs
Name:		bogodisk
Version:	0.5.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://sweaglesw.com/~djwong/programs/bogodisk/%{name}-%{version}.tar.gz
# Source0-md5:	cd047128e1c7bb8e1e1f59213523e6d8
URL:		http://sweaglesw.com/~djwong/programs/bogodisk/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Disk throughput benchmarking tool.

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
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
