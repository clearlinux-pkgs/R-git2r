#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-git2r
Version  : 0.15.0
Release  : 21
URL      : http://cran.r-project.org/src/contrib/git2r_0.15.0.tar.gz
Source0  : http://cran.r-project.org/src/contrib/git2r_0.15.0.tar.gz
Summary  : Provides Access to Git Repositories
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: R-git2r-lib
BuildRequires : clr-R-helpers
BuildRequires : curl-dev
BuildRequires : git
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libssl)
BuildRequires : zlib-dev

%description
No detailed description available

%package lib
Summary: lib components for the R-git2r package.
Group: Libraries

%description lib
lib components for the R-git2r package.


%prep
%setup -q -c -n git2r

%build

%install
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library git2r
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library git2r


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/AUTHORS
/usr/lib64/R/library/git2r/CITATION
/usr/lib64/R/library/git2r/COPYING
/usr/lib64/R/library/git2r/COPYRIGHTS
/usr/lib64/R/library/git2r/DESCRIPTION
/usr/lib64/R/library/git2r/INDEX
/usr/lib64/R/library/git2r/Meta/Rd.rds
/usr/lib64/R/library/git2r/Meta/hsearch.rds
/usr/lib64/R/library/git2r/Meta/links.rds
/usr/lib64/R/library/git2r/Meta/nsInfo.rds
/usr/lib64/R/library/git2r/Meta/package.rds
/usr/lib64/R/library/git2r/NAMESPACE
/usr/lib64/R/library/git2r/NEWS
/usr/lib64/R/library/git2r/R/git2r
/usr/lib64/R/library/git2r/R/git2r.rdb
/usr/lib64/R/library/git2r/R/git2r.rdx
/usr/lib64/R/library/git2r/help/AnIndex
/usr/lib64/R/library/git2r/help/aliases.rds
/usr/lib64/R/library/git2r/help/git2r.rdb
/usr/lib64/R/library/git2r/help/git2r.rdx
/usr/lib64/R/library/git2r/help/paths.rds
/usr/lib64/R/library/git2r/html/00Index.html
/usr/lib64/R/library/git2r/html/R.css
/usr/lib64/R/library/git2r/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/libs/git2r.so
