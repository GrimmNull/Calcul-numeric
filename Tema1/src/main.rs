mod exercise1;
mod exercise2;
mod exercise3;


use std::f64::consts::PI;
use exercise1::exercise::find_smallest;
use exercise2::exercise::non_associative;
use exercise3::exercise::{computed_sin, computed_cos, computed_ln};

fn main() {
    let machine_precision = find_smallest();
    println!();
    non_associative(machine_precision);
    println!();
    println!();

    let degree_sin: f64 = 0.5;
    println!("sin(x):");
    println!("x = {}", degree_sin);
    let library_sin = ((1.0 / 4.0) * PI * degree_sin).sin();
    let own_sin = computed_sin(degree_sin);
    println!("Library: {}", library_sin);
    println!("Computed: {}", own_sin);
    println!("Error margin: {}", f64::abs(library_sin - own_sin));

    println!();
    let degree_cos: f64 = 0.5;
    println!("cos(x):");
    println!("x = {}", degree_cos);
    let library_cos = ((1.0 / 4.0) * PI * degree_cos).cos();
    let own_cos = computed_cos(degree_cos);
    println!("Library: {}", library_cos);
    println!("Computed: {}", own_cos);
    println!("Error margin: {}", f64::abs(library_cos - own_cos));
    println!();

    let ln_arg: f64 = 0.8;
    let library_ln = f64::ln(ln_arg);
    let own_ln = computed_ln(ln_arg);
    println!("ln(x):");
    println!("x = {}", ln_arg);
    println!("Library: {}", library_ln);
    println!("Computed: {}", own_ln);
    println!("Error margin: {}", f64::abs(library_ln - own_ln));
}