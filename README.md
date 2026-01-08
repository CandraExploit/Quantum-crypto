#  Quantum Threat to Encryption

Comprehensive educational project demonstrating why quantum computing threatens current encryption and what solutions exist.

> **Disclaimer**: This is an educational project with simplified implementations. Not for production use.

##  Visualizations

### Classical vs Quantum Complexity
![Complexity Comparison](visualizations/01_complexity_comparison.png)

### Quantum Speedup Factor
![Quantum Speedup](visualizations/02_quantum_speedup.png)

### Threat Timeline
![Threat Timeline](visualizations/03_threat_timeline.png)

### Algorithm Security Comparison
![Algorithm Security](visualizations/04_algorithm_comparison.png)

### Qubit Progress
![Qubit Progress](visualizations/05_qubit_progress.png)

---

##  What You'll Learn

1. **How RSA works** - The encryption protecting the internet
2. **Why RSA is secure (classically)** - Prime factorization is hard
3. **Shor's Algorithm** - Quantum algorithm that breaks RSA
4. **The Timeline** - When will quantum computers break encryption?
5. **Post-Quantum Solutions** - NIST standards (Kyber, SPHINCS+)
6. **Advanced Implementations** - LWE, Lattice-based crypto

## 📁 Project Structure

```
QuantumCrypto/
├── 01_rsa_basics.py           # RSA encryption fundamentals
├── 02_classical_attack.py     # Brute force factorization (slow)
├── 03_shors_algorithm.py      # Quantum attack using Qiskit
├── 04_comparison.py           # Classical vs Quantum complexity
├── 05_post_quantum.py         # NIST post-quantum standards
├── 06_visualizations.py       # Generate threat visualizations
├── 07_advanced_post_quantum.py # LWE, Kyber, SPHINCS+ implementations
├── visualizations/
│   ├── 01_complexity_comparison.png
│   ├── 02_quantum_speedup.png
│   ├── 03_threat_timeline.png
│   ├── 04_algorithm_comparison.png
│   └── 05_qubit_progress.png
├── requirements.txt
└── README.md
```

##  Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run each module
python 01_rsa_basics.py
python 02_classical_attack.py
python 03_shors_algorithm.py
python 04_comparison.py
python 05_post_quantum.py
python 06_visualizations.py      # Generates charts
python 07_advanced_post_quantum.py  # Advanced implementations
```

## ⚠️ Key Takeaways

| Encryption | Classical (GNFS) | Quantum (Shor) | Notes |
|------------|------------------|----------------|-------|
| RSA-2048 | Sub-exponential | **Polynomial O(n³)** | Requires ~4000 logical qubits with error correction |
| AES-256 | ~2^256 | ~2^128 (Grover) | Still secure with sufficient margin |
| Kyber-768 | Secure | Secure | NIST FIPS 203 (ML-KEM) |
| SPHINCS+ | Secure | Secure | NIST FIPS 205 (SLH-DSA) |

**Important Notes:**
- The polynomial vs sub-exponential complexity difference is the key threat
- Current quantum computers (~1000 physical qubits) lack sufficient qubits AND error rates for cryptographic attacks
- ~4000 logical qubits needed = millions of physical qubits with current technology
- Timeline for cryptographically-relevant quantum computers remains debated (estimates: 2030-2040)
- NIST has set 2035 as the deadline to deprecate quantum-vulnerable algorithms

## 🔐 Post-Quantum Algorithms Covered

| Algorithm | Type | Use Case | NIST Standard |
|-----------|------|----------|---------------|
| **CRYSTALS-Kyber** | Lattice-based | Key Exchange | FIPS 203 (ML-KEM) |
| **CRYSTALS-Dilithium** | Lattice-based | Digital Signatures | FIPS 204 (ML-DSA) |
| **SPHINCS+** | Hash-based | Digital Signatures | FIPS 205 (SLH-DSA) |
| **LWE** | Learning With Errors | Encryption basis | - |

## 📚 References

- Shor, P.W. (1994). "Algorithms for quantum computation: discrete logarithms and factoring"
- Gidney & Ekerå (2021). "How to factor 2048 bit RSA integers in 8 hours using 20 million noisy qubits"
- [NIST Post-Quantum Cryptography](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [IBM Quantum](https://quantum-computing.ibm.com/)
- [Open Quantum Safe](https://openquantumsafe.org/)
- [Qiskit](https://qiskit.org/)

## License

MIT License - Educational use.

---

**⚠️ Important**: This project demonstrates the *theoretical* threat. Current quantum computers cannot break RSA-2048. Timeline estimates vary (2030-2040). Begin planning migration to post-quantum cryptography now.
