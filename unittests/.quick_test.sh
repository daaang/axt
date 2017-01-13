find_built_lib_dirs() {
  find build -maxdepth 1 -type d -name 'lib*' 2> /dev/null
}

error_out_if_project_is_not_built() {
  number_of_lib_dirs=`find_built_lib_dirs | wc -l`

  if [ $number_of_lib_dirs = 0 ]; then
    echo "Couldn't find any build/lib* directories. Be sure you've run"
    echo "\`make build\` before running tests. Or better yet, just run"
    echo "\`make test\`."
    exit 1
  fi
}

test_with_pythonpath() {
  echo "PYTHONPATH=$1"
  if ! PYTHONPATH="$1" python3 -m unittest; then
    exit 1
  fi
}

test_every_lib_dir() {
  find_built_lib_dirs | while read base_lib; do
    test_with_pythonpath "$base_lib"
  done
}

error_out_if_project_is_not_built
test_every_lib_dir
