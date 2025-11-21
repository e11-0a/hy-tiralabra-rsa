#!/bin/bash

# Hiljainen rm
rm test_primes.txt &>/dev/null

# Luodaan 25 alkulukua openssl:n avulla
for i in {0..24}; do
    openssl prime -generate -bits 2048 >> test_primes.txt
done