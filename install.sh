#!/bin/bash
#Linux 3.13.0-24-generic x86_64
#GNU bash, version 4.3.11(1)-release (x86_64-pc-linux-gnu)
#GNU Make 3.81
#Python 2.7.6

######################################################################
# variable defaults

#source install config if it exists but is not a requirement
if [ -f "install.config" ];then
source install.config
fi

#Output file where make output is written
MAKEOUT="${MAKEOUT:-make.out}"

#set MAKE if the MAKE variable is null
MAKE="${MAKE:-make}"

#set PYTHON if PYTHON variable is null
#search for a python 2.x version else set PYTHON=python
if [ -z "${PYTHON}" ]; then
  if which python2.7 &> /dev/null;then
    PYTHON="python2.7"
  elif which python2.6 &> /dev/null;then
    PYTHON="python2.6"
  elif which python2.5 &> /dev/null;then
    PYTHON="python2.5"
  elif which python2.4 &> /dev/null;then
    PYTHON="python2.4"
  elif which python2.3 &> /dev/null;then
    PYTHON="python2.3"
  elif which python2.2 &> /dev/null;then
    PYTHON="python2.2"
  else
    PYTHON="python"
  fi
fi

#variable clean up
#remove trailing slash from HTDOCS_DIR if it exists
HTDOCS_DIR="${HTDOCS_DIR%/}"

######################################################################
# functions

#This function checks for errors before allowing to continue
function preflight(){
  STATUS=0
  if [ -z "${HTDOCS_DIR}" ]; then
    echo "HTDOCS_DIR must be specified in install.config."
    echo "See install.config.sample for an example."
    echo ""
    STATUS=1
  fi
  #Test if python exists and is executable
  if [ ! -x "$(which "${PYTHON}")" ];then
    echo "${PYTHON} does not exist on this system or it is not executable!"
    echo ""
    STATUS=1
  fi
  if [ ! -x "$(which "${MAKE}")" ];then
    echo "${MAKE} does not exist on this system or it is not executable!"
    echo ""
    STATUS=1
  fi
  return ${STATUS}
}

#main function is where all the magic happens.  Building the site
function main(){
  STATUS=0
  ${MAKE} PYTHON="${PYTHON}" DocumentRoot="${HTDOCS_DIR}" clean all programmatic install 2>&1 | tee "${MAKEOUT}"
  #capture the exit status of the make command
  if [ ! "${PIPESTATUS[0]}" -eq "0" ];then
    STATUS=1
  fi
  echo done >> "${MAKEOUT}"
  return ${STATUS}
}

######################################################################
# main execution

#main depends on successful execution of preflight
#output to stderr like a good posix compatible program
#return a bad status code when the build process fails
preflight 1>&2 && main 1>&2
