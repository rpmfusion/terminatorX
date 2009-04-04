Summary:       Realtime Audio Synthesizer
Name:          terminatorX
Version:       3.82
Release:       3%{?dist}
Group:         Applications/Multimedia
License:       GPLv2+ and GFDL
URL:           http://terminatorx.org/
Source0:       http://terminatorx.org/dist/%{name}-%{version}.tar.gz
Patch0:        %{name}-gcc44.patch
# To make the package buildable on ppc/ppc64:
Patch1:        %{name}-endian_h.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: alsa-lib-devel
BuildRequires: audiofile-devel
BuildRequires: desktop-file-utils
BuildRequires: gnome-libs-devel
BuildRequires: gtk2-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: ladspa-devel
BuildRequires: libcap-devel
BuildRequires: liblrdf-devel
BuildRequires: libmad-devel
BuildRequires: libvorbis-devel 
BuildRequires: libxml2-devel
BuildRequires: libXxf86dga-devel 
BuildRequires: mpg321
BuildRequires: scrollkeeper
BuildRequires: sox
BuildRequires: vorbis-tools 

Requires:      mpg321
Requires:      sox
Requires:      vorbis-tools

Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
terminatorX is a realtime audio synthesizer that allows you to "scratch" on
digitally sampled audio data (*.wav, *.au, *.ogg, *.mp3, etc.) the way 
hiphop-DJs scratch on vinyl records. It features multiple turntables, realtime
effects (buit-in as well as LADSPA plugin effects), a sequencer and an
easy-to-use gtk+ GUI.

%prep
%setup -q
%patch0 -p1 -b .gcc44
%patch1 -p1 -b .endian

# To match the freedesktop standards
sed -i 's|\.png||' gnome-support/%{name}.desktop

# Fix encoding
for file in AUTHORS ChangeLog README; do
   iconv -f iso8859-1 -t utf8 $file -o $file.tmp
   touch -r $file $file.tmp
   mv -f $file.tmp $file
done

%build
%configure
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# install mime files
mkdir -p %{buildroot}%{_datadir}/mime-info
install -pm 0644 gnome-support/terminatorX.keys %{buildroot}%{_datadir}/mime-info
install -pm 0644 gnome-support/terminatorX.mime %{buildroot}%{_datadir}/mime-info

# move icons to the proper freedesktop location
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
mv %{buildroot}%{_datadir}/pixmaps/terminatorX-app.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/
mv %{buildroot}%{_datadir}/pixmaps/terminatorX-mime.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/

# desktop file categories
ADD="Audio Midi X-Jack X-DJTools"
REMOVE="Application"
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  `for c in ${ADD}    ; do echo "--add-category $c "    ; done` \
  `for c in ${REMOVE} ; do echo "--remove-category $c " ; done` \
  gnome-support/%{name}.desktop

# we don't need to package these
rm -f %{buildroot}%{_datadir}/gnome/apps/Multimedia/%{name}.desktop
rm -rf %{buildroot}%{_var}/scrollkeeper

%clean
rm -rf %{buildroot}

%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null
scrollkeeper-update -q -o %{_datadir}/omf/%{name} || :

%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null
fi
scrollkeeper-update -q || :

%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING* NEWS README* THANKS TODO 
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/%{name}/
%{_datadir}/mime-info/%{name}.keys
%{_datadir}/mime-info/%{name}.mime
%{_datadir}/omf/*/*
%{_datadir}/icons/hicolor/48x48/apps/*png
%{_datadir}/applications/%{name}.desktop


%changelog
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

* Thu Feb 14 2000 Adrian Reber <adrian@42.fht-esslingen.de>
 - Updated to 3.55

* Thu Dec 17 1999 Adrian Reber <adrian@42.fht-esslingen.de>
 - Updated to 3.5

* Thu Jul 29 1999 Adrian Reber <adrian@rhlx01.fht-esslingen.de>
 - Updated to 3.2

* Fri May 07 1999 Adrian Reber <adrian@rhlx01.fht-esslingen.de>
 - Initial release

