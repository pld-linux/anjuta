Summary:	Gnome integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko programowania dla Gnome
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
Anjuta is a very versatile integrated development environment for C
and C++ GNU/Linux. Written in GTK/Gnome and written for GTK/Gnome, it
features many advanced programming tools and utilities. Besides many
other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l pl
Anjuta to wszechstronne zintegrowane ¶rodowisko programowania dla jêzyka
C oraz C++. Zosta³o napisane z wykorzystaniem tandemu GTK/Gnome, w³a¶nie
po to by go w takim otoczeniu u¿ywaæ. Miêdzy innymi posiada zarz±dcê
projektów, kreator aplikacji, wbudowany interaktywny odpluskwiacz oraz
edytor z mo¿liwo¶ci± przegl±dania ¼róde³.

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
