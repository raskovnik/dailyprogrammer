//rust implementation of problem number 388 on r/dailyprogrammer
fn main() {
    let mut x : u32 = 2133;
    loop{
        x += 1;
        if x == reverse(x) {
            println!{"{}",x};
            break
        }
    }
}

fn reverse(x: u32) -> u32 { 
    let my_str: String = format!("{:?}", x);
    let reversed = my_str.chars().rev().collect::<String>();
    let my_num = reversed.parse::<u32>().unwrap();
    my_num
}
