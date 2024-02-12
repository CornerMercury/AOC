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
    let int_input: i32 = input.parse::<i32>().unwrap() - 1;
    let (x, y) = n_to_coords(int_input).unwrap();
    println!("{}", x.abs() + y.abs());
    Ok(())
}

fn n_to_coords(n: i32) -> Option<(i32, i32)> {
    let root: i32 = (n as f64).sqrt() as i32;
    let neg: i32 = [-1, 1][(root % 2) as usize];
    let diff: i32 = (root * (root + 1)) - n;
    let x = (root / 2 + root % 2) * neg + neg * (diff - diff.abs()) / 2;
    let y = (root / 2 + root % 2) * neg * -1_i32 + neg * (diff + diff.abs()) / 2;
    Some((x, y))
}

fn part2(input: &str) -> Result<()> {
    let mut coords_to_int = HashMap::new();
    let mut current_int = 1;
    let mut current_n = 1;
    coords_to_int.insert((0, 0), current_int);
    while current_int <= input.parse::<i32>().unwrap() {
        let coords = n_to_coords(current_n).unwrap();
        current_int = 0;
        for i in vec![-1, 0, 1] {
            for j in vec![-1, 0, 1] {
                if i != 0 || j != 0 {
                    match coords_to_int.get(&(coords.0 + i, coords.1 + j)) {
                        Some(num) => current_int += num,
                        _ => (),
                    }
                }
            }
        }
        current_n += 1;
        coords_to_int.insert(coords, current_int);
    }
    println!("{}", current_int);
    Ok(())
}
