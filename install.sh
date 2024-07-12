#!/usr/bin/env bash

curdir=`pwd`

echo "#!/usr/bin/env bash
prevdir=\`pwd\`
appdir='$curdir'
pydir='bin/python'
cd \$appdir/src
\$appdir/\$pydir cli.py \$@
cd \$prevdir" > ./flipkart

chmod +x ./flipkart
