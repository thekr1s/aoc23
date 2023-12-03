use std::fs::read_to_string;


fn main() {
    let mut sum:u32 = 0;
    let mut max_sum = 0;
    let mut vals: Vec<u32> = vec![];
    for line in read_to_string("2022/day1/rs/input.txt").unwrap().lines() {
        let line = line.trim();
        if line.len() == 0 {
            vals.push(sum);
            if sum > max_sum{
                max_sum = sum;
            }
            sum = 0;
        } else {
            sum += line.parse::<u32>().unwrap();
        }
    }
    vals.sort();
    let n = vals.len();
    let sum = vals[n-1] + vals[n-2] + vals[n-3];
    println!("{sum}");
    
}
