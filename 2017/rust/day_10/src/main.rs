use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let lengths: Vec<usize> = input
        .split(",")
        .map(|x| x.parse::<usize>().unwrap())
        .collect();
    let vec_length: usize = 256;
    let mut list: Vec<u8> = (0..=255).collect();
    let mut skip: usize = 0;
    let mut pos: usize = 0;
    for length in &lengths {
        for i in 0..(*length / 2) {
            let temp = list[(i + pos) % vec_length];
            list[(i + pos) % vec_length] = list[(pos + length - i - 1) % vec_length];
            list[(pos + length - i - 1) % vec_length] = temp;
        }
        pos += (length + skip) % vec_length;
        skip += 1;
    }
    println!("{:?}", list[0] as u32 * list[1] as u32);
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let mut lengths: Vec<usize> = input.bytes().map(|x| x as usize).collect();
    let mut extra: Vec<usize> = vec![17, 31, 73, 47, 23];
    lengths.append(&mut extra);
    let vec_length: usize = 256;
    let mut list: Vec<u8> = (0..=(vec_length - 1) as u8).collect();
    let mut skip: usize = 0;
    let mut pos: usize = 0;
    for _ in 0..64 {
        for length in &lengths {
            for i in 0..(*length / 2) {
                let temp = list[(i + pos) % vec_length];
                list[(i + pos) % vec_length] = list[(pos + length - i - 1) % vec_length];
                list[(pos + length - i - 1) % vec_length] = temp;
            }
            pos += (length + skip) % vec_length;
            skip += 1;
        }
    }

    let mut hash = String::new();
    for chunk in list.chunks(16) {
        hash.push_str(&format!("{:02x}", chunk.iter().fold(0, |res, &x| res ^ x)));
    }
    println!("{hash}");
    Ok(())
}
