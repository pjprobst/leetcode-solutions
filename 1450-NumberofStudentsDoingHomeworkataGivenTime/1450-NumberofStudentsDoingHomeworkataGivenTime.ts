// Last updated: 9/16/2025, 7:38:55 PM
function majorityElement(nums: number[]): number {
    const m = new Map()

    for (const n of nums){
        if (m.has(n)) {
            m.set(n, m.get(n) + 1)
        } else {
            m.set(n, 1)
        }
    }

    return Array.from(m.entries()).sort((a, b) => b[1] - a[1])[0][0]
};