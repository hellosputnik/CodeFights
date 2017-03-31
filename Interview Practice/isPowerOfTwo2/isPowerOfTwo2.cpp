bool isPowerOfTwo2(long long n) {
    if (n == 1)
        return true;
    if (n % 2 == 0)
        return isPowerOfTwo2(n / 2);
    else
        return false;
}

