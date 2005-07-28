# TODO:
# - subversion plugin
# - glade-3 support
# - post/preun mime registration
# - kill scrolleeper buildtime detection
#
Summary:	GNOME integrated development environment
Summary(pl):	Zintegrowane ¶rodowisko programowania dla GNOME
Summary(es):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	2.0.1
Release:	0.1
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/anjuta/%{name}-%{version}.tar.gz
# Source0-md5:	21d765fabb35da3f2cc405e1b00eaa10
Patch0:		%{name}-gettext.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-desktop.patch
Patch3:		%{name}-build_fixes.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	autogen-devel
BuildRequires:	automake
BuildRequires:	devhelp-devel >= 0.9
BuildRequires:	gd-devel
BuildRequires:	gdl-devel >= 0.5.0
# not released yet
#BuildRequires:	glade3-devel
BuildRequires:	gnome-build-devel >= 0.1.2
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	graphviz-devel >= 2.2.1
BuildRequires:	guile-devel >= 1.6.7
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
# shouldn't be in graphviz-devel R:s? not required directly
# here
BuildRequires:	libsvg-cairo-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	ncurses-devel
# for subversion
#BuildRequires:	neon-devel >= 0.24.5
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
# broken and evil
#BuildRequires:	subversion-devel >= 1.0.2
# no documentation for now
# BuildRequires:	scrollkeeper
BuildRequires:	vte-devel >= 0.11.0
#Requires(post,postun):	scrollkeeper
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anjuta is a very versatile integrated development environment for C
and C++ for GNU/Linux. Written in GTK/GNOME and written for GTK/GNOME,
it features many advanced programming tools and utilities. Besides
many other, it has project management, application wizards, onboard
interactive debugger, and a powerful source editor with source
browsing.

%description -l es
Anjuta es un entorno integrado de desarrollo para C y C++ para
GNU/Linux. Escrito en y para GTK/GNOME, proporciona muchas
herramientas de programación avanzadas. Entre otros, habilita
manejamiento de proyectos, wizards de aplicaciones, depurador
interactivo y un editador potente de código fuente que permite
hojearlo.

%description -l pl
Anjuta to wszechstronne zintegrowane ¶rodowisko programowania dla
jêzyka C oraz C++. Zosta³o napisane z wykorzystaniem tandemu
GTK/GNOME, w³a¶nie po to by go w takim otoczeniu u¿ywaæ. Miêdzy innymi
posiada zarz±dcê projektów, kreator aplikacji, wbudowany interaktywny
odpluskwiacz oraz edytor z mo¿liwo¶ci± przegl±dania ¼róde³.

%description -l pt_BR
O Anjuta é um ambiente de desenvolvimento integrado (IDE) versátil
para as linguagens C e C++. Foi escrito para o GTK/GNOME e tem uma
série de características de programação avançadas. Basicamente é uma
interface gráfica com o usuário para um conjunto de utilitários de
linha de comando e ferramentas para programação para o Linux. Estas
são geralmente executadas em um console em modo texto e podem ser não
amigáveis.

%package libs
Summary:	Anjuta shared libraries
Summary(pl):	Bibloteki wspó³dzielone Anjuta
Group:		Development/Libraries

%description libs
Anjuta shared libraries.

%description libs -l pl
Bibloteki wspó³dzielone Anjuta.

%package devel
Summary:	Anjuta header files
Summary(pl):	Pliki nag³ówkowe Anjuta
Group:		Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description devel
Anjuta header files.

%description devel -l pl
Pliki nag³ówkowe Anjuta.

%package static
Summary:	Anjuta static library
Summary(pl):	Biblioteka statyczna Anjuta
Group:		Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Anjuta static library.

%description static -l pl
Biblioteka statyczna Anjuta.

%prep
%setup -q
%patch0 -p0
#%patch1 -p1
%patch2 -p1
%patch3 -p1

sed -i -e 's|^(packageplugindir=)lib/|$1%{_lib}/|' configure.in

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-plugin-subversion \
	--enable-final \
	--enable-gtk-doc \
	--enable-static \
	--with-html-dir=%{_gtkdocdir}	       
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/lib*.{a,la}
rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post   libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE MAINTAINERS NEWS README ROADMAP TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/libanjuta-*.so*
%{_datadir}/mime/packages/*.xml
%{_libdir}/%{name}/*.plugin
%{_iconsdir}/
%{_pixmapsdir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/*
%{_mandir}/man1/*
# no documentation for now
#%%{_omf_dest_dir}/%{name}

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/libanjuta-1.0
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_gtkdocdir}/libanjuta
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
