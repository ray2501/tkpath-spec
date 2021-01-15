%{!?directory:%define directory /usr}

%define buildroot %{_tmppath}/%{name}

Name:          tkpath
Summary:       SVG-like rendering for the canvas
Version:       0.3.3
Release:       1
License:       BSD-3-Clause
Group:         Development/Libraries/Tcl
Source:        %{name}-%{version}.tar.gz
URL:           https://bitbucket.org/andrew_shadura/tkpath
BuildRequires: autoconf
BuildRequires: tcl-devel >= 8.5
BuildRequires: tk-devel >= 8.5
BuildRequires: cairo-devel >= 1.0
Requires:      tcl >= 8.5
Requires:      tk >= 8.5
BuildRoot:     %{buildroot}

%description
Tkpath implements path drawing modeled after SVG.
It is very flexible and reproduces all standard drawing canvas items.
Features include: opacity, antialiasing, gradient fills,
affine transformations, and fill rules.

Backends include: CoreGraphics on MacOSX, GDI on Win32, GDI+ on WinXP,
Cairo on X11, and Tk drawing as a fallback.

Not all backends support all features.

%prep
%setup -q -n %{name}-%{version}

%build
./configure \
	--prefix=%{directory} \
	--exec-prefix=%{directory} \
	--libdir=%{directory}/%{_lib} \
%ifarch x86_64
	--enable-64bit=yes \
%endif
	--with-tcl=%{directory}/%{_lib} \
	--with-tk=%{directory}/%{_lib}
make 

%install
make DESTDIR=%{buildroot} pkglibdir=%{tcl_archdir}/%{name}%{version} install

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%{tcl_archdir}
