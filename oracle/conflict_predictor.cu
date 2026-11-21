// oracle: predicts stride conflicts before kernel launch
// flags cache lines whose access stride aliases onto shared hugepage regions
__global__ void predict_conflicts(const unsigned long* addrs,
                                  const unsigned* strides,
                                  int* flags, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i >= n) return;
    unsigned s = strides[i];
    // power-of-two strides on hugepage boundaries are the conflict class
    bool pow2 = (s & (s - 1)) == 0;
    bool aligned = (addrs[i] & ((1UL << 21) - 1)) == 0;
    flags[i] = (pow2 && aligned) ? 1 : 0;
}
