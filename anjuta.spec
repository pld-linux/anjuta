Summary:	anjuta
Name:		anjuta
Version:	0.1.4
Release:	0
License:	GPL
Group:		Development/Debuggers
Source0:	anjuta-%{version}.tar.gz
URL:		http://anjuta.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup  -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README ChangeLog 

%clean
rm -rf $RPM_BUILD_ROOT
