#%%define		snap	20030425

Summary:	GNOME integrated development environment
Summary(pl):	Zintegrowane �rodowisko programowania dla GNOME
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	1.1.98
Release:	2
Epoch:		1
License:	GPL
Group:		Development/Tools
#Source0:	%{name}-%{version}-%{snap}.tar.bz2
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	cd4a048c856831d5eaddd6e78de3169c
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-home_etc.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	ORBit2-devel >= 2.8.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 2.2.0
BuildRequires:	intltool
BuildRequires:	gnome-common >= 2.4.0
BuildRequires:	gnome-vfs2-devel >= 2.4.0
BuildRequires:	libglade2-devel >= 2.0.1
BuildRequires:	libgnomeprintui-devel >= 2.4.0
BuildRequires:	libgnomeui-devel >= 2.4.0
BuildRequires:	libxml2-devel >= 2.4.2
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.11.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anjuta is a very versatile integrated development environment for C
and C++ GNU/Linux. Written in GTK/GNOME and written for GTK/GNOME, it
features many advanced programming tools and utilities. Besides many
other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l pl
Anjuta to wszechstronne zintegrowane �rodowisko programowania dla
j�zyka C oraz C++. Zosta�o napisane z wykorzystaniem tandemu
GTK/GNOME, w�a�nie po to by go w takim otoczeniu u�ywa�. Mi�dzy innymi
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
%setup -q
%patch0 -p0
%patch1 -p1

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
CFLAGS="%{rpmcflags} -fno-omit-frame-pointer"
rm -f missing
#%%{__gettextize}
#intltoolize
%{__libtoolize}
%{__aclocal} -I /usr/share/aclocal/gnome2-macros
%{__autoheader}
%{__autoconf}
%{__automake}
#./autogen.sh
%configure \
	--disable-static \
	--enable-gprof
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/lib*.la

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /usr/bin/scrollkeeper-update
%postun -p /usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE NEWS README TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/anjuta
%attr(755,root,root) %{_libdir}/anjuta/lib*.so*
%{_pixmapsdir}/anjuta
%{_datadir}/anjuta
%{_datadir}/mime-info/*
%{_datadir}/mimelnk/application/*
%{_desktopdir}/*
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
