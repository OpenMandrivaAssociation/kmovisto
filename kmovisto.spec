%define	name	kmovisto
%define	version	0.7.0
%define	release	%mkrel 9

Summary:	Molecule viewer and 3-D exporter
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
URL:		https://mitglied.lycos.de/PageOfMH
Group:		Sciences/Chemistry
Source0:	%{name}-%{version}.tar.bz2
Patch:		kmovisto-0.7.0-cpp.patch.bz2
BuildRequires:	qt3-devel
BuildRequires:  MesaGLU-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=kmovisto
Categories=Science;Chemistry;
Name=KMovisto
Icon=chemistry_section
Comment=QT Molecule Viewer
EOF

%if %mdkversion < 200900
%post
%update_menus
%endif
		
%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -fr %buildroot

%files
%defattr (-,root,root,0755)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop

