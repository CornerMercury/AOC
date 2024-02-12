use std::collections::HashSet;
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
        let split: Vec<&str> = line.split_whitespace().collect();
        if split.len() == HashSet::<_>::from_iter(split).len() {
            total += 1;
        }
    }
    println!("{}", total);
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut total = 0;
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let mut can_be_rearranged = false;
        for i in 0..split.len() {
            if can_be_rearranged {
                break;
            }
            let mut s1 = split[i].chars().collect::<Vec<_>>();
            s1.sort_by(|a, b| b.cmp(a));
            for j in 0..split.len() {
                let mut s2 = split[j].chars().collect::<Vec<_>>();
                s2.sort_by(|a, b| b.cmp(a));
                if i != j && s1 == s2 {
                    can_be_rearranged = true;
                    break;
                }
            }
        }
        if can_be_rearranged == false {
            total += 1;
        }
    }
    println!("{}", total);
    Ok(())
}
