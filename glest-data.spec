Summary:	Game data for Glest
Name:		glest-data
Version:	3.2.1
Release:	%mkrel 3
License:	GPLv2+
Group:		Games/Strategy
URL:		http://www.glest.org/
Source0:	http://downloads.sourceforge.net/glest/glest_data_%{version}.zip
BuildRequires:	recode
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Glest is a 3d OpenGL real time strategy game. It takes place in a 
context which could be compared to that of the pre-renaissance 
Europe, with the licence that magic forces exist in the environment 
and can be controlled.

This package contains the architecture independent data files needed
for playing the game.

%prep
%setup -q -n glest_game

# fix endings
find docs -type f | xargs sed -i -e "s/\r//g"
# UTF-8
recode ISO-8859-1..UTF-8 docs/*.txt
mv data/lang/espa?ol.lng data/lang/espanol.lng

%build
# nothing to do here

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_gamesdatadir}/glest
cp -fr * %{buildroot}%{_gamesdatadir}/glest/
rm -fr  %{buildroot}%{_gamesdatadir}/glest/docs
rm -f %{buildroot}%{_gamesdatadir}/glest/glest.ini

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc docs/*
%{_gamesdatadir}/glest/
