Summary:	Gnome integrated development environment
Name:		anjuta
Version:	0.1.4
Release:	0
License:	GPL
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	http://anjuta.sourceforge.net/packages/14/%{name}-%{version}.tar.gz
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
