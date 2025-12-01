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
    let mut left = HashSet::new();
    let mut right = HashSet::new();
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        left.insert(split[0]);
        for i in 3..split.len() {
            match split[i].strip_suffix(",") {
                Some(str) => right.insert(str),
                _ => right.insert(split[i]),
            };
        }
    }
    println!(
        "{}",
        left.symmetric_difference(&right)
            .collect::<HashSet<_>>()
            .iter()
            .next()
            .unwrap()
    );
    Ok(())
}

struct Node {
    weight: u32,
    children: Vec<String>,
}

fn part2(input: &str) -> Result<()> {
    let mut left = HashSet::new();
    let mut right = HashSet::new();
    let mut nodes: HashMap<String, Node> = HashMap::new();
    for line in input.lines() {
        let split: Vec<&str> = line.split_whitespace().collect();
        left.insert(split[0].to_string());

        let mut children: Vec<String> = vec![];
        if split.len() > 2 {
            for i in 3..split.len() {
                let child = split[i].strip_suffix(",").unwrap_or(split[i]).to_string();
                right.insert(child.clone());
                children.push(child.clone());
            }
        }
        let node = Node {
            weight: split[1]
                .replace("(", "")
                .replace(")", "")
                .parse::<u32>()
                .unwrap(),
            children: children,
        };
        nodes.insert(split[0].to_string(), node);
    }

    let root_list = left.symmetric_difference(&right).collect::<HashSet<_>>();
    let root = root_list.iter().next().unwrap();

    find_error(&root, &nodes);
    Ok(())
}

fn calculate_weight(name: &String, graph: &HashMap<String, Node>) -> u32 {
    let node = graph.get(name).unwrap();
    let mut weight = node.weight;
    for c in &node.children {
        weight += calculate_weight(c, &graph);
    }
    weight
}

fn find_error(name: &String, graph: &HashMap<String, Node>) -> u32 {
    let node = graph.get(name).unwrap();
    let weights: Vec<u32> = node
        .children
        .iter()
        .map(|x| calculate_weight(x, &graph))
        .collect();

    for weight in &weights {
        if *weight != weights[0] {
            println!(
                "{:?} {:?}",
                weights,
                node.children
                    .iter()
                    .map(|x| graph[x].weight)
                    .collect::<Vec<u32>>()
            );
            for child in &node.children {
                find_error(child, &graph);
            }
        }
    }
    0
}
