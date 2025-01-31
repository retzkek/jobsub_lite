Name:		jobsub_lite
Version:	beta6
Release:	1%{?dist}
Summary:	Job submission wrapper scripts

Group:		Fermi SCS Group
License:	Apache
URL:		https://github.com/marcmengel/jobsub_lite
Source0:	https://github.com/marcmengel/jobsub_lite/archive/refs/tags/%{version}.tar.gz

BuildRequires:	python3
Requires: python3
Requires: cigetcert
Requires: htgettoken
Requires: python36-jinja2
Requires: condor
Requires: condor-classads
Requires: python3-condor
Requires: condor-credmon

%description
Job submission wrapper scripts


%prep
%setup

%build
/bin/true

%pre

for f in condor_q condor_transfer_data condor_release condor_wait condor_rm condor_submit condor_submit_dag 
do
    mv /usr/bin/$f /usr/bin/$f.real
done

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python3.6/site-packages/jobsub_lite/lib/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/python3.6/site-packages/jobsub_lite/templates/
mkdir -p $RPM_BUILD_ROOT/etc/condor/config.d
install -m 755 bin/* $RPM_BUILD_ROOT%{_bindir}
install -m 755 lib/* $RPM_BUILD_ROOT%{_libdir}/python3.6/site-packages/jobsub_lite/lib/
for d in templates/*
do
    mkdir $RPM_BUILD_ROOT%{_libdir}/python3.6/site-packages/jobsub_lite/$d
    install -m 644 $d/* $RPM_BUILD_ROOT%{_libdir}/python3.6/site-packages/jobsub_lite/$d/
done
install -m 644 config.d/50-jobsub_lite.configs $RPM_BUILD_ROOT/etc/condor/config.d

%postun

for f in condor_q condor_transfer_data condor_release condor_wait condor_rm condor_submit condor_submit_dag 
do
    mv /usr/bin/$f.real /usr/bin/$f
done

%files
%doc
%{_bindir}//condor_q
%{_bindir}/condor_release
%{_bindir}/condor_rm
%{_bindir}/condor_submit
%{_bindir}/condor_submit_dag
%{_bindir}/condor_transfer_data
%{_bindir}/condor_wait
%{_bindir}/decode_token.sh
%{_bindir}/fake_ifdh
%{_bindir}/jobsub_cmd
%{_bindir}/jobsub_hold
%{_bindir}/jobsub_q
%{_bindir}/jobsub_release
%{_bindir}/jobsub_rm
%{_bindir}/jobsub_submit
%{_bindir}/jobsub_transfer_data
%{_bindir}/jobsub_wait
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/condor.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/creds.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/dagnabbit.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/get_parser.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/packages.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/poms_wrap.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/tarfiles.py
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/utils.py
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dag/dag.dag.condor.sub
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dag/dagman_wrapper.sh
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dag/dagmax.config
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dagbegin.cmd
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dagend.cmd
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dagman_wrapper.sh
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dagmax.config
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dataset.dag
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/dataset.dag.condor.sub
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/sambegin.sh
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/dataset_dag/samend.sh
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/maxconcurrent_dag/dagmax.config
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/maxconcurrent_dag/maxconcurrent.dag
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/simple/simple.cmd
%{_libdir}/python3.6/site-packages/jobsub_lite/templates/simple/simple.sh
/etc/condor/config.d/50-jobsub_lite.configs 
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/condor.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/creds.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/dagnabbit.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/get_parser.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/packages.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/poms_wrap.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/tarfiles.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/utils.cpython-36.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/condor.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/creds.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/dagnabbit.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/get_parser.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/packages.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/poms_wrap.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/tarfiles.cpython-36.opt-1.pyc
%{_libdir}/python3.6/site-packages/jobsub_lite/lib/__pycache__/utils.cpython-36.opt-1.pyc
%clean
rm -rf $RPM_BUILD_ROOT

%changelog

