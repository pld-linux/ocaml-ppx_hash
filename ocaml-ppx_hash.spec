#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	A ppx rewriter that generates hash functions from type expressions and definitions
Summary(pl.UTF-8):	Moduł przepisujący ppx generujący funkcje haszujące z wyrażeń i definicji typów
Name:		ocaml-ppx_hash
Version:	0.14.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/janestreet/ppx_hash/tags
Source0:	https://github.com/janestreet/ppx_hash/archive/v%{version}/ppx_hash-%{version}.tar.gz
# Source0-md5:	e7a369576b35065102f3505246315c58
URL:		https://github.com/janestreet/ppx_hash
BuildRequires:	ocaml >= 1:4.04.2
BuildRequires:	ocaml-base-devel >= 0.14
BuildRequires:	ocaml-base-devel < 0.15
BuildRequires:	ocaml-dune >= 2.0.0
BuildRequires:	ocaml-ppx_compare-devel >= 0.14
BuildRequires:	ocaml-ppx_compare-devel < 0.15
BuildRequires:	ocaml-ppx_sexp_conv-devel >= 0.14
BuildRequires:	ocaml-ppx_sexp_conv-devel < 0.15
BuildRequires:	ocaml-ppxlib-devel >= 0.11.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
A ppx writer that generates hash functions from type expressions and
definitions.

This package contains files needed to run bytecode executables using
ppx_hash library.

%description -l pl.UTF-8
Moduł przepisujący generujący funkcje haszujące z wyrażeń i definicji
typów.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki ppx_hash.

%package devel
Summary:	A ppx rewriter that generates hash functions from type expressions and definitions - development part
Summary(pl.UTF-8):	Moduł przepisujący ppx generujący funkcje haszujące z wyrażeń i definicji typów - cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml
Requires:	ocaml-base-devel >= 0.14
Requires:	ocaml-ppx_compare-devel >= 0.14
Requires:	ocaml-ppx_sexp_conv-devel >= 0.14
Requires:	ocaml-ppxlib-devel >= 0.11.0

%description devel
This package contains files needed to develop OCaml programs using
ppx_hash library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów w OCamlu
używających biblioteki ppx_hash.

%prep
%setup -q -n ppx_hash-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_hash/*.ml
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/ppx_hash/*/*.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/ppx_hash

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md doc/design.notes
%dir %{_libdir}/ocaml/ppx_hash
%{_libdir}/ocaml/ppx_hash/META
%{_libdir}/ocaml/ppx_hash/*.cma
%dir %{_libdir}/ocaml/ppx_hash/expander
%{_libdir}/ocaml/ppx_hash/expander/*.cma
%dir %{_libdir}/ocaml/ppx_hash/runtime-lib
%{_libdir}/ocaml/ppx_hash/runtime-lib/*.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/ppx_hash/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_hash/expander/*.cmxs
%attr(755,root,root) %{_libdir}/ocaml/ppx_hash/runtime-lib/*.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/ppx_hash/*.cmi
%{_libdir}/ocaml/ppx_hash/*.cmt
%{_libdir}/ocaml/ppx_hash/*.cmti
%{_libdir}/ocaml/ppx_hash/*.mli
%{_libdir}/ocaml/ppx_hash/expander/*.cmi
%{_libdir}/ocaml/ppx_hash/expander/*.cmt
%{_libdir}/ocaml/ppx_hash/expander/*.cmti
%{_libdir}/ocaml/ppx_hash/expander/*.mli
%{_libdir}/ocaml/ppx_hash/runtime-lib/*.cmi
%{_libdir}/ocaml/ppx_hash/runtime-lib/*.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/ppx_hash/ppx_hash.a
%{_libdir}/ocaml/ppx_hash/*.cmx
%{_libdir}/ocaml/ppx_hash/*.cmxa
%{_libdir}/ocaml/ppx_hash/expander/ppx_hash_expander.a
%{_libdir}/ocaml/ppx_hash/expander/*.cmx
%{_libdir}/ocaml/ppx_hash/expander/*.cmxa
%{_libdir}/ocaml/ppx_hash/runtime-lib/ppx_hash_lib.a
%{_libdir}/ocaml/ppx_hash/runtime-lib/*.cmx
%{_libdir}/ocaml/ppx_hash/runtime-lib/*.cmxa
%endif
%{_libdir}/ocaml/ppx_hash/dune-package
%{_libdir}/ocaml/ppx_hash/opam
