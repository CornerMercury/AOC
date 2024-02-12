use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let mut total: u32 = 0;
    let mut last_char = '-';
    let first_char = input.chars().next().unwrap();
    for char in format!("{}{}", input, first_char).chars() {
        if last_char == char {
            total += char.to_digit(10).unwrap();
        }
        last_char = char;
    }
    println!("{}", total);
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut total: u32 = 0;
    let first_char = input.chars().next().unwrap();
    let left = format!("{}{}", input, first_char);
    let r = format!("{}{}", input, input);
    let mut right = r.chars();
    let len = input.len();
    for _ in 0..len / 2 {
        right.next();
    }
    for (l, r) in left.chars().zip(right) {
        if l == r {
            total += r.to_digit(10).unwrap();
        }
    }
    println!("{}", total);
    Ok(())
}
