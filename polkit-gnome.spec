Summary: PolicyKit integration for the GNOME desktop
Name: polkit-gnome
Version: 0.92
Release: 1%{?dist}
License: LGPLv2
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: Applications/System
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: polkit-devel >= 0.92
BuildRequires: desktop-file-utils

# for /usr/share/gnome/autostart
Requires: gnome-session

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%prep
%setup -q

%build
%configure --enable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-install --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_datadir}/gnome/autostart                      \
  $RPM_BUILD_ROOT%{_datadir}/gnome/autostart/polkit-gnome-authentication-agent-1.desktop

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_datadir}/gnome/autostart/*
%{_libexecdir}/*

%changelog
* Mon Jun 08 2009 David Zeuthen <davidz@redhat.com> - 0.92-1
- Update to 0.92 release

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.92-0.git20090527
- Update to 0.92 snapshot

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.91-1
- Initial spec file.
