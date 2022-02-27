
pub mod exercise {
    use std::borrow::Borrow;

    pub fn non_associative(machine_precision: i32) {
        let mut a:f64 = 1.0;
        let mut u:f64 = f64::powf(10.0, -machine_precision as f64);
        let mut b:f64 = u/10.0;
        let mut c:f64 = u/10.0;

        if (a + b) + c == a + (b + c) {
            println!("The addition still stands");
        } else {
            println!("The addition doesn't stand");
        }

        a = 0.1;
        b= 0.2;
        c = 0.3;

        if (a * b) * c == a * (b * c) {
            println!("The multiplication still stands");
            println!("{}", (a * b) * c);
            println!("{}", a * (b * c));
        } else {
            println!("The multiplication doesn't stand");
            println!("{}", (a * b) * c);
            println!("{}", a * (b * c));
        }
    }
}