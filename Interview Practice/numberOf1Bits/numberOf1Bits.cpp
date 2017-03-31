int numberOf1Bits(int n) {
    int number = 0;

    while (n) {
        if (n & 1)
            ++number;
        n >>= 1;
    }

    return number;
}

