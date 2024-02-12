use std::collections::HashMap;
use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let mut registers: HashMap<String, i32> = HashMap::new();
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let register = split[0].to_string();
        if !registers.contains_key(&register) {
            registers.insert(register.clone(), 0);
        }
        let increment = [-1, 1][(split[1] == "inc") as usize];
        let num = split[2].parse::<i32>().unwrap();
        let cmp_num = split[6].parse::<i32>().unwrap();
        let cmp_register = split[4].to_string();
        if !registers.contains_key(&cmp_register) {
            registers.insert(cmp_register.clone(), 0);
        }
        let cmp_value = registers[&cmp_register];
        let cmp = match split[5] {
            ">" => cmp_value > cmp_num,
            "<" => cmp_value < cmp_num,
            "<=" => cmp_value <= cmp_num,
            ">=" => cmp_value >= cmp_num,
            "==" => cmp_value == cmp_num,
            "!=" => cmp_value != cmp_num,
            _ => unimplemented!(),
        };
        if cmp {
            if let Some(x) = registers.get_mut(&register) {
                *x += increment * num
            }
        }
    }
    println!(
        "{}",
        registers
            .into_values()
            .collect::<Vec<i32>>()
            .iter()
            .max()
            .unwrap()
    );
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut max = 0;
    let mut registers: HashMap<String, i32> = HashMap::new();
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        let register = split[0].to_string();
        if !registers.contains_key(&register) {
            registers.insert(register.clone(), 0);
        }
        let increment = [-1, 1][(split[1] == "inc") as usize];
        let num = split[2].parse::<i32>().unwrap();
        let cmp_num = split[6].parse::<i32>().unwrap();
        let cmp_register = split[4].to_string();
        if !registers.contains_key(&cmp_register) {
            registers.insert(cmp_register.clone(), 0);
        }
        let cmp_value = registers[&cmp_register];
        let cmp = match split[5] {
            ">" => cmp_value > cmp_num,
            "<" => cmp_value < cmp_num,
            "<=" => cmp_value <= cmp_num,
            ">=" => cmp_value >= cmp_num,
            "==" => cmp_value == cmp_num,
            "!=" => cmp_value != cmp_num,
            _ => unimplemented!(),
        };
        if cmp {
            if let Some(x) = registers.get_mut(&register) {
                *x += increment * num;
                if *x > max {
                    max = *x;
                }
            }
        }
    }
    println!("{max}");
    Ok(())
}
