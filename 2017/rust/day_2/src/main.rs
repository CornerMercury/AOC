use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let mut total = 0;
    for line in input.lines() {
        let nums: Vec<u32> = line
            .split_whitespace()
            .map(|c| c.parse::<u32>().unwrap())
            .collect();
        total += nums.iter().max().unwrap() - nums.iter().min().unwrap()
    }
    println!("{}", total);
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut total = 0;
    for line in input.lines() {
        let nums: Vec<u32> = line
            .split_whitespace()
            .map(|c| c.parse::<u32>().unwrap())
            .collect();
        for num1 in &nums {
            for num2 in &nums {
                if num1 != num2 && (num1 % num2 == 0 || num1 % num2 == 0) {
                    let tup = vec![num1, num2];
                    total += *tup.iter().max().unwrap() / *tup.iter().min().unwrap();
                }
            }
        }
    }
    println!("{}", total);
    Ok(())
}
