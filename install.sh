#!/usr/bin/env bash

appdir=`pwd`

echo "Installing requirements..."
$appdir/bin/pip install -r requirements.txt

echo -e "\nDatabase setup..."
cd src
$appdir/dir/python cli.py setup required
cd $appdir

echo -e "\nWriting script..."
echo "#!/usr/bin/env bash
prevdir=\`pwd\`
appdir='$appdir'
cd \$appdir/src
\$appdir/bin/python cli.py \$@
cd \$prevdir" > ./flipkart

chmod +x ./flipkart
echo
echo -e "\nDone."
