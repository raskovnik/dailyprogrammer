fn plus_one(number: i32) -> String {
    let mut new = String::new();
    let x : String = number.to_string();
    for c in x.chars() {
        new.push_str(&(c.to_string().parse::<i32>().unwrap() + 1).to_string());
    }
    new
}

fn main(){
    println!("{}", plus_one(998));
}