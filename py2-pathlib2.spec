### RPM external py2-pathlib2 2.3.2
## INITENV +PATH PYTHON27PATH %{i}/${PYTHON_LIB_SITE_PACKAGES}
## INITENV +PATH PYTHON3PATH %{i}/${PYTHON3_LIB_SITE_PACKAGES}


%define pip_name pathlib2
Requires: py2-six py2-scandir 

## IMPORT build-with-pip

