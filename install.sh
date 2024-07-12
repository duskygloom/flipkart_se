#!/usr/bin/env bash

curdir=`pwd`

echo "Installing requirements..."
$curdir/bin/pip install -r requirements.txt

echo "Writing script..."
echo "#!/usr/bin/env bash
prevdir=\`pwd\`
appdir='$curdir'
cd \$appdir/src
\$appdir/bin/python cli.py \$@
cd \$prevdir" > ./flipkart

chmod +x ./flipkart
