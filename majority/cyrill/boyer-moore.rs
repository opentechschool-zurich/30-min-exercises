fn main() {
    println!("{:?}", majority(vec![1, 1, 2, 1, 3, 1]));
}

fn majority<I: PartialEq>(input: impl IntoIterator<Item = I>) -> Option<I> {
    let mut i = 0;
    let mut m = None;
    for x in input.into_iter() {
        if i == 0 {
            m = Some(x);
        } else if m == Some(x) {
            i += 1;
        } else {
            i -= 1;
        }
    }
    m
}
