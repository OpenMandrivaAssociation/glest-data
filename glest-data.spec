%define	name	glest-data
%define	version	2.0.1
%define	ver	%{version}
%define	release	%mkrel 2
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
cp -fr * $RPM_BUILD_ROOT%{_gamesdatadir}/glest/
rm -fr  $RPM_BUILD_ROOT%{_gamesdatadir}/glest/docs

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/*
%{_gamesdatadir}/glest/

