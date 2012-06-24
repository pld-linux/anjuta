%define snap 2002-10-24-15
Summary:	Gnome integrated development environment
Summary(pl):	Zintegrowane �rodowisko programowania dla Gnome
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	1.0.
Release:	0.%(echo %{snap} | sed 's/-//g').1
License:	GPL
Group:		Development/Tools
Source0:	http://anjuta.sourceforge.net/cvs/anjuta-cvs-HEAD-hourly-%{snap}.tar.gz
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-no_systemtags.patch
Patch2:		%{name}-omf.patch
Patch3:		%{name}-module_no_version.patch
Patch4:		%{name}-use_AM_CXXFLAGS.patch
Patch5:		%{name}-desktop_fix.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
BuildRequires:	libgnomeui-devel >= 2.0.5
BuildRequires:	libgnomeprintui-devel >= 1.116.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Anjuta is a very versatile integrated development environment for C
and C++ GNU/Linux. Written in GTK/Gnome and written for GTK/Gnome, it
features many advanced programming tools and utilities. Besides many
other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l pl
Anjuta to wszechstronne zintegrowane �rodowisko programowania dla
j�zyka C oraz C++. Zosta�o napisane z wykorzystaniem tandemu
GTK/Gnome, w�a�nie po to by go w takim otoczeniu u�ywa�. Mi�dzy innymi
posiada zarz�dc� projekt�w, kreator aplikacji, wbudowany interaktywny
odpluskwiacz oraz edytor z mo�liwo�ci� przegl�dania �r�de�.

%description -l pt_BR
O Anjuta � um ambiente de desenvolvimento integrado (IDE) vers�til
para as linguagens C e C++. Foi escrito para o GTK/GNOME e tem uma
s�rie de caracter�sticas de programa��o avan�adas. Basicamente � uma
interface gr�fica com o usu�rio para um conjunto de utilit�rios de
linha de comando e ferramentas para programa��o para o Linux. Estas
s�o geralmente executadas em um console em modo texto e podem ser n�o
amig�veis.

%prep
%setup -q -n %{name}

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
rm -f missing
glib-gettextize
intltoolize
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-gnome \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_applnkdir}/Development

%find_lang %{name} --with-gnome

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/anjuta
%attr(755,root,root) %{_libdir}/anjuta/lib*.so
%{_omf_dest_dir}/%{name}
%{_datadir}/anjuta
%{_applnkdir}/Development/*
%{_pixmapsdir}/*
