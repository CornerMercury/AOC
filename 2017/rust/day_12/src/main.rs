use std::collections::{HashMap, HashSet};
use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    for line in input.lines() {}
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    Ok(())
}
