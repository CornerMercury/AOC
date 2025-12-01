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
    let mut nums: Vec<i32> = input.lines().map(|c| c.parse::<i32>().unwrap()).collect();
    let mut i: i32 = 0;
    while 0 <= i && i < nums.len() as i32 {
        let n = nums[i as usize];
        nums[i as usize] += 1;
        i += n;
        total += 1;
    }
    println!("{}", total);
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut total = 0;
    let mut nums = input
        .lines()
        .map(|c| c.parse::<i32>().unwrap())
        .collect::<Vec<i32>>()
        .into_boxed_slice();
    let mut i: i32 = 0;
    while 0 <= i && i < nums.len() as i32 {
        let n = nums[i as usize];
        if n >= 3 {
            nums[i as usize] -= 1;
        } else {
            nums[i as usize] += 1;
        }
        i += n;
        total += 1;
    }
    println!("{}", total);
    Ok(())
}
