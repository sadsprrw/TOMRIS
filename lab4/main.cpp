static int_precision stirling_first_optimizedloop(int_precision& nip, int_precision& kip, const bool sign = false) {
    const int_precision c0(0), c1(1);  const int n = int(nip), k = int(kip);
    std::vector<int_precision> cnk((size_t)n + 1,0);
    int_precision im1;
    if (k==0 && n==0 || k==n) return c1;
    if (k==0 || n==0 || k>n) return c0;
    cnk[1] = c1;
    for (int i = 1; i < n; ++i) {
        im1 = int_precision(i);
        for (int j = i+1; j > 0; --j)
            cnk[j] = cnk[j - 1] + im1 * cnk[j];
    }
    return sign == true && (n - k) & 0x1 ? -cnk[k] : cnk[k];
}