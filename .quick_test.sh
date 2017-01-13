find_built_lib_dirs() {
  find build -maxdepth 1 -type d -name 'lib*'
}

count=`find_built_lib_dirs | wc -l`

if [ $count = 0 ]; then
  echo "Couldn't find any build/lib* directories."
  exit 1
fi

find_built_lib_dirs | while read base_lib; do
  echo "PYTHONPATH=$base_lib"
  if ! PYTHONPATH="$base_lib" python3 -m unittest; then
    exit 1
  fi
done
