fn sum_digits(n: i32) -> i32 {
    let mut total = 0;
    let mut num: i32 = n;
    while num != 0 {
        total += num % 10;
        num /= 10;
    }
    total
}

fn persistence(number: i32) -> i32 {
    let mut num: i32 = number;
    let mut sums = 0;
    while num > 9 {
        num = sum_digits(num);
        sums += 1;
    }
    sums
}

fn main() {
    let a : i32 = 1234;
    let result = persistence(a);
    println!("{}", result);
}