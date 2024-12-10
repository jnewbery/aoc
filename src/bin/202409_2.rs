static _TEST_INPUT: &str = include_str!("202409_test_input.txt");
static _INPUT: &str = include_str!("202409_input.txt");

struct File {
    id: Option<i32>,
    start: i32,
    size: i32,
}

fn files_to_blocks(files: &Vec<File>) -> Vec<Option<i32>> {
    let mut blocks: Vec<Option<i32>> = Vec::new();
    let mut pos = 0;
    for file in files.iter() {
        while pos < file.start {
            blocks.push(None);
            pos += 1;
        }
        for _i in 0..file.size {
            blocks.push(Some(file.id.unwrap()));
            pos += 1;
        }
    }
    blocks
}

fn main() {
    let mut files: Vec<File> = Vec::new();
    let mut spaces: Vec<File> = Vec::new();
    let mut id = 0;
    let mut is_file = true;
    let mut pos = 0;

    for c in _INPUT.chars().take_while(|c| c.is_digit(10)).collect::<String>().chars() {
        // println!("{}", c);
        let current_size = c.to_digit(10).unwrap() as i32;
        match is_file {
            true => {
                files.push(File { id: Some(id), start: pos, size: current_size });
                pos += current_size;
                is_file = false;
                id += 1;
            },
            false => {
                spaces.push(File { id: None, start: pos, size: current_size });
                pos += current_size;
                is_file = true;
            }
        }
    }

    for file in files.iter_mut().rev() {
        for space in spaces.iter_mut() {
            if space.start > file.start { break; }
            if space.size >= file.size {
                // println!("Moving file {} from {} to {}", file.id.unwrap(), file.start, space.start);
                file.start = space.start;
                space.start += file.size;
                space.size -= file.size;
                break;
            }
        }
    }

    files.sort_by(|a, b| a.start.cmp(&b.start));

    let blocks = files_to_blocks(&files);

    let sol = blocks.iter().enumerate().fold(0 as i64, |acc, (i, x)| {
        match x {
            Some(b) => acc + (b * i as i32) as i64,
            None => acc,
        }
    });
    println!("{}", sol);
}
