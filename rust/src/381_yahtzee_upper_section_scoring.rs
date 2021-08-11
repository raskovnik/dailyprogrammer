use std::collections::HashMap;
use std::fs::File;
use std::io::BufReader;
use std::io::BufRead;


fn main() {
    let mut scores = HashMap::new();
    let reader = BufReader::new(File::open("381.txt").expect("Cannot open file"));
    // for line in reader.lines() {
    //     println!("{:?}", line.unwrap().parse::<i32>().unwrap());
    // }
    for line in reader.lines() {
        let num = line.unwrap().parse::<i64>().unwrap();
        let count = scores.entry(num).or_insert(0);
        *count += num;
    }
    let mut val = 0;
    for value in scores.values() {
        if value > &val {
            val = *value;
        }

    }
    println!("{}", val);
}