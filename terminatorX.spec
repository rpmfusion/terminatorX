Summary:       Real-time Audio Synthesizer
Name:          terminatorX
Version:       4.2.0
Release:       5%{?dist}
Group:         Applications/Multimedia
License:       GPLv2+ and GFDL
URL:           https://terminatorx.org/
Source0:       %url/dist/%{name}-%{version}.tar.gz

BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib
BuildRequires: gcc-c++
BuildRequires: gtk3-devel
BuildRequires: itstool
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: libcap-devel
BuildRequires: liblrdf-devel
BuildRequires: libmad-devel
BuildRequires: libvorbis-devel
BuildRequires: libxml2-devel
BuildRequires: libX11-devel
BuildRequires: mpg123
BuildRequires: pulseaudio-libs-devel
BuildRequires: sox
BuildRequires: vorbis-tools

Requires:      hicolor-icon-theme
Requires:      mpg123
Requires:      sox
Requires:      vorbis-tools

%description
terminatorX is a real-time audio synthesizer that allows you to "scratch" on
digitally sampled audio data (*.wav, *.au, *.ogg, *.mp3, etc.) the way
hiphop-DJs scratch on vinyl records. It features multiple turntables, real-time
effects (buit-in as well as LADSPA plug-in effects), a sequencer and MIDI
interface - all accessible through an easy-to-use gtk+ GUI.

%prep
%setup -q

# Fix Ladspa path
sed -i 's|/lib/|/%{_lib}/|g' src/tX_ladspa.cc

%build
%configure
%make_build

%install
%make_install

# desktop file categories
ADD="Audio X-Jack X-DJTools X-DigitalProcessing Sequencer"
REMOVE="Application"
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  `for c in ${ADD}    ; do echo "--add-category $c "    ; done` \
  `for c in ${REMOVE} ; do echo "--remove-category $c " ; done` \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/%{name}.appdata.xml

%files
%doc ChangeLog NEWS README*
%license COPYING*
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/mime-info/%{name}.keys
%{_datadir}/mime-info/%{name}.mime
%{_datadir}/help/C/%{name}-manual/
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/icons/hicolor/512x512/apps/%{name}.png
%{_datadir}/icons/hicolor/512x512/mimetypes/%{name}-mime.png
%{_datadir}/applications/%{name}.desktop
%{_datadir}/appdata/%{name}.appdata.xml

%changelog
* Tue Jan 28 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Aug 02 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Aug 02 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Oct 01 2022 Leigh Scott <leigh123linux@gmail.com> - 4.2.0-1
- Update to 4.2.0

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 4.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sat Oct 30 2021 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 4.1.0-1
- Version updae

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Leigh Scott <leigh123linux@googlemail.com> - 4.0.1-6
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 4.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 4.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 4.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 26 2016 Adrian Reber <adrian@lisas.de> - 4.0.1-1
- Update to 4.0.1
- Added pulseaudio-devel BR
- Removed unneeded BRs

* Tue Jul 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 4.0.0-1
- Update to 4.0.0
- Change from gtk2 to gtk3

* Sat Dec 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 3.90-3
- Switch to mpg123

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 3.90-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Thu Feb 13 2014 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 3.90-1
- Update to 3.90

* Sun Dec 08 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.84-5
- Rebuilt

* Sun Mar 24 2013 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 3.84-4
- Build fix against newer zlib
- Spec file cleanup

* Sun Mar 03 2013 Nicolas Chauvet <kwizart@gmail.com> - 3.84-3
- Mass rebuilt for Fedora 19 Features

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 3.84-2
- Rebuilt for c++ ABI breakage

* Sat Nov 26 2011 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 3.84-1
- Update to 3.84

* Tue Mar 01 2011 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 3.83-1
- Update to 3.83

* Fri Oct 23 2009 Orcan Ogetbil <oged[DOT]fedora[AT]gmail[DOT]com> - 3.82-4
- Update desktop file according to F-12 FedoraStudio feature

* Sat Apr 04 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 3.82-3
- Fix ppc/ppc64 build failure

* Wed Apr 01 2009 Orcan Ogetbil <oget[dot]fedora[at]gmail[dot]com> - 3.82-2
- Prepared package for RPMFusion submission (originates from planetccrma)

* Tue Dec 11 2007 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Wed Feb 16 2005 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- declare do_save_tables before using it (for <= fc1)

* Fri Dec 31 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.82-1
- updated to 3.82
- update doc file list

* Mon Dec 27 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- spec file cleanup

* Thu May 20 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added build dependencies

* Sun Feb 29 2004 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.81-2
- rebuild for liblrdf 0.3.5

* Mon Oct 20 2003 Patrice Tisserand <Patrice.Tisserand@ircam.fr> 3.81-1
- updated for terminatorX-3.81
- fixed building as non root user
- still need to bez built with --define='_unpackaged_files_terminate_build 0',
  don't knwo what to do with scrollkeeper

* Wed May  7 2003 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu> 3.80-1
- updated to 3.80
- added proper desktop entry
- updated file list (what to do with scrollkeeper?)
- added clean target
- make it build under gcc 2.96

* Mon Dec  9 2002 Fernando Lopez-Lezcano <nando@ccrma.stanford.edu>
- added patch to compile under redhat 8.0 and gcc 3.2
- erased post warning about suid root executable

* Sat Sep 14 2002 Alexander Konig <alex@lisas.de>
 - Switch from xpm to pngs for GNOME icons

* Fri May 31 2002 Alexander Konig <alex@lisas.de>
 - Added Adrian's man page

* Tue Mar 20 2001 Adrian Reber <adrian@lisas.de>
 - Updated to 3.71

* Sat Dec 09 2000 Adrian Reber <adrian@lisas.de>
 - Updated to 3.70

* Wed Apr 12 2000 Adrian Reber <adrian@lisas.de>
 - Updated to 3.60

* Wed Feb 23 2000 Adrian Reber <adrian@42.fht-esslingen.de>
 - Mandrake adaptations.

* Mon Feb 14 2000 Adrian Reber <adrian@42.fht-esslingen.de>
 - Updated to 3.55

* Fri Dec 17 1999 Adrian Reber <adrian@42.fht-esslingen.de>
 - Updated to 3.5

* Thu Jul 29 1999 Adrian Reber <adrian@rhlx01.fht-esslingen.de>
 - Updated to 3.2

* Fri May 07 1999 Adrian Reber <adrian@rhlx01.fht-esslingen.de>
 - Initial release

