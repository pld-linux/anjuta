Summary:	GNOME integrated development environment
Summary(es):	Entorno integrado de desarrollo (IDE) de GNOME
Summary(pl):	Zintegrowane ¶rodowisko programowania dla GNOME
Summary(pt_BR):	Ambiente de desenvolvimento integrado C e C++
Name:		anjuta
Version:	2.0.2
Release:	4
Epoch:		1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/anjuta/%{name}-%{version}.tar.gz
# Source0-md5:	e0d1e216da809df32816d233d7c55165
#Patch0: %{name}-home_etc.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-cflags.patch
URL:		http://anjuta.sourceforge.net/
BuildRequires:	ORBit2-devel >= 1:2.12.1
BuildRequires:	autoconf >= 2.52
BuildRequires:	autogen
BuildRequires:	automake
BuildRequires:	devhelp-devel
BuildRequires:	gdl-devel >= 0.6.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-build-devel
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	gnome-vfs2-devel >= 2.10.0-2
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libglade2-devel >= 1:2.5.1
BuildRequires:	libgnomeprintui-devel >= 2.10.2
BuildRequires:	libgnomeui-devel >= 2.10.0-2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libwnck-devel
BuildRequires:	libxml2-devel >= 1:2.6.19
BuildRequires:	ncurses-devel
BuildRequires:	neon-devel
BuildRequires:	pcre-devel >= 3.9
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRequires:	scrollkeeper
BuildRequires:	subversion-devel
BuildRequires:	vte-devel >= 0.11.0
Requires(post,postun):	scrollkeeper
# Requires:	gnome-terminal
Requires:	libanjuta = %{epoch}:%{version}-%{release}
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

%package -n libanjuta
Summary:	libanjuta library
Group:		Development/Libraries
Conflicts:	%{name} < 1:2.0.2-1

%description -n libanjuta
libanjuta library.

%package -n libanjuta-devel
Summary:	Header files and develpment documentation for libanjuta
Group:		Development/Libraries
Requires:	libanjuta-devel = %{epoch}:%{version}-%{release}

%description -n libanjuta-devel
Header files and develpment documentation for libanjuta.

%prep
%setup -q
#%patch0 -p1 NEEDS checking
%patch1 -p1
%patch2 -p0

%{__perl} -pi -e 's@^(packageplugindir=)lib/@$1%{_lib}/@' configure.in

%build
CXXFLAGS="%{rpmcflags} -fno-exceptions"
CFLAGS="%{rpmcflags} -fno-omit-frame-pointer"
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir} \
	--with-apr-config=%{_bindir}/apr-1-config \
	--with-apu-config=%{_bindir}/apu-1-config \
	--with-neon-config=%{_bindir}/neon-config \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	gnomemenudir=%{_desktopdir}

# *.la not needed - *.so loaded through libgmodule
rm -f $RPM_BUILD_ROOT%{_libdir}/anjuta/lib*.la

rm -r $RPM_BUILD_ROOT%{_datadir}/mime-info

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%scrollkeeper_update_post

%postun
%scrollkeeper_update_postun

%post	-n libanjuta -p /sbin/ldconfig
%postun -n libanjuta -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog FUTURE NEWS README TODO doc/ScintillaDoc.html
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/lib*.so*
%{_libdir}/%{name}/*.plugin
%{_pixmapsdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/application-registry/*.*
%{_datadir}/mime/packages/*.*
%{_desktopdir}/*.desktop
%{_mandir}/man1/*
%{_omf_dest_dir}/%{name}
%{_sysconfdir}/gconf/schemas/*.*
%{_iconsdir}/*/*/*/*.*

%files -n libanjuta
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*

%files -n libanjuta-devel
%defattr(644,root,root,755)
%{_includedir}/libanjuta-*
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_pkgconfigdir}/*.pc
%{_gtkdocdir}/libanjuta
