echo_success() {
  if [ `tput cols` -lt 80 ]; then
    echo "[32mSuccess.[0m"

  else
    echo -n "[1;37;42m                                    Success."
    echo "                                    [0m"
  fi
}

echo_failure() {
  if [ `tput cols` -lt 80 ]; then
    echo "[31mFailure.[0m"

  else
    echo -n "[1;37;41m                                    Failure."
    echo "                                    [0m"
  fi
}

echo ""
if bash .quick_test.sh; then
  echo ""
  make clean
  echo_success

else
  echo ""
  echo_failure
fi
