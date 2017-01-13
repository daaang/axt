the_terminal_is_very_narrow() {
  [ `tput cols` -lt 80 ]
}

echo_wide_success() {
  echo -n "[1;37;42m                                    Success."
  echo "                                    [0m"
}

echo_wide_failure() {
  echo -n "[1;37;41m                                    Failure."
  echo "                                    [0m"
}

echo_narrow_success() {
  echo "[32mSuccess.[0m"
}

echo_narrow_failure() {
  echo "[31mFailure.[0m"
}

echo_success() {
  if the_terminal_is_very_narrow; then
    echo_narrow_success

  else
    echo_wide_success
  fi
}

echo_failure() {
  if the_terminal_is_very_narrow; then
    echo_narrow_failure

  else
    echo_wide_failure
  fi
}

echo ""
if bash unittests/.quick_test.sh; then
  echo ""
  make clean
  echo_success

else
  echo ""
  echo_failure
fi
