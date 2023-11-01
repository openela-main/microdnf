%global libdnf_version 0.62.0

Name:           microdnf
Version:        3.8.0
Release:        2%{?dist}
Summary:        Lightweight implementation of DNF in C

License:        GPLv2+
URL:            https://github.com/rpm-software-management/microdnf
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Revert-Dont-set-default-value-of-assumeyes-to-TRUE.patch

BuildRequires:  gcc
BuildRequires:  meson >= 0.36.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gobject-2.0) >= 2.44.0
BuildRequires:  pkgconfig(libpeas-1.0) >= 1.20.0
BuildRequires:  pkgconfig(libdnf) >= %{libdnf_version}
BuildRequires:  pkgconfig(smartcols)
BuildRequires:  help2man

Requires:       libdnf%{?_isa} >= %{libdnf_version}
%if 0%{?rhel} > 8 || 0%{?fedora}
# Ensure DNF package manager configuration skeleton is installed
Requires:       dnf-data
%endif

%description
Micro DNF is a lightweight C implementation of DNF, designed to be used
for doing simple packaging actions when you don't need full-blown DNF and
you want the tiniest useful environments possible.

That is, you don't want any interpreter stack and you want the most
minimal environment possible so you can build up to exactly what you need.


%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README.md
%{_mandir}/man8/microdnf.8*
%{_bindir}/%{name}

%changelog
* Thu May 20 2021 Pavla Kratochvilova <pkratoch@redhat.com> - 3.8.0-2
- Revert: Don't set default value of "assumeyes" to TRUE

* Wed May 19 2021 Pavla Kratochvilova <pkratoch@redhat.com> - 3.8.0-1
- Update to 3.8.0
- Don't set default value of "assumeyes" to TRUE
- Support for user confirmation and assumeyes, assumeno, defaultyes
- Add commands: distro-sync, makecache
- Add subcommands support
- Add support for command aliases
- Added alias "update" to "upgrade" command
- Relicense to GPLv2+
- Add support for setting allow_vendor_change
- [download] Support for "--resolve", "--alldeps" and "--archlist=" arguments
- [download] several optimizations
- Support "--setopt=keepcache=0/1"
- Extend "--setopt" to support repository options

* Mon Feb 08 2021 Nicola Sella <nsella@redhat.com> - 3.4.0-4
- Print info about obsoleted packages before transaction (RhBug:1855542)

* Fri Jan 29 2021 Nicola Sella <nsella@redhat.com> - 3.4.0-3
- Patch: Add support for setting a platform module ID
- Rename "update" command to "upgrade", "update" remain as compatibility alias

* Fri Jan 15 2021 Nicola Sella <nsella@redhat.com> - 3.4.0-2
- Patch: Add module enable/disable/reset command

* Mon Apr 06 2020 Ales Matej <amatej@redhat.com> - 3.4.0-1
- Update to 3.4.0
- Fix: do not download metadata in remove command
- Add reinstall command
- Add "--setopt=tsflags=test" support
- Add "--setopt=reposdir=<path>" and "--setopt=varsdir=<path1>,<path2>,..." support
- Add "--config=<path_to_config_file>" support
- Add "--disableplugin", "--enableplugin" support (RhBug:1781126)
- Add "--noplugins" support
- Add "--setopt=cachedir=<path_to_cache_directory>" support
- Add "--installroot=<path_to_installroot_directory>" support
- Add "--refresh" support
- Support "install_weak_deps" conf option and "--setopt=install_weak_deps=0/1"
- Respect reposdir from conf file
- Respect "metadata_expire" conf file opton (RhBug:1771147)
- [repolist] Print padding spaces only if output is terminal

* Mon Jan 13 2020 Ales Matej <amatej@redhat.com> - 3.0.1-8
- Fix: Don't print lines with (null) in transaction report (RhBug:1691353)

* Tue Dec 17 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 3.0.1-7
- Add dependency on libdnf

* Tue Dec 17 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 3.0.1-6
- Allow downgrade for all transactions microdnf does (RhBug:1725863)

* Tue Nov 26 2019 Ales Matej <amatej@redhat.com> - 3.0.1-5
- Add repolist command (RhBug:1584952)
- Add repoquery command (RhBug:1769245)

* Wed Nov 13 2019 Ales Matej <amatej@redhat.com> - 3.0.1-4
- Add support of best behavior (RhBug:1679476)
- Add support for --releasever (RhBug:1591627)

* Fri Aug 30 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 3.0.1-3
- Fix microdnf --help coredump (RhBug:1744979)

* Thu Aug 01 2019 Pavla Kratochvilova <pkratoch@redhat.com> - 3.0.1-2
- Fix minor memory leaks (RhBug:1702283)
- Use help2man to generate a man page (RhBug:1612520)

* Wed Jun 27 2018 Jaroslav Mracek <jmracek@redhat.com> - 3.0.1-1
- Update to 3.0.1

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 3-2
- No CMake, only meson

* Thu Jun 01 2017 Igor Gnatenko <ignatenko@redhat.com> - 3-1
- Update to 3

* Fri May 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 2-3
- Apply few patches from upstream

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 02 2017 Igor Gnatenko <ignatenko@redhat.com> - 2-1
- Update to 2

* Mon Dec 12 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1-1
- Initial package
