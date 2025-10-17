function solution(a, b) {
    const A = String(a) + String(b);
    const B = 2 * Number(a) * Number(b);
    
    return A >= B ? Number(A) : B;
}