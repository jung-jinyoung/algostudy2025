// 방법의 종류 : n더하기, 2곱하기 3곱하기

function solution(x, y, n) {
    var answer = 0;
    const matrix = [];
    for (let i = 0; i < y+1; i++) {
        matrix.push(0)
    }
    
    matrix[y] = 1;
    for (let i = y-1; i > 0; i--) {
        if (i < x) break
        // 여기서 세개의 케이스 비교
        let val = 987654321;
        const third = y >= 3 * i && matrix[3*i] !== 0 ? matrix[3*i] + 1 : null;
        const second = y >= 2 * i && matrix[2*i] !== 0 ? matrix[2*i] + 1 : null;
        const plus = y >= i + n && matrix[i+n] !== 0 ? matrix[i+n] + 1 : null;
        const candidates = [third, second, plus];
        for (candidate of candidates) {
            if (candidate !== null) {
                if (val > candidate) {
                    val = candidate
                }
            }
        }
        if (val !== 987654321) {
            matrix[i] = val
        }
    }
    
    return matrix[x]-1;
}
