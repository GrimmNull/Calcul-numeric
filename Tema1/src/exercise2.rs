
pub mod exercise {
    use std::borrow::Borrow;

    pub fn non_associative() {
        let a:f64 = 1.0;
        let mut u:f64 = 10.0;
        let b:f64 = u/10.0;
        let c:f64 = u/10.0;
        println!("u: {}", u);
        println!("b: {}", b);
        u+=10.0;
        println!("u: {}", u);
        println!("b: {}", b);
    }
}