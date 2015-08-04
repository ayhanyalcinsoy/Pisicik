#!/bin/bash
#
# A script to maintain a Pardus local repo with only the latest packages
#
# History
# - v0.2, dfisek, 18/07/2009, don't get delta packages
# - v0.1, dfisek, 13/07/2007
#
# todo :
#  - implement download/use of pisi's cleanCache.py "if [ -f /etc/pardus-release ]"
#  - check if the previous mirroring was interrupted in repo up-to-date check
#

# Pardus local and official repo configuration
PARDUS_DIR="/home/PisiLinux/Masaüstü/Depo/PİSİLİNUX/PisiLinux-2.0/core"

TMPFILE1=`mktemp /tmp/parduslocalrepo.XXXXXX` || exit 1
TMPFILE2=`mktemp /tmp/parduslocalrepo.XXXXXX` || exit 1
TMPFILE3=`mktemp /tmp/parduslocalrepo.XXXXXX` || exit 1

cd $PARDUS_DIR


# Check if the repo is up-to-date
WGET_LOG=$(2>&1 LC_ALL=C wget -N http://ciftlik.pisilinux.org/pisi-2.0/pisi-index.xml.xz)
if echo "$WGET_LOG" | fgrep 'saved' &> /dev/null
then
    # Update repo index
    rm -f pisi-index.xml pisi-index.xml.xz.sha1sum pisi-index.xml.sha1sum
    wget http://ciftlik.pisilinux.org/pisi-2.0//pisi-index.xml.xz.sha1sum
    nice --adjustment=19 xz -dk pisi-index.xml.xz
    wget http://ciftlik.pisilinux.org/pisi-2.0//pisi-index.xml.sha1sum

    # Extract latest package list
    grep PackageURI pisi-index.xml > $TMPFILE1
    grep -v delta $TMPFILE1 > $TMPFILE2
    sed -e "s/^ *<PackageURI>/http:\/\/ciftlik.pisilinux.org\/pisi-2.0\//g" -e "s/<\/PackageURI>//g" $TMPFILE2 > $TMPFILE3

    # Implement cleanCache.py's function
    sed -e "s/^ *<PackageURI>/mv\ /g" -e "s/<\/PackageURI>/\ temp/g" $TMPFILE2 > mv.sh
    mkdir temp
    sh ./mv.sh >/dev/null 2>&1 </dev/null
    rm -f *.pisi mv.sh
    mv temp/* ./
    rmdir temp

    # Download the files
    if ! wget -c -r -m -nH -N -i $TMPFILE3; then
       echo "Download failed!"
    else
       echo "Download complete."
    fi

    # Cleanup temporary files
    rm -f $TMPFILE3 $TMPFILE2 $TMPFILE1
else
    # Index hasn't changed
    echo "Repo is already up-to-date."
fi
