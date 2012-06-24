Summary:	Gnome integrated development environment
Summary(pl):	Zintegrowane �rodowisko programowania dla Gnome
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	0.1.9
Release:	10
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/anjuta/%{name}-%{version}.tar.gz
# Source0-md5:	645a108a816b30ecff1df13395e6ce00
Patch0:		%{name}-ac_am.patch
Patch1:		%{name}-no_systemtags.patch
Patch2:		%{name}-omf.patch
Patch3:		%{name}-module_no_version.patch
Patch4:		%{name}-use_AM_CXXFLAGS.patch
Patch5:		%{name}-desktop_fix.patch
Patch6:		%{name}-desktop.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bonobo-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-vfs-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
BuildRequires:	gnomemm-devel
Requires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _prefix         /usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

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
%setup  -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
xml-i18n-toolize --copy --force
%{__aclocal} -I macros
%{__autoconf}
%{__automake}
echo "all install:">plugins/sample1/Makefile.in
CXXFLAGS="%{rpmcflags} -fno-exceptions"
%configure \
	--with-gnome \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name} \
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
