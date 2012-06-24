Summary:	Gnome integrated development environment
Summary(pl):	Zintegrowane �rodowisko programowania dla Gnome
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	0.1.9
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://anjuta.sourceforge.net/packages/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-ac_am.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	ORBit-devel
BuildRequires:	audiofile-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	intltool
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libxml-devel
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
BuildRequires:	libsigc++1-devel
BuildRequires:	gnomemm-devel
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

%build
libtoolize --copy --force
gettextize --copy --force
intltoolize --copy --force
xml-i18n-toolize --copy --force
aclocal -I macros
autoconf
automake -a -c -f
CXXFLAGS="%{rpmcflags} -fno-exceptions"
%configure \
	--with-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_applnkdir}/Development \
	$RPM_BUILD_ROOT%{_datadir}/%{name}/gnome

install %{SOURCE1} $RPM_BUILD_ROOT/%{_applnkdir}/Development

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	omf_dest_dir=%{_omf_dest_dir}/%{name}

gzip -9nf README ChangeLog NEWS TODO

%find_lang %{name} --with-gnome

%post   -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/anjuta
%attr(755,root,root) %{_libdir}/anjuta/lib*.so.*.*
%attr(755,root,root) %{_libdir}/anjuta/lib*.??
%{_omf_dest_dir}/%{name}
%{_datadir}/anjuta
%{_applnkdir}/Development/*
%{_pixmapsdir}/anjuta
