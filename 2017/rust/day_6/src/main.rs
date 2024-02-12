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
    let mut total = 0;
    let mut vec_nums: Vec<u32> = input
        .split_whitespace()
        .map(|c| c.parse::<u32>().unwrap())
        .collect();
    let mut set = HashSet::new();
    let len = vec_nums.len();
    while !set.contains(&format!("{:?}", vec_nums)) {
        total += 1;
        set.insert(format!("{:?}", vec_nums));
        let mut max = 0;
        let mut max_index = 0;
        for i in 0..len {
            if vec_nums[i] > max {
                max = vec_nums[i];
                max_index = i;
            }
        }
        vec_nums[max_index] = 0;
        let add = max / len as u32;
        let rem = max % len as u32;
        for i in 0..len {
            if i < rem as usize {
                vec_nums[(max_index + i + 1) % len] += add + 1;
            } else {
                vec_nums[(max_index + i + 1) % len] += add;
            }
        }
    }
    println!("{}", total);

    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut total = 0;
    let mut vec_nums: Vec<u32> = input
        .split_whitespace()
        .map(|c| c.parse::<u32>().unwrap())
        .collect();
    let mut dict = HashMap::new();
    let len = vec_nums.len();
    while !dict.contains_key(&format!("{:?}", vec_nums)) {
        dict.insert(format!("{:?}", vec_nums), total);
        total += 1;
        let mut max = 0;
        let mut max_index = 0;
        for i in 0..len {
            if vec_nums[i] > max {
                max = vec_nums[i];
                max_index = i;
            }
        }
        vec_nums[max_index] = 0;
        let add = max / len as u32;
        let rem = max % len as u32;
        for i in 0..len {
            if i < rem as usize {
                vec_nums[(max_index + i + 1) % len] += add + 1;
            } else {
                vec_nums[(max_index + i + 1) % len] += add;
            }
        }
    }
    println!("{}", total - dict[&format!("{:?}", vec_nums)]);

    Ok(())
}
