Name: 		wmsysmon
Summary: 	Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera/AfterStepa
Version: 	0.2
Release: 	3
Copyright: 	GPL
Group:          X11/Window Managers/Tools
Group(pl):      X11/Zarz±dcy Okien/Narzêdzia
Source0: 	http://www.neotokyo.org/illusion/%{name}-%{version}.tar.gz
Source1: 	wmsysmon.desktop
Icon: 		wmsysmon.gif
BuildPrereq:    XFree86-devel
BuildPrereq:    xpm-devel
BuildRoot:      /tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmsysmon monitors memory, swap, disk I/O, uptime, interrupts.  Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera i AfterStepa, 
monitoruj±cym wykorzystanie zasobów systemowych.

%prep
%setup -q -n %{name}.app

%build
make -C %{name} FLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/DockApplets}

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf BUGS CHANGES README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {BUGS,CHANGES,README}.gz
%attr(755,root,root) %{_bindir}/%{name}
/etc/X11/applnk/DockApplets/wmsysmon.desktop

%changelog
* Thu May 20 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [0.2-2]
- package is FHS 2.0 compliant,
- spec file modified for PLD use,
- based on spec written by Yeechang Lee <ylee@columbia.edu>.
