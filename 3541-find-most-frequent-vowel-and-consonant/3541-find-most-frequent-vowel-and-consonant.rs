use std::collections::HashMap;

impl Solution {
    pub fn max_freq_sum(s: String) -> i32 {
        let mut max_vowels = 0;
        let mut max_consonants = 0;
        let vowels = vec!['a', 'e', 'i', 'o', 'u'];
        let mut dict = HashMap::new();

        let str_arr = String::from(s);


        for v in str_arr.chars() {
            if dict.contains_key(&v) {
                dict.insert(v, dict.get(&v).unwrap() + 1);
            } else {
                dict.insert(v, 1);
            }
        }

        for (key, val) in &dict {
            if vowels.contains(&key) {
                if val > &max_vowels {
                    max_vowels = *val;
                }
            } else {
                if val > &max_consonants {
                    max_consonants = *val;
                }
            }
        }

        return max_vowels + max_consonants;
    }
}