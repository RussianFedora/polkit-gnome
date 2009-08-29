Summary: PolicyKit integration for the GNOME desktop
Name: polkit-gnome
Version: 0.94
Release: 2%{?dist}
License: LGPLv2+
URL: http://www.freedesktop.org/wiki/Software/PolicyKit
Group: Applications/System
Source0: http://hal.freedesktop.org/releases/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: gtk2-devel
BuildRequires: polkit-devel >= 0.94
BuildRequires: desktop-file-utils
BuildRequires: intltool

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

%build
%configure --enable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

desktop-file-install --delete-original                   \
  --dir $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart                      \
  --add-only-show-in KDE \
  $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/polkit-gnome-authentication-agent-1.desktop

%find_lang polkit-gnome-1

%clean
rm -rf $RPM_BUILD_ROOT

%files -f polkit-gnome-1.lang
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_sysconfdir}/xdg/autostart/*
%{_libexecdir}/*
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%files docs
%defattr(-,root,root,-)
%{_datadir}/gtk-doc/html/*


%changelog
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
