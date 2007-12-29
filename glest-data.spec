%define	name	glest-data
%define	version	2.0.1
%define	ver	%{version}
%define	release	%mkrel 1
%define	Summary	Game data for Glest

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{Summary}
License:	GPL
Group:		Games/Strategy
URL:		http://www.glest.org/
Source0:	glest_data_%{version}.zip
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch

%description
Glest is a 3d OpenGL real time strategy game. It takes place in a 
context which could be compared to that of the pre-renaissance 
Europe, with the licence that magic forces exist in the environment 
and can be controlled.

This package contains the architecture independent data files needed
for playing the game.

%prep
%setup -q -n glest_game

%build
# nothing to do here

%install
rm -rf $RPM_BUILD_ROOT
  
install -m755 -d $RPM_BUILD_ROOT%{_gamesdatadir}/glest/data/
install -m755 -d $RPM_BUILD_ROOT%{_gamesdatadir}/glest/maps/
install -m755 -d $RPM_BUILD_ROOT%{_gamesdatadir}/glest/techs/
install -m755 -d $RPM_BUILD_ROOT%{_gamesdatadir}/glest/tilesets/
install -m644 configuration.xml $RPM_BUILD_ROOT%{_gamesdatadir}/glest/

cp -a data/* $RPM_BUILD_ROOT%{_gamesdatadir}/glest/data/
cp -a maps/* $RPM_BUILD_ROOT%{_gamesdatadir}/glest/maps/
cp -a techs/* $RPM_BUILD_ROOT%{_gamesdatadir}/glest/techs/
cp -a tilesets/* $RPM_BUILD_ROOT%{_gamesdatadir}/glest/tilesets/

#install -m666 glest.log $RPM_BUILD_ROOT%{_gamesdatadir}/glest/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/readme.txt docs/license.txt docs/tech/*
%{_gamesdatadir}/glest/

