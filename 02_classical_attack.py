"""
=============================================================================
CLASSICAL ATTACK ON RSA (Brute Force Factorization)
=============================================================================
Demonstration of classical attack on RSA using factorization methods.
This shows why RSA is secure against classical computers - it takes
a VERY long time to factor large numbers.

Author: Quantum Crypto Education
=============================================================================
"""

import time
import math
from typing import Tuple, Optional
import random


def trial_division(n: int, verbose: bool = True) -> Tuple[Optional[int], Optional[int], float, int]:
    """
    Factorization using trial division (brute force).
    
    This is the simplest method - try all numbers
    from 2 to √n.
    
    Returns:
        - p: first factor (or None if prime)
        - q: second factor (or None if prime)
        - time_taken: time required
        - attempts: number of attempts
    """
    if verbose:
        print(f"\nTrying to factorize n = {n}")
        print("-" * 50)
    
    start_time = time.time()
    attempts = 0
    
    # Check for factor 2
    attempts += 1
    if n % 2 == 0:
        time_taken = time.time() - start_time
        return 2, n // 2, time_taken, attempts
    
    # Check odd numbers from 3 to √n
    i = 3
    sqrt_n = int(math.sqrt(n)) + 1
    
    while i <= sqrt_n:
        attempts += 1
        if n % i == 0:
            time_taken = time.time() - start_time
            if verbose:
                print(f"[OK] Factor found! {n} = {i} × {n // i}")
                print(f"   Attempts: {attempts:,}")
                print(f"   Time: {time_taken:.6f} seconds")
            return i, n // i, time_taken, attempts
        i += 2
        
        # Progress indicator for large numbers
        if verbose and attempts % 100000 == 0:
            print(f"   ... checked {attempts:,} candidates ...")
    
    time_taken = time.time() - start_time
    if verbose:
        print(f"[X] No factors found - {n} is prime!")
        print(f"   Attempts: {attempts:,}")
        print(f"   Time: {time_taken:.6f} seconds")
    return None, None, time_taken, attempts


def pollard_rho(n: int, verbose: bool = True) -> Tuple[Optional[int], Optional[int], float, int]:
    """
    Pollard's Rho algorithm - more efficient than trial division.
    
    Uses cycle detection (Floyd's algorithm) to
    find factors faster.
    
    Still EXPONENTIAL in complexity!
    """
    if verbose:
        print(f"\nPollard's Rho on n = {n}")
        print("-" * 50)
    
    start_time = time.time()
    attempts = 0
    
    if n % 2 == 0:
        return 2, n // 2, time.time() - start_time, 1
    
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    
    while d == 1:
        attempts += 1
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = math.gcd(abs(x - y), n)
        
        if attempts > n:  # Safety limit
            break
    
    time_taken = time.time() - start_time
    
    if d != n and d != 1:
        if verbose:
            print(f"[OK] Factor found! {n} = {d} × {n // d}")
            print(f"   Iterations: {attempts:,}")
            print(f"   Time: {time_taken:.6f} seconds")
        return d, n // d, time_taken, attempts
    
    if verbose:
        print(f"[X] Failed to find factors")
    return None, None, time_taken, attempts


def demo_classical_attack():
    """Demo classical attack on various RSA sizes."""
    
    print("\n" + "=" * 70)
    print("CLASSICAL ATTACK DEMONSTRATION")
    print("=" * 70)
    
    # Test cases with different sizes
    test_cases = [
        ("Tiny (8-bit)", 143),           # 11 × 13
        ("Small (16-bit)", 10403),        # 101 × 103
        ("Medium (24-bit)", 1018081),     # 1009 × 1009
        ("Larger (32-bit)", 2147483659),  # 46337 × 46351
    ]
    
    results = []
    
    for name, n in test_cases:
        print(f"\n{'='*60}")
        print(f"Test: {name}")
        print(f"   n = {n} ({n.bit_length()} bits)")
        print("=" * 60)
        
        # Trial Division
        p, q, time_td, attempts_td = trial_division(n)
        
        # Pollard's Rho
        p2, q2, time_pr, attempts_pr = pollard_rho(n)
        
        results.append({
            'name': name,
            'n': n,
            'bits': n.bit_length(),
            'td_time': time_td,
            'td_attempts': attempts_td,
            'pr_time': time_pr,
            'pr_attempts': attempts_pr
        })
    
    # Summary
    print("\n" + "=" * 70)
    print("RESULTS SUMMARY")
    print("=" * 70)
    print(f"{'Size':<20} {'Bits':>6} {'Trial Div Time':>15} {'Pollard Time':>15}")
    print("-" * 70)
    for r in results:
        print(f"{r['name']:<20} {r['bits']:>6} {r['td_time']:>14.6f}s {r['pr_time']:>14.6f}s")
    
    return results


def estimate_rsa_crack_time():
    """Estimate time to crack real RSA keys."""
    
    print("\n" + "=" * 70)
    print("ESTIMATED TIME TO CRACK RSA (Classical Computer)")
    print("=" * 70)
    
    # Assumptions based on current technology
    # Best known classical algorithm: General Number Field Sieve
    # Complexity: exp((64/9)^(1/3) * (ln n)^(1/3) * (ln ln n)^(2/3))
    
    estimates = [
        ("RSA-512", 512, "< 1 day", "BROKEN (1999)"),
        ("RSA-768", 768, "~2 years", "BROKEN (2009)"),
        ("RSA-1024", 1024, "~1000 years", "Theoretically vulnerable"),
        ("RSA-2048", 2048, "~10^15 years", "Current standard"),
        ("RSA-4096", 4096, "~10^30 years", "High security"),
    ]
    
    print(f"\n{'Key Size':<12} {'Bits':>6} {'Est. Time (Classical)':>25} {'Status':>25}")
    print("-" * 70)
    for name, bits, time_est, status in estimates:
        print(f"{name:<12} {bits:>6} {time_est:>25} {status:>25}")
    
    print("""
    
    [!] IMPORTANT: 
    
    The estimates above are for the BEST available CLASSICAL COMPUTERS!
    
    With QUANTUM COMPUTER (Shor's Algorithm):
    ┌─────────────────────────────────────────────────────────────────┐
    │  Shor's Algorithm provides EXPONENTIAL SPEEDUP                  │
    │  Complexity: O(n³) vs O(exp(n^(1/3))) for GNFS                  │
    │                                                                 │
    │  HOWEVER currently:                                             │
    │  • Requires ~4000 LOGICAL qubits with error correction          │
    │  • This equals MILLIONS of physical qubits with current tech    │
    │  • IBM/Google currently have ~1000 physical qubits              │
    │                                                                 │
    │  Prediction: 2030-2040 quantum computers MAY threaten RSA       │
    └─────────────────────────────────────────────────────────────────┘
    """)


def complexity_comparison():
    """Compare classical vs quantum complexity."""
    
    print("\n" + "=" * 70)
    print("COMPLEXITY COMPARISON: CLASSICAL vs QUANTUM")
    print("=" * 70)
    
    print("""
    FACTORING n (where n ≈ 2^k, k = bit length):
    
    ┌────────────────────────────────────────────────────────────────────┐
    │  ALGORITHM                    │  COMPLEXITY           │  TYPE      │
    ├────────────────────────────────────────────────────────────────────┤
    │  Trial Division               │  O(√n) = O(2^(k/2))   │  Classical │
    │  Pollard's Rho                │  O(n^(1/4))           │  Classical │
    │  Quadratic Sieve              │  O(exp(√(k·ln(k))))   │  Classical │
    │  General Number Field Sieve   │  O(exp(k^(1/3)))      │  Classical │
    ├────────────────────────────────────────────────────────────────────┤
    │  SHOR'S ALGORITHM             │  O(k³) = O((log n)³)  │  QUANTUM   │
    └────────────────────────────────────────────────────────────────────┘
    
    KEY DIFFERENCE:
    
    • Classical: EXPONENTIAL in bit size (k)
      - Time increases DRASTICALLY with key size
      - RSA-2048 is practically impossible to break
    
    • Quantum (Shor): POLYNOMIAL in bit size (k)
      - Time increases SLOWLY with key size
      - RSA-2048 can be broken in reasonable time!
    
    Example for RSA-2048 (k = 2048):
    
    • Classical (GNFS): ~2^100 operations ≈ 10^30 operations
      → Takes trillions of years
    
    • Quantum (Shor): ~2048³ ≈ 8.6 × 10^9 operations
      → Tractable with large enough quantum computer
      → HOWEVER requires ~4000 logical qubits + error correction (not yet available)
    
    CONCLUSION:
    Shor's Algorithm provides EXPONENTIAL SPEEDUP!
    This threat is REAL but the timeline is still debated (est. 2030-2040).
    """)


if __name__ == "__main__":
    print("=" * 70)
    print("  QUANTUM CRYPTO EDUCATION - Part 2: Classical Attack  ")
    print("=" * 70)
    
    # Run demo
    demo_classical_attack()
    estimate_rsa_crack_time()
    complexity_comparison()
    
    print("\n" + "=" * 70)
    print("--> NEXT: See 03_shors_algorithm.py for QUANTUM attack!")
    print("=" * 70)
