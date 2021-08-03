use std::collections::HashMap;

fn char_count() {
    let text = "xxxyyy";
    let mut map = HashMap::new();

    for charr in text.chars() {
        let count = map.entry(charr).or_insert(0);
        *count += 1;
    }
    let mut val = 0;
    match &map.values().next() {
        None => val = 0,
        Some(i) => val += **i,
    }
   for value in map.values() {
        if value < &val || value > &val {
            println!("False");
            break;
        }
        println!("True");
   }
}

fn main() {
    char_count();
}