%define	upstream_name    Params-ValidationCompiler

Name:		perl-%{upstream_name}
Version:	0.31
Release:	3

Summary:	Optimized subroutine parameter validator


License:	Artistic 2.0
Group:		Development/Perl
Url:		https://metacpan.org/pod/Params::ValidationCompiler
Source0:	http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate)

BuildArch:	noarch


%description
This module creates a customized, highly efficient parameter
checking subroutine.
It can handle named or positional parameters, and can return the
parameters as key/value pairs or a list of values.

In addition to type checks, it also supports parameter defaults,
optional parameters, and extra "slurpy" parameters.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make_build

%install
%make_install

%files
%doc Changes 
%{perl_vendorlib}/Params
%{_mandir}/*/*
