#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-git2r
Version  : 0.26.1
Release  : 79
URL      : https://cran.r-project.org/src/contrib/git2r_0.26.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/git2r_0.26.1.tar.gz
Summary  : Provides Access to Git Repositories
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1 MIT
Requires: R-git2r-lib = %{version}-%{release}
BuildRequires : buildreq-R
BuildRequires : curl-dev
BuildRequires : git
BuildRequires : libgit2-dev
BuildRequires : libidn-dev
BuildRequires : libssh2-dev
BuildRequires : nghttp2-dev
BuildRequires : openssl-dev
BuildRequires : pkgconfig(libssh2)
BuildRequires : pkgconfig(openssl)
BuildRequires : pkgconfig(zlib)
BuildRequires : util-linux
BuildRequires : zlib-dev

%description
implementation of the 'Git' core methods. Provides access to 'Git'
    repositories to extract data and running some basic 'Git'
    commands.

%package lib
Summary: lib components for the R-git2r package.
Group: Libraries

%description lib
lib components for the R-git2r package.


%prep
%setup -q -c -n git2r

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571838423

%install
export SOURCE_DATE_EPOCH=1571838423
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library git2r
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc git2r || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/AUTHORS
/usr/lib64/R/library/git2r/CITATION
/usr/lib64/R/library/git2r/COPYING
/usr/lib64/R/library/git2r/COPYRIGHTS
/usr/lib64/R/library/git2r/DESCRIPTION
/usr/lib64/R/library/git2r/INDEX
/usr/lib64/R/library/git2r/Meta/Rd.rds
/usr/lib64/R/library/git2r/Meta/features.rds
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
/usr/lib64/R/library/git2r/tests/add-force.R
/usr/lib64/R/library/git2r/tests/bare_repository.R
/usr/lib64/R/library/git2r/tests/blame.R
/usr/lib64/R/library/git2r/tests/blob.R
/usr/lib64/R/library/git2r/tests/branch.R
/usr/lib64/R/library/git2r/tests/bundle.R
/usr/lib64/R/library/git2r/tests/checkout-named-branch.R
/usr/lib64/R/library/git2r/tests/checkout.R
/usr/lib64/R/library/git2r/tests/checkout_branch.R
/usr/lib64/R/library/git2r/tests/checkout_commit.R
/usr/lib64/R/library/git2r/tests/checkout_tag.R
/usr/lib64/R/library/git2r/tests/clone_bare.R
/usr/lib64/R/library/git2r/tests/clone_branch.R
/usr/lib64/R/library/git2r/tests/clone_checkout.R
/usr/lib64/R/library/git2r/tests/commit.R
/usr/lib64/R/library/git2r/tests/commits_path.R
/usr/lib64/R/library/git2r/tests/config.R
/usr/lib64/R/library/git2r/tests/diff.R
/usr/lib64/R/library/git2r/tests/fast_forward_merge.R
/usr/lib64/R/library/git2r/tests/fetch.R
/usr/lib64/R/library/git2r/tests/graph.R
/usr/lib64/R/library/git2r/tests/index.R
/usr/lib64/R/library/git2r/tests/invalid-conf-var.R
/usr/lib64/R/library/git2r/tests/libgit2.R
/usr/lib64/R/library/git2r/tests/merge.R
/usr/lib64/R/library/git2r/tests/merge_named_branch.R
/usr/lib64/R/library/git2r/tests/normal_merge.R
/usr/lib64/R/library/git2r/tests/note.R
/usr/lib64/R/library/git2r/tests/odb_blobs.R
/usr/lib64/R/library/git2r/tests/pre-process-path.R
/usr/lib64/R/library/git2r/tests/pull.R
/usr/lib64/R/library/git2r/tests/push-force.R
/usr/lib64/R/library/git2r/tests/push.R
/usr/lib64/R/library/git2r/tests/reference.R
/usr/lib64/R/library/git2r/tests/reflog.R
/usr/lib64/R/library/git2r/tests/refspec.R
/usr/lib64/R/library/git2r/tests/remotes.R
/usr/lib64/R/library/git2r/tests/remove.R
/usr/lib64/R/library/git2r/tests/repository.R
/usr/lib64/R/library/git2r/tests/reset.R
/usr/lib64/R/library/git2r/tests/revparse.R
/usr/lib64/R/library/git2r/tests/signature.R
/usr/lib64/R/library/git2r/tests/stash.R
/usr/lib64/R/library/git2r/tests/status.R
/usr/lib64/R/library/git2r/tests/tag.R
/usr/lib64/R/library/git2r/tests/time.R
/usr/lib64/R/library/git2r/tests/tree.R
/usr/lib64/R/library/git2r/tests/when.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/git2r/libs/git2r.so
/usr/lib64/R/library/git2r/libs/git2r.so.avx2
