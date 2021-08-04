use std::collections::HashMap;

fn main() {
   let characters = "dbbaCEDbdAacCEAadcB";
   let mut map = HashMap::new();
   for charr in characters.chars() {
      match charr {
         'A'..='Z' => {
            let count = map.entry(charr.to_string().to_lowercase()).or_insert(0);
            *count -= 1;
         },
         'a'..='z' => {
            let count = map.entry(charr.to_string().to_lowercase()).or_insert(0);
            *count += 1;
         }
         _ => continue
      }
   }
   println!("{:?}", map);
}