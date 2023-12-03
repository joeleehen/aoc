use std::fs::read_to_string;

fn main() {
    let mut sum = 0;

    for line in read_to_string("input.txt").unwrap().lines() {
        sum += get_digits(line);
    }

    println!("{}", sum);
}

fn get_digits(line: &str) -> i32 {
    // iterate across the line and grab the digits
    let mut left = 'x';
    let mut right = 'x';
    let cline = line.chars();

    for letter in cline {
        if letter.is_numeric() {
            if left == 'x' {
                left = letter;
            }
        right = letter;
        }
    }
    let mut digits = String::from("");
    digits.push(left);
    digits.push(right);

    let int_digits: i32 = digits.parse().unwrap();

    int_digits
}
