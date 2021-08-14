fn main() {
    let mut a = [1, 2, 3, 3, 5, 6, 7, 8, 9];
    for i in 0..a.len() {
        for j in 1..a.len() {
            if a[i] % 2 == 0 &&  a[j] % 2 != 0 {
                a.swap(i, j);
            }
        }
    }
    println!("{:?}", a);
}