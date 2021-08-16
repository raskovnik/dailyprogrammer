fn main() {
    let result = at_cipher(String::from("foo!bar"));
    println!("{}",result);
}

fn at_cipher(text: String) -> String {
    let alphabet = "abcdefghijklmnopqrstuvwxyz";
    let mut cipher = String::new();
    for c in text.chars() {
        if alphabet.contains(c){
            let c_idx = alphabet.find(c).unwrap();
            cipher.push(*&alphabet.chars().nth(25 - c_idx).unwrap());
        } else {
            cipher.push(c);
        }
    }
    return cipher;
}