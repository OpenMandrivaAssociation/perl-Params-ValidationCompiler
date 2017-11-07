%define	upstream_name    Params-ValidationCompiler
%define upstream_version 0.24

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Optimized subroutine parameter validator


License:	Artistic 2.0
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Params/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl-devel
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Params::Validate) >= 0.72

BuildArch:	noarch


%description
This module creates a customized, highly efficient parameter
checking subroutine.
It can handle named or positional parameters, and can return the
parameters as key/value pairs or a list of values.

In addition to type checks, it also supports parameter defaults,
optional parameters, and extra "slurpy" parameters.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL installdirs=vendor destdir=%{buildroot}
%make

%install
%makeinstall_std

%files
%doc Changes 
%{perl_vendorlib}/Params
%{_mandir}/*/*
