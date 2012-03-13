Name:		qtfm
Summary:	Lightweight file manager based on pure Qt
Version:	5.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Other
URL:		http://www.qtfm.org/
Source0:	http://www.qtfm.org/%{name}-%{version}.tar.gz
Patch0:		qtfm-5.4-mdv-desktop.patch
BuildRequires:	libqt4-devel
BuildRequires:	magic-devel

%description
qtFM is a small, lightweight file manager for Linux desktops based on pure Qt
and works great with minimal desktop environments like Openbox.

Features:

*  lightweight, pure Qt, no KDE libraries or other dependencies
*  full theme and mime file type icon integration
*  tree, bookmarks, list, icon, detail and thumbnail views
*  customizable interface, rearrange views and toolbars to suit
*  powerful custom command system for user defined actions
*  customizable key bindings for built-in and custom actions
*  drag & drop functionality
*  tabs

%prep
%setup -q
%patch0 -p1

%build
%qmake_qt4
%make

%install
make install INSTALL_ROOT=%{buildroot}

%if %{mdvver} >= 201200
%find_lang %{name} --with-qt
%define langfile %{name}.lang
%endif

%files %{?langfile:-f %{langfile}}
%{_bindir}/qtfm
%{_datadir}/applications/qtfm.desktop
%doc CHANGELOG COPYING README
%{_datadir}/pixmaps/qtfm.png
%if %{mdvver} <= 201100
%{_datadir}/qtfm/qtfm_*.qm
%endif
