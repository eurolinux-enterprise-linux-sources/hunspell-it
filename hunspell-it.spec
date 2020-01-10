Name: hunspell-it
Summary: Italian hunspell dictionaries
%define upstreamid 20070901
Version: 2.4
Release: 0.10.%{upstreamid}%{?dist}
Source: http://downloads.sourceforge.net/sourceforge/linguistico/italiano_2_4_2007_09_01.zip
Group: Applications/Text
URL: http://linguistico.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
License: GPLv3+
BuildArch: noarch
Requires: hunspell
#dic contains free-form text inside the .dic, i.e. "error: line 3: bad flagvector"
#  https://sourceforge.net/tracker/?func=detail&aid=2994177&group_id=128318&atid=711333
Patch0: hunspell-it-sf2994177.cleandic.patch

%description
Italian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-it
%patch0 -p0 -b .cleandic

%build
chmod -x *

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p *.dic *.aff $RPM_BUILD_ROOT/%{_datadir}/myspell
pushd $RPM_BUILD_ROOT/%{_datadir}/myspell/
it_IT_aliases="it_CH"
for lang in $it_IT_aliases; do
        ln -s it_IT.aff $lang.aff
        ln -s it_IT.dic $lang.dic
done


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc it_IT_README.txt it_IT_COPYING it_IT_AUTHORS it_IT_license.txt it_IT_notes.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.4-0.10.20070901
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.9.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.8.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.7.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.6.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Apr 29 2010 Caolan McNamara <caolanm@redhat.com> - 2.4-0.5.20070901
- remove spurious text from .dic

* Tue Jan 05 2010 Caolan McNamara <caolanm@redhat.com> - 2.4-0.4.20070901
- it_IT_README.1st says GPLv2+, but it_IT_README.txt says GPLv3+ -> 
  change license field to GPLv3+

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.3.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-0.2.20070901
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Sep 03 2007 Caolan McNamara <caolanm@redhat.com> - 2.4-0.1.20070901
- latest version

* Fri Aug 03 2007 Caolan McNamara <caolanm@redhat.com> - 2.3-0.2.20060723
- clarify license version

* Thu Dec 07 2006 Caolan McNamara <caolanm@redhat.com> - 2.3-0.1.20060723
- initial version
