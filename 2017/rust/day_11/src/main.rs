use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let split = input.split(",");
    let mut pos: [i32; 3] = [0, 0, 0];
    for dir in split {
        let change: [i32; 3] = match dir {
            "n" => [1, 0, -1],
            "ne" => [1, -1, 0],
            "se" => [0, -1, 1],
            "s" => [-1, 0, 1],
            "sw" => [-1, 1, 0],
            "nw" => [0, 1, -1],
            _ => unimplemented!(),
        };
        pos[0] += change[0];
        pos[1] += change[1];
        pos[2] += change[2];
    }
    println!("{:?}", pos.iter().map(|x| x.abs()).max().unwrap());
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let split = input.split(",");
    let mut pos: [i32; 3] = [0, 0, 0];
    let mut max = 0;
    for dir in split {
        let change: [i32; 3] = match dir {
            "n" => [1, 0, -1],
            "ne" => [1, -1, 0],
            "se" => [0, -1, 1],
            "s" => [-1, 0, 1],
            "sw" => [-1, 1, 0],
            "nw" => [0, 1, -1],
            _ => unimplemented!(),
        };
        pos[0] += change[0];
        pos[1] += change[1];
        pos[2] += change[2];
        if pos.iter().map(|x| x.abs()).max().unwrap() > max {
            max = pos.iter().map(|x| x.abs()).max().unwrap()
        }
    }
    println!("{}", max);
    Ok(())
}
