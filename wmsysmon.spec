Summary:	Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Summary(pl):	Monitor systemu dla WindowMakera/AfterStepa
Name:		wmsysmon
Version:	0.7.6
Release:	4
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://www.gnugeneration.com/software/wmsysmon/src/%{name}-%{version}.tar.gz
# Source0-md5:	1f8b7872c20fa6af1c89265ea2126c31
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
URL:		http://www.gnugeneration.com/software/wmsysmon/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmsysmon monitors memory, swap, disk I/O, uptime, interrupts. Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%description -l pl
wmsysmon jest dokowalnym apletem dla WindowMakera i AfterStepa,
monitoruj±cym wykorzystanie zasobów systemowych.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DHI_INTS" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install src/wmsysmon $RPM_BUILD_ROOT%{_bindir}

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/wmsysmon
%{_desktopdir}/docklets/wmsysmon.desktop
