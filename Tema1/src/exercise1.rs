
pub mod exercise {
    pub fn find_smallest() -> i32 {
        let mut power:i32 = 1;
        let u :f64 = 10.0;
        while 1.0 + f64::powf(u, -(power+1) as f64) != 1.0 {
            power+=1;
        }
        println!("Power: {}", power);
        println!("u: {}", f64::powf(u, -power as f64));
        println!("1 + u = {}", 1.0 + f64::powf(u, -(power+1) as f64));
        return power;
    }
}

