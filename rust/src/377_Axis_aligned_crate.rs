fn crates(rw: i32, rl:i32, cw: i32, cl: i32) ->i32 {
    (rw / cw) * (rl / cl)
}

fn main(){
    println!("{}",crates(25, 18, 6, 5));
    println!("{}", crates(12, 34, 5, 6))
}