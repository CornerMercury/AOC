use std::fs;

type Result<T> = ::std::result::Result<T, Box<dyn (::std::error::Error)>>;

fn main() -> Result<()> {
    let input = fs::read_to_string("src/i.txt").expect("Should have been able to read the file");
    part1(&input)?;
    part2(&input)?;
    Ok(())
}

fn part1(input: &str) -> Result<()> {
    let chars: Vec<char> = input.chars().collect();
    let mut i: usize = 0;
    let mut total = 0;
    let mut depth = 1;
    let mut in_garbage = false;
    while i < input.len() {
        let current_char = chars[i];
        if current_char == '!' {
            i += 1;
        } else {
            if in_garbage {
                if current_char == '>' {
                    in_garbage = false;
                }
            } else {
                match current_char {
                    '{' => {
                        total += depth;
                        depth += 1;
                    }
                    '}' => depth -= 1,
                    '<' => in_garbage = true,
                    ',' => (),
                    _ => unimplemented!(),
                }
            }
        }
        i += 1;
    }
    println!("{total}");
    Ok(())
}

fn part2(input: &str) -> Result<()> {
    let chars: Vec<char> = input.chars().collect();
    let mut i: usize = 0;
    let mut total = 0;
    let mut in_garbage = false;
    while i < input.len() {
        let current_char = chars[i];
        if current_char == '!' {
            i += 1;
        } else {
            if in_garbage {
                if current_char == '>' {
                    in_garbage = false;
                } else {
                    total += 1;
                }
            } else {
                match current_char {
                    '{' => (),
                    '}' => (),
                    '<' => in_garbage = true,
                    ',' => (),
                    _ => unimplemented!(),
                }
            }
        }
        i += 1;
    }
    println!("{total}");
    Ok(())
}
