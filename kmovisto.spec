%define	name	kmovisto
%define	version	0.7.0
%define	release	%mkrel 6

Summary:	Molecule viewer and 3-D exporter
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		http://mitglied.lycos.de/PageOfMH
Group:		Sciences/Chemistry
Source0:	%{name}-%{version}.tar.bz2
Patch:		kmovisto-0.7.0-cpp.patch.bz2
BuildRequires:	qt3-devel
BuildRequires:  MesaGLU-devel

%description
KMovisto is a free molecule viewer. This program imports GAUSSIAN or XYZ files
and exports POVRay, VRML or XYZ files.

%prep
%setup -q
%patch -p1

%build
export QTDIR=%{_prefix}/lib/qt3
export QTLIB=$QTDIR/%{_lib}
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

# menu
install -d $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="kmovisto"\
needs="x11"\
section="More Applications/Sciences/Chemistry"\
title="KMovisto"\
icon="chemistry_section.png"\
longtitle="QT Molecule Viewer"
EOF

%post
%update_menus
		
%postun
%clean_menus

%clean
rm -fr %buildroot

%files
%defattr (-,root,root,0755)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/%{name}
%{_menudir}/%{name}

