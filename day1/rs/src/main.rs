use std::fs::read_to_string;

const NUMBERS:&[&str] = &[
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine"
];

fn get_calibration_value(line:&str) -> u32 {
    let mut first:i32 = -1;
    let mut firstpos:usize = 0xfffff;
    let mut last:i32 = 0;
    let mut lastpos:usize = 0xfffff;

    for (i, c) in line.chars().enumerate() {
        if c.is_numeric() {
            let n = c.to_digit(10).unwrap() as i32;
            if first == -1 {
                first = n;
                firstpos = i;
            }
            last = n;
            lastpos = i;
        }
    }
    for (i,n) in NUMBERS.iter().enumerate() {
        if let Some(p) = line.find(n) {
            if p < firstpos {
                first = i as i32 + 1;
                firstpos = p;
            }
        }
        if let Some(p) = line.rfind(n) {
            if p > lastpos{
                last = i as i32 + 1;
                lastpos = p;
            }
        }
    };
    (first * 10 + last) as u32
}

fn main() {
    let mut sum = 0;
    for line in read_to_string("day1/input.txt").unwrap().lines() {
        sum += get_calibration_value(line);
    }
    println!("Sum: {sum}");
    
}
