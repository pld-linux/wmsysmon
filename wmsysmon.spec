%define name wmsysmon
%define version 0.2
%define release 1

%define builddir $RPM_BUILD_DIR/%{name}.app/%{name}

Name: %{name}
Summary: Window Maker/AfterStep memory/swap/IO/uptime/ints monitor
Version: %{version}
Release: %{release}
Group: X11/Utilities
Copyright: GPL
Vendor: Dave Clark <clarkd@skynet.ca>
Source0: %{name}-%{version}.tar.gz
Source1: %{name}.wmconfig
URL: http://www.neotokyo.org/illusion/
Icon: %{name}.gif
Patch: %{name}.app-make.patch

%description
%{name} monitors memory, swap, disk I/O, uptime, interrupts.  Window
Maker and AfterStep dockable, but should run (I think) without them
(e.g., swallowable by fvwm).

%changelog
* Thu Dec 31 1998 Yeechang Lee <ylee@columbia.edu>
- Fixed a stupid mistake in wmsysmon.wmconfig
* Tue Dec 29 1998 Yeechang Lee <ylee@columbia.edu>
- Patched Makefile so binary goes in /usr/X11R6/bin rather than /usr/local/bin

%prep
%setup -n %{builddir}
cd $RPM_BUILD_DIR
%patch

%build
make

%install
mkdir -p /etc/X11/wmconfig
cp -pf $RPM_SOURCE_DIR/wmsysmon.wmconfig /etc/X11/wmconfig/%{name}
strip %{name}
make install

%files
%doc ../BUGS ../CHANGES ../COPYING ../README
%attr(644,root,root) %config(missingok) /etc/X11/wmconfig/%{name}
%attr(755,root,root) /usr/X11R6/bin/%{name}

%clean
rm -rf $RPM_BUILD_DIR/%{name}.app
