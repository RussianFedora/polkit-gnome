Summary: PolicyKit integration for the GNOME desktop
Name: polkit-gnome
Version: 0.97
Release: 1%{?dist}
License: LGPLv2+
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: Applications/System
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2

BuildRequires: gtk2-devel >= 2.25.11
BuildRequires: polkit-devel >= 0.95-1
BuildRequires: desktop-file-utils
BuildRequires: intltool
BuildRequires: gobject-introspection-devel

Obsoletes: PolicyKit-gnome <= 0.10
Provides: PolicyKit-gnome = 0.11
Obsoletes: PolicyKit-gnome-libs <= 0.10
Provides: PolicyKit-gnome-libs = 0.11

Provides: PolicyKit-authentication-agent

Requires: polkit >= 0.95

# use icons that exist in current icon theme
Patch0: new-lock-icons.patch

%description
polkit-gnome provides an authentication agent for PolicyKit
that matches the look and feel of the GNOME desktop.

%package devel
Summary: Development files for polkit-gnome
Group: Development/Libraries
Requires: %name = %{version}-%{release}
Requires: %name-docs = %{version}-%{release}
Requires: pkgconfig
Requires: polkit-devel
Obsoletes: PolicyKit-gnome-devel <= 0.10
Provides: PolicyKit-gnome-devel = 0.11
Obsoletes: PolicyKit-gnome-demo <= 0.10
Provides: PolicyKit-gnome-demo = 0.11

%description devel
Development files for polkit-gnome.

%package docs
Summary: Development documentation for polkit-gnome
Group: Development/Libraries
Requires: %name-devel = %{version}-%{release}
Requires: gtk-doc

%description docs
Development documentation for polkit-gnome.

%prep
%setup -q
%patch0 -p1 -b .new-lock-icons

%build
%configure --enable-gtk-doc --disable-introspection
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

desktop-file-install --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart                      \
  --remove-only-show-in GNOME \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

echo 'NotShowIn=KDE;' >>$RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop
desktop-file-validate $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

%find_lang polkit-gnome-1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f polkit-gnome-1.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_sysconfdir}/xdg/autostart/*
%{_libexecdir}/*
%{_libdir}/lib*.so.*
# %{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*
# %{_datadir}/gir-1.0/*.gir

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*


%changelog
* Mon Aug 09 2010 David Zeuthen <davidz@redhat.com> - 0.97-1
- Update to 0.97

* Mon Jun 14 2010 Matthias Clasen <mclasen@redhat.com> - 0.96-2
- Use lock icons that exist in current icon theme
- Minor spec file fixes

* Fri Jan 15 2010 David Zeuthen <davidz@redhat.com> - 0.96-1
- Update to release 0.96
- Disable introspection support for the time being

* Tue Jan  5 2010 Kevin Kofler <Kevin@tigcc.ticalc.org> - 0.95-2
- Don't autostart in KDE on F13+

* Fri Nov 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-1
- Update to release 0.95
- Drop upstreamed patches

* Wed Oct  7 2009 Matthias Clasen <mclasen@redhat.com> - 0.95.0.git20090913.6
- Prevent the statusicon from eating whitespace

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.5
- add Provides: PolicyKit-authentication-agent to satify what PolicyKit-gnome
  also provided

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.4
- Refine how Obsolete: is used and also add Provides: (thanks Jesse
  Keating and nim-nim)

* Mon Sep 14 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.3
- Obsolete old PolicyKit-gnome packages

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.2
- Update BR

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913.1
- Update BR

* Sun Sep 13 2009 David Zeuthen <davidz@redhat.com> - 0.95-0.git20090913
- Update to git snapshot
- Turn on GObject introspection

* Wed Sep  2 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-4
- Just remove the OnlyShowIn, it turns out everybody wants this

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-3
- Require a new enough polkit (#517479)

* Sat Aug 29 2009 Matthias Clasen <mclasen@redhat.com> - 0.94-2
- Show in KDE, too (#519674)

* Wed Aug 12 2009 David Zeuthen <davidz@redhat.com> - 0.94-1
- Update to upstream release 0.94

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.93-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 David Zeuthen <davidz@redhat.com> - 0.93-2
- Rebuild

* Mon Jul 20 2009 David Zeuthen <davidz@redhat.com> - 0.93-1
- Update to 0.93

* Tue Jun  9 2009 Matthias Clasen <mclasen@redhat.com> - 0.9.2-3
- Fix BuildRequires

* Tue Jun 09 2009 David Zeuthen <davidz@redhat.com> - 0.92-2
- Change license to LGPLv2+
- Remove Requires: gnome-session

* Mon Jun 08 2009 David Zeuthen <davidz@redhat.com> - 0.92-1
- Update to 0.92 release

* Wed May 27 2009 David Zeuthen <davidz@redhat.com> - 0.92-0.git20090527
- Update to 0.92 snapshot

* Mon Feb  9 2009 David Zeuthen <davidz@redhat.com> - 0.91-1
- Initial spec file.
